import re
import os
from collections import namedtuple
from Toolkit.LabelGenerator import LabelGenerator
from Toolkit.LookAhead import LookAhead
from Toolkit.functions import scanpattern, safewrite, loctoline

class Token(namedtuple('Token', ('value', 'type', 'loc'))):
    """ Override __new__ method to create default (None) values for namedtuple
    
    >>> Token(value="foobar")
    Token(value='foobar', type=None, loc=None)
    >>> Token("foo", "bar")
    Token(value='foo', type='bar', loc=None)
    """
    
    def __new__(cls, value=None, type=None, loc=None):
        return super(Token, cls).__new__(cls, value, type, loc)
        
kinds = ("static", "field", "argument", "local")
    
class UnknownKind(Exception):
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        
        return "Unknown kind: %s\nMust be one of %s" % (self.kind, str(kinds))
    
class SymbolTable:
    
    def __init__(self):
        self.classScope = {}
        self.startSubroutine()
        self.classnames = []
        
    def setClass(self, classname):
        if classname in self.classnames:
            raise Exception("%s class already defined." % classname)
        
        self.classnames.append(classname)
        
        self.classname = classname
        
    def startSubroutine(self):
        self.subScope = {}
        
    def define(self, kind, type, name):
        
        if kind not in kinds:
            raise UnknownKind(kind)
        
        symbol = namedtuple("symbol", ['kind', 'type', 'index'])
        
        if kind in ("field", "static"):
            
            name = ".".join((self.classname, name))
            
            if name not in self.classScope.keys():
                self.classScope[name]=symbol(kind, type, self.varCount(kind))
            else:
                raise Exception("\"%s\" identifier \"%s\" already defined as \"%s\" in class (%s) scope."\
                % (kind, name, self.classScope[name].type, self.classScope[name].kind))
        else:
            
            if name not in self.subScope.keys():
                self.subScope[name]=symbol(kind, type, self.varCount(kind))
                
            else:
                raise Exception("\"%s\" identifier \"%s\" already defined as \"%s\" in subroutine (%s) scope."\
                % (kind, name, self.subScope[name].type, self.subScope[name].kind))

    def varCount(self, kind):
        
        if kind not in kinds:
            raise UnknownKind(kind)

        if kind in ("field", "static"):
            return sum(1 for name in self.classScope.keys() if self.classScope[name].kind == kind)
        else:
            return sum(1 for name in self.subScope.keys() if self.subScope[name].kind == kind)

            

          
    def typeOf(self, name):
        
        if name in self.subScope.keys():
            return self.subScope[name].type
        elif name in self.classScope.keys():
            return self.classScope[name].type
            
        elif ".".join((self.classname, name)) in self.classScope.keys():
            return self.classScope[".".join((self.classname, name))].type
        else:
            return None
    
    def indexOf(self, name):
        
        if name in self.subScope.keys():
            return self.subScope[name].index
        elif name in self.classScope.keys():
            return self.classScope[name].index
        
        elif ".".join((self.classname, name)) in self.classScope.keys():
            return self.classScope[".".join((self.classname, name))].index

        else:
            return None
    
    def kindOf(self, name):
        kind = None
        
        if name in self.subScope.keys():
            kind = self.subScope[name].kind
            
        elif name in self.classScope.keys():
            kind = self.classScope[name].kind
        
        # a little patch for static variables
        elif ".".join((self.classname, name)) in self.classScope.keys():
            kind = self.classScope[".".join((self.classname, name))].kind
            
        if kind == "field":
            kind = "this"
            
        return kind

class VMWrite:
    
    def __init__(self, overwrite=False):
        
        self.overwrite = overwrite
    
    def openfile(self, outfile):
        
        if not (self.overwrite or not os.path.exists(outfile)):
            raise Exception("File %s already exists" % outfile)
            
        self.outfile = open(outfile, "wt")
        self.filestart = True
        
    def closefile(self):
        self.outfile.close()

    def _paddedwrite(self, *args, padding=1):
        """ write some newlines and then write some data.
            padding = number of newlines to be added.
        """
        
        if self.filestart:
            self.filestart = False
        else:
            for i in range(padding):
                self.outfile.write("\n")
        
        self.outfile.write(*args)
        
    def push(self, segment, index):
        if segment in ("constant", "local", "static", "argument",\
                       "this", "that", "pointer", "temp"):
            self._paddedwrite("push %s %d" % (segment, index))
        else:
            raise Exception("Unknown segment: %s" % segment)

    def pop(self, segment, index):
        if segment in ("constant", "local", "static", "argument",\
                       "this", "that", "pointer", "temp"):
            self._paddedwrite("pop %s %d" % (segment, index))
        else:
            raise Exception("Unknown segment: %s" % segment)
    
    def arithmetic(self, command):
        if command in ("add, sub, neg, eq, gt, lt, and, or, not"):
            self._paddedwrite(command)
        else:
            raise Exception("Unknown command: %s" % command)

            
            
    def label(self, label):
        self._paddedwrite("label %s" % label)

    
    def goto(self, label):
        self._paddedwrite("goto %s" % label)

        
    def ifgoto(self, label):
        self._paddedwrite("if-goto %s" % label)

        
    def call(self, name, nArgs):
        self._paddedwrite("call %s %d" % (name, nArgs))

    
    def function(self, name, nLocals):
        self._paddedwrite("//", padding=2)
        self._paddedwrite("function %s %d" % (name, nLocals))
        self._paddedwrite("//")
    
    def ret(self):
        self._paddedwrite("return")

class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on the input
    (or raise a SyntaxError if it doesn't match).
    '''
    def __init__(self, programdir, inputextension=".jack", outputextension=".vm", overwrite=False):
        
        self.symbols = SymbolTable()
        
        
        
        dirname = os.path.dirname(programdir)
        
        self.vmwriter = VMWrite(overwrite)
        
        inputfiles = [os.path.join(programdir, name) for name in os.listdir(programdir)
                       if name.endswith(inputextension)]

        for inputfile, filename, basename in [(open(f), f, os.path.splitext(f)[0]) for f in inputfiles]:
                        
            self.vmwriter.openfile(basename + outputextension)
            
            try:
                self.parse(inputfile.read())
            except Exception as e:
                print("\nIn file: { %s }" % filename)
                raise e

            self.vmwriter.closefile()
        
    
    def parse(self, text):
        
        self.loctoline = loctoline(text)
        tokenizer = ExpressionEvaluator._tokenize(text)
        self.tokens = LookAhead(tokenizer)

        
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Next symbol tokenized
        self._advance()         # Load first lookahead token
        
        self.p_class()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
        
    def _accept(self, Token):
        'Test and consume the next token if it matches Token'
        
        val, type, _ = Token
        
        if Token.value:
            if isinstance(Token.value, str):
                val = [Token.value]
                
            if self.nexttok and self.nexttok.value in val:
                self._advance()
                return True
            else:
                return False
            
        elif Token.type:
            if isinstance(Token.type, str):
                type = [Token.type]
            if self.nexttok and self.nexttok.type in type:
                self._advance()
                return True
            else:
                return False
                
    def _expect(self, Token):
        'Consume next token if it matches Token or rase Exception'
        if not self._accept(Token):
            
            if self.nexttok:
                type = self.nexttok.type
                value = self.nexttok.value
                line = self.loctoline(self.nexttok.loc)
            else:
                raise Exception("Unexpected End of File on line %d" % self.loctoline(self.tok.loc))

                
            if Token.value:
                raise Exception("Found %s \"%s\" on line %d: expected \"%s\""\
                 % (type, value, line, Token.value))
            elif Token.type:
                raise Exception("Found %s \"%s\" on line %d: expected %s"\
                 % (type, value, line, Token.type))
    
    def _tokenize(text):
        """Returns a generator that yields Token objects
           Also strips out line and block comments.
        """
        
        keywords = { "class", "constructor", "function", "method",
                     "field", "static", "var", "int", "char", "boolean",
                     "void", "true", "false", "null", "this", "let",
                     "do", "if", "else", "while", "return" }
                
        symbols =  { "{", "}", "(", ")", "[", "]",
                     ".", ",", ";", "+", "-", "*",
                     "/", "&", "|", "<", ">", "=", "~", "!" }

        line_comment    = r"(?P<line_comment>//.*\n)"
        block_comment   = r"(?P<block_comment>\/\*[^*]*\*+([^/][^*]*\*+)*\/)"
        string          = r"(?P<stringConstant>\".*\")"
        integer         = r"(?P<integerConstant>\d+)"
        symbol          = "(?P<symbol>\\" + "|\\".join(str(s) for s in symbols) + ")"
        keyword         = r"(?P<keyword>\b" + "\b|\b".join(str(s) for s in keywords) + "\b)"
        whitespace      = r"(?P<whitespace>\s+)"
        identifier      = r"(?P<identifier>\w+)"
        
        master_pat = "|".join((block_comment, line_comment, string, integer, symbol, keyword, whitespace, identifier))
        
        ignore_types = 'whitespace', 'block_comment', 'line_comment'
        
        for scanmatch in scanpattern(master_pat, text, ignore_types):
            yield Token(value=scanmatch.value, type=scanmatch.type, loc=scanmatch.loc)
                

    ##### Grammar rules follow #####
    
    
    ##### Program Structure #####
    

    
    def p_class(self):
        "(class ::= 'class' className '{' classVarDec subroutineDec '}')*"
        
        while self._accept(Token(value="class")):
  
            self.classname = self.p_className()
            
            self.symbols.setClass(self.classname)
            
            self._expect(Token(value="{"))

            self.p_classVarDec()
            
            self.p_subroutineDec()
                
            self._expect(Token(value="}"))
        
            if self.nexttok:
                if self.nexttok.value != "class":
                    raise Exception("Found %s \"%s\" on line %d: expected class"\
                 % (self.tok.type, self.tok.value, self.loctoline(self.tok.loc)))


        
    def p_classVarDec(self):
        "classVarDec ::= (('static' | 'field') type varName (',' varName)* ';'?)*"
        
        while self._accept(Token(value=("static", "field"))):
            
            kind = self.tok.value
            
            type = self.p_type()
            
            name = self.p_varName()
            
            self.symbols.define(kind, type, name)
            
            while self._accept(Token(value=",")):
                
                name = self.p_varName()
                
                self.symbols.define(kind, type, name)
                
            self._accept(Token(value=";"))
        
    def p_type(self):
        "type ::= 'int' | 'char' | 'boolean' | className"
        
        if self._accept(Token(value=("int", "char", "boolean"))):
            pass
        else:
            self._expect(Token(type="identifier"))
        
        return self.tok.value
        
    def p_parameterList(self):
        "parameterList   ::= (type varName) (',' type varName)*"
        
        kind = "argument"
        type = self.p_type()
        name = self.p_varName()
        
        if self.functype == "method":
            self.symbols.define(kind, "int", "this")
            
        self.symbols.define(kind, type, name)
        
        while self._accept(Token(value=",")):
            
            type = self.p_type()
            name = self.p_varName()
            self.symbols.define(kind, type, name)
        
    def p_subroutineDec(self):
        "subroutineDec ::= (('constructor' | 'function' | 'method') \
                           ('void' | type) subroutineName '(' (parameterList)? ')'\
                             subroutineBody)*"
        
        
        while self._accept(Token(value=("constructor", "function", "method"))):
            
            self.symbols.startSubroutine()
            
            self.functype = self.tok.value
            

            if self._accept(Token(value="void")):
                self.returntype = "void"
            else:
                self.returntype = self.p_type()
            
            if self.functype == "constructor" and self.tok.value != self.classname:
                raise Exception("constructor of %s must return %s, not %s" % (self.classname, self.classname, self.tok.value))
            
            self.subname = self.p_subroutineName()
            
            self.labels = LabelGenerator(".".join((self.classname, self.subname)))
            
            self._expect(Token(value="("))
            
            if self.nexttok.value != ")":
                
                self.p_parameterList()
            
                
            self._expect(Token(value=")"))

            self.p_subroutineBody()
            
    def p_subroutineBody(self):
        "subroutineBody  ::= '{' varDec statements '}'"
        
        self.returnedproperly = False
        
        self._expect(Token(value="{"))
            
        self.p_varDec()
        
        numvars = self.symbols.varCount("local")
        
        # add one to numvars if this is a method
        
        if self.functype == "method":

            numvars += 1
                
        self.vmwriter.function(".".join((self.classname, self.subname)), numvars)
        
        
        
        if self.functype == "constructor":
            
            # allocate memory for this object and point to its base
            numfields = self.symbols.varCount("field")
            
            if numfields == 0:
                raise Exception("class %s constructor has no fields on line %d" % (self.classname, self.loctoline(self.tok.loc)))
                
            self.vmwriter.push("constant", numfields)
            self.vmwriter.call("Memory.alloc", 1)
            self.vmwriter.pop("pointer", 0)
        
        elif self.functype == "method":
            self.vmwriter.push("argument", 0)
            self.vmwriter.pop("pointer", 0)
            
            
        if self.nexttok.value != "}":
            self.p_statements()
        
        self._expect(Token(value="}"))
    
        if not self.returnedproperly:
            "automatically return"
            if self.functype == "constructor":
                self.vmwriter.push("pointer", 0)
            self.vmwriter.ret()
            
    def p_varDec(self):
        "varDec ::= ('var' type varName (',' varName)*)* ';'?"
        
        while self._accept(Token(value="var")):
            
            kind = "local"

            type = self.p_type()
            
            name = self.p_varName()
            
            self.symbols.define(kind, type, name)
        
            while self._accept(Token(value=",")):
                
                name = self.p_varName()
                
                self.symbols.define(kind, type, name)

            self._accept(Token(value=";"))

    def p_className(self):
        self._expect(Token(type="identifier"))
        return(self.tok.value)
        
    def p_varName(self):
        self._expect(Token(type="identifier"))
        return(self.tok.value)
        
    def p_subroutineName(self):
        self._expect(Token(type="identifier"))
        return(self.tok.value)


    #### Statements ####


    def p_statements(self):
        
        "statement  ::= (letStatement | ifStatement | whileStatement |\
                         doStatement)* returnStatement"

        while self.nexttok.value in ("let", "if", "while", "do", "return"):
            
            if self.nexttok.value=="let":
                self.p_letStatement()
                    

            elif self.nexttok.value=="if":
                self.p_ifStatement()
                self.returnedproperly = False

            elif self.nexttok.value=="while":
                self.p_whileStatement()
                self.returnedproperly = False
            
            elif self.nexttok.value=="do":
                self.p_doStatement()
                    
        
            elif self.nexttok.value=="return":
                self.p_returnStatement()
                
                    
                if self.nexttok.value == "}":
                    if self.functype == "constructor" and self.tok.value != "this":
                        self.returnedproperly = False
                    else:
                        self.returnedproperly = True
                
        
        
        
    def p_letStatement(self):
        "letStatement ::= 'let' varName ('[' expression ']')? '=' expression ';'?"
        
        isarray = False
        
        self._expect(Token(value="let"))
        
        self._expect(Token(type="identifier"))
        
        varName = self.tok.value
        
            
        if self._accept(Token(value="[")):
            
            isarray = True
            
            self.vmwriter.push(self.symbols.kindOf(varName), self.symbols.indexOf(varName))
            
            self.p_expression()

            self.vmwriter.arithmetic("add")
            
            self.vmwriter.pop("pointer", 1)
            
            self._expect(Token(value="]"))
        
        
        # process the expression
        
        self._expect(Token(value="="))
        
        self.p_expression()
            
        if isarray:
            self.vmwriter.pop("that", 0)

            
        else:
                
            if not self.symbols.kindOf(varName):
                raise Exception("Unknown symbol %s on line %d" % (varName, self.loctoline(self.tok.loc)))
            
            self.vmwriter.pop(self.symbols.kindOf(varName), self.symbols.indexOf(varName))

        self._accept(Token(value=";"))

    def p_ifStatement(self):
        "ifStatement ::= 'if' expression '{' statements '}'\
                         ('else' '{' statements '}')?"
        
        iflabel = self.labels.next("if")
        
        self._expect(Token(value="if"))
        
        self.p_expression()
            
        # this may look a bit odd, but it pushes the result of the expression
        # back onto the stack to be tested by the (optional) else statement. 
        
        self.vmwriter.pop("temp", 1)
        self.vmwriter.push("temp", 1)
        self.vmwriter.push("temp", 1)
        
        self.vmwriter.arithmetic("not")
        
        self.vmwriter.ifgoto(iflabel)
        
        self._expect(Token(value="{"))
        self.p_statements()
        self._expect(Token(value="}"))
        
        if self._accept(Token(value="else")):
            gotolabel = self.labels.next("goto")
            
            self.vmwriter.label(iflabel)
            
            # here's where we can consume and test the expression's value.
            self.vmwriter.ifgoto(gotolabel)
            
            self._expect(Token(value="{"))
            self.p_statements()
            self._expect(Token(value="}"))
            
            self.vmwriter.label(gotolabel)
        else:
            self.vmwriter.label(iflabel)
            self.vmwriter.pop("temp", 1)
            
    def p_whileStatement(self):
        "whileStatement ::= 'while'  expression '{' statements '}'"
        
        startlabel = self.labels.next("while")
        stoplabel = self.labels.next("while")
        
        self._expect(Token(value="while"))
        
        self.vmwriter.label(startlabel)
            
        self.p_expression()

        self.vmwriter.arithmetic("not")
        self.vmwriter.ifgoto(stoplabel)
        
        self._expect(Token(value="{"))
        self.p_statements()
        
        self._expect(Token(value="}"))
        
        self.vmwriter.goto(startlabel)
        self.vmwriter.label(stoplabel)
            
    def p_doStatement(self):
        "doStatement ::= 'do' subroutineCall ';'?"

        self._expect(Token(value="do"))
        self.p_subroutineCall()
        
        self.vmwriter.pop("temp", 0)
        
        self._accept(Token(value=";"))

    def p_returnStatement(self):
        "returnStatement ::= 'return' expression? ';'?"
        
        self._expect(Token(value="return"))
        
        if self.returntype == "void":
            self.vmwriter.push("constant", 0)
            
        else:
            self.p_expression()
        
        self.vmwriter.ret()
            
        self._accept(Token(value=";"))


##### Expressions #####


    def p_expression(self):
        "expression ::= term (op term)*"
        
        op = {  "+": "add",
                "-": "sub",
                "&": "and",
                "|": "or",
                "<": "lt",
                ">": "gt",
                "=": "eq"}
                        
        self.p_term()
            
        while self._accept(Token(value=list(op.keys()) + ["*", "/"])):
            
            myop = self.tok.value
            loc = self.tok.loc
                        
            self.p_term()
            
            
            if myop == "*":
                self.vmwriter.call("Math.multiply", 2)
                    
            elif myop == "/":
                self.vmwriter.call("Math.divide", 2)
                    
            elif myop in op.keys():
                self.vmwriter.arithmetic(op[myop])
            
            else:
                raise Exception("Unknown op: \"%s\" on line %d"\
                % (myop, loc))
                    
    def p_term(self):
        "term ::= integerConstant | stringConstant | keywordConstant |\
                  varName | varName '[' expression ']' | subroutineCall |\
                  '(' expression ')' | unaryOp term"

        keywordConstant = "true", "false", "null", "this"
 
        unaryOp = "-", "~", "!"
        
        if self._accept(Token(value="(")):
            
            self.p_expression()

            self._expect(Token(value=")"))
        
        elif self._accept(Token(type=("integerConstant"))):
        
            self.vmwriter.push("constant", int(self.tok.value))
                
             
        elif self._accept(Token(type=("stringConstant"))):
            
            string = self.tok.value.strip("\"")
            
            self.vmwriter.push("constant", len(string))
            
            self.vmwriter.call("String.new", 1)
            
            for c in [ord(c) for c in string]:
                self.vmwriter.push("constant", c)
                self.vmwriter.call("String.appendChar", 2)
            
        elif self._accept(Token(value=keywordConstant)):
            
            k = self.tok.value
            
            if k == "this":
                self.vmwriter.push("pointer", 0)
                    
            else:
                self.vmwriter.push("constant", 0)
                    
            if k == "true":
                self.vmwriter.arithmetic("not")

        
        elif self._accept(Token(value=unaryOp)):
            
            myop = self.tok.value

            self.p_term()
    
            if myop == "-":
                self.vmwriter.arithmetic("neg")
                    
            elif myop in ("~", "!"):
                self.vmwriter.arithmetic("not")

        
        elif self.nexttok.type=="identifier":
                
                look = self.tokens[0]
                
                if look.value in (".", "("):
                            
                            # call subroutine
                    self.p_subroutineCall()
                        
                        
                elif look.value == "[":
                    
                    # this is an array
                    
                    self._expect(Token(type="identifier"))
                    
                    # save the array pointer so that we don't 
                    # mess it up for any other nested expressions
                    
                    self.vmwriter.push("pointer", 1)
                    
                    self.vmwriter.push(self.symbols.kindOf(self.tok.value), self.symbols.indexOf(self.tok.value))
                
                    self._expect(Token(value="["))
                    
                    self.p_expression()

                    self.vmwriter.arithmetic("add")
                    
                    self._expect(Token(value="]"))
                    
                    # juggle the returned value just a little bit
                    # this prevents nested arrays from clobbering each
                    # other's pointers
                    
                    self.vmwriter.pop("pointer", 1)
                    self.vmwriter.push("that", 0)
                    self.vmwriter.pop("temp", 2)
                    self.vmwriter.pop("pointer", 1)
                    self.vmwriter.push("temp", 2)

                else:
                    
                    # this is a varName
                    self._expect(Token(type="identifier"))
                    name = self.tok.value
                    
                    if not self.symbols.kindOf(name):
                        raise Exception("Unknown identifier: %s on line %d" % (name, self.loctoline(self.tok.loc)))
                        
                    self.vmwriter.push(self.symbols.kindOf(name), self.symbols.indexOf(name))
                    
                        

    def p_expressionList(self):
        "expressionList  ::= expression (',' expression)*"

        exps = 1
        
        self.p_expression()
            
        
        while self._accept(Token(value=",")):
            
            exps += 1
            self.p_expression()
                
        return exps

    def p_subroutineCall(self):
        "subroutineCall ::= subroutineName '(' (expressionList)? ')' |\
                            (className | varName) '.' subroutineName \
                            '(' (expressionList)? ')'"
        
        
        self._expect(Token(type="identifier"))
        
        # right now, name could be a subroutineName, a className, or a varName
        
        name = self.tok.value
        
        if self._accept(Token(value="(")):
            
            """ this is a class method belonging to the class we're 
             currently in
            """
            
            self.vmwriter.push("pointer", 0)
            numArgs = 1
            
            if self.nexttok.value != ")":
                numArgs += self.p_expressionList()
                
            self._expect(Token(value=")"))
            
            name = ".".join((self.classname, name))

            
        else:
            
            self._expect(Token(value="."))
            self._expect(Token(type="identifier"))
            
            varType = self.symbols.typeOf(name)
            subroutineName = self.tok.value

            if varType:
                """ this is an object method
                    varType will be the class of the method to be 
                    called
                """
                
                if  not self.symbols.kindOf(name):
                    raise Exception("Unknown symbol: %s on line %d" % (name, self.loctoline(self.tok.loc)))
                    
                kind, index = (self.symbols.kindOf(name), self.symbols.indexOf(name))
            
                self.vmwriter.push(kind, index)
            
                name = ".".join((varType, subroutineName))
                
                numArgs = 1
                
            else:
                # this is some other class method
                name = ".".join((name, subroutineName))
                numArgs = 0
                
            
            self._expect(Token(value="("))
            
            
            if self.nexttok.value != ")":
                numArgs += self.p_expressionList()
                
            self._expect(Token(value=")"))


        self.vmwriter.call(name, numArgs)
        
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ExpressionEvaluator("./Square")
                    





