import re



class Lookahead:
    from itertools import tee, islice
    
    """Wrap an iterator with lookahead indexing
    
    >>> L = Lookahead([5, 3, 1, 5, 6, 3])
    
    >>> next(L)
    5
    >>> next(L)
    3
    >>> L[0]
    1
    >>> L[1]
    5
    >>> next(L)
    1
    """

    
    def __init__(self, iterator):
        self.t = tee(iterator, 1)[0]
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.t)
    def __getitem__(self, i):
        for value in islice(self.t.__copy__(), i, None):
            return value
        raise IndexError(i)


from collections import namedtuple

class Token(namedtuple('Token', ['value', 'type', 'loc'])):
    """ Override __new__ method to create default (None) values for namedtuple
    
    >>> Token(value="foobar")
    Token(value='foobar', type=None, loc=None)
    >>> Token("foo", "bar")
    Token(value='foo', type='bar', loc=None)
    """
    
    def __new__(cls, value=None, type=None, loc=None):
        return super(Token, cls).__new__(cls, value, type, loc)
        

             
def loctoline(text):
    """Take a given text and produce a data structure S such that
    S[loc] will yield the line number in text
    
    >>> loctoline("foo\\nbar")
    (1, 1, 1, 1, 2, 2, 2)
    """
    
    s = []
    num = 1
    
    for char in text:
        if char == "\n":
            s.append(num)
            num += 1
        else:
            s.append(num)
    
    return tuple(s)
    

def tokenize(text):
    """Returns a generator that yields Token objects
       Also strips out line and block comments.
    """
    
    keywords = { "class", "constructor", "function", "method",
                 "field", "static", "var", "int", "char", "boolean",
                 "void", "true", "false", "null", "this", "let",
                 "do", "if", "else", "while", "return" }
            
    symbols =  { "{", "}", "(", ")", "[", "]",
                 ".", ",", ";", "+", "-", "*",
                 "/", "&", "|", "<", ">", "=", "~" }

    line = loctoline(text)

    line_comment    = r"(?P<L_comment>//.*\n)"
    block_comment   = r"(?P<B_comment>\/\*[^*]*\*+([^/][^*]*\*+)*\/)"
    string          = r"(?P<stringConstant>\".*\")"
    integer         = r"(?P<integerConstant>\d+)"
    symbol          = r"(?P<symbol>\\" + "|\\".join(str(s) for s in symbols) + ")"
    keyword         = r"(?P<keyword>" + "|".join(str(s) for s in keywords) + ")"
    ws              = r"(?P<ws>\s+)"
    identifier      = r"(?P<identifier>\w+)"

    master_pat = re.compile("|".join([block_comment, line_comment, string, integer, symbol, keyword, ws, identifier]))
    
    scanner = master_pat.scanner(text)
    
    for m in iter(scanner.match, None):
        value = m.group()
        type = m.lastgroup
        loc = m.start()
        
        if type not in ['ws', 'B_comment', 'L_comment']:
            yield (Token(value, type, loc))

def tag(value=None, tag=None):
    return("<%s>%s</%s>" % (tag, value, tag))

class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on the input
    (or raise a SyntaxError if it doesn't match).
    '''
    
    def parse(self, text):
        self.loctoline = loctoline(text)
        self.tokens = Lookahead(tokenize(text))
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Next symbol tokenized
        self._advance()         # Load first lookahead token
        
        parsedText = ""
        
        for i in self.p_class():
            parsedText += i
        
        return parsedText
        
    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
    
    def _accept(self, Token):
        'Test and consume the next token if it matches Token'
        
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
            if self.nexttok and self.nexttok.type in Token.type:
                self._advance()
                return True
            else:
                return False
                
    
    def _expect(self, Token):
        'Consume next token if it matches Token or rase Exception'
        if not self._accept(Token):
            line = self.loctoline[self.nexttok.loc]
            if Token.value:
                raise Exception("Found %s \"%s\" on line %d: expected \"%s\""\
                 % (self.nexttok.type, self.nexttok.value, line, Token.value))
            elif Token.type:
                raise Exception("Found %s \"%s\" on line %d: expected %s"\
                 % (self.nexttok.type, self.nexttok.value, line, Token.type))
            
            
                
    ##### Grammar rules follow #####
    
    
    ##### Program Structure #####
    
    
   
    def p_class(self):
        "class ::= 'class' className '{' classVarDec* subroutineDec* '}'"
        
        self._expect(Token(value="class"))
        yield("<class>")
        yield(tag(tag=self.tok.type, value=self.tok.value))
  
        for y in self.p_className():
            yield (y)
        
        self._expect(Token(value="{"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        for y in self.p_classVarDec():
            yield(y)
            
        for y in self.p_subroutineDec():
            yield(y)
        
        self._expect(Token(value="}"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</class>")
        
    def p_classVarDec(self):
        "classVarDec ::= ('static' | 'field') type varName (',' varName)* ';'"
        
        while self._accept(Token(value=("static", "field"))):
            yield("<classVarDec>")
            
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_type():
                yield y
            
            for y in self.p_varName():
                yield y
            
            while self._accept(Token(value=",")):
                yield(tag(tag=self.tok.type, value=self.tok.value))
                
                for y in self.p_varName():
                    yield y
                
            self._expect(Token(value=";"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

            yield("</classVarDec>")
            
    def p_type(self):
        "type ::= 'int' | 'char' | 'boolean' | className"
        
        if self._accept(Token(value=("int", "char", "boolean"))):
            
            yield(tag(tag=self.tok.type, value=self.tok.value))
        else:
            for y in self.p_className():
                yield y
        
    def p_parameterList(self):
        "parameterList   ::= ((type varName) (',' type varName)*)?"
        for y in self.p_type():
            yield y
            
        if self._accept(Token(type="identifier")):
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
        
        while self._accept(Token(value=",")):
            
            for y in self.p_type():
                yield y
            
            self._expect(Token(type="identifier"))
        
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
    def p_subroutineDec(self):
        "subroutineDec ::= ('constructor' | 'function' | 'method') \
                           ('void' | type) subroutineName '(' parameterList ')'\
                             subroutineBody"
                             
        while self._accept(Token(value=("constructor", "function", "method"))):
            
            yield("<subroutineDec>")
            
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            if self._accept(Token(value="void")):
                yield(tag(tag=self.tok.type, value=self.tok.value))
            else:
                for y in self.p_type():
                    yield y
            
            for y in self.p_subroutineName():
                yield y
            
            self._expect(Token(value="("))
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_parameterList():
                yield y
                
            self._expect(Token(value=")"))
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_subroutineBody():
                yield y
            
            yield ("</subroutineDec>")
            
    def p_subroutineBody(self):
        "subroutineBody  ::= '{' varDec* statements '}'"
        
        yield ("<subroutineBody>")
        
        self._expect(Token(value="{"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
            
        for y in self.p_varDec():
            yield y
        
        for y in self.p_statements():
            yield y
        
        self._expect(Token(value="}"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield ("</subroutineBody>")
    
    def p_varDec(self):
        "varDec ::= 'var' type varName (',' varName)* ';'"
        
        while self._accept(Token(value="var")):
            yield(tag(tag=self.tok.type, value=self.tok.value))

            for y in self.p_type():
                yield y
        
            self._expect(Token(type="identifier"))
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
            while self._accept(Token(value=",")):
                self._expect(Token(type="identifier"))
                yield(tag(tag=self.tok.type, value=self.tok.value))

            self._expect(Token(value=";"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

    
    def p_className(self):
        if self._accept(Token(type="identifier")):
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
    def p_varName(self):
        if self._accept(Token(type="identifier")):
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
    def p_subroutineName(self):
        if self._accept(Token(type="identifier")):
            yield(tag(tag=self.tok.type, value=self.tok.value))

        
    #### Statements ####
        
    def p_statements(self):
        "statements ::= statement*"
                             
        yield("<statements>")
        
        "statement  ::= letStatement | ifStatement | whileStatement |\
                        doStatement | returnStatement"

        while self.nexttok.value in ("let", "if", "while", "do", "return"):
            
            if self.nexttok.value=="let":

                for y in self.p_letStatement():
                    yield y

            elif self.nexttok.value=="if":

                for y in self.p_ifStatement():
                    yield y

            elif self.nexttok.value=="while":

                for y in self.p_whileStatement():
                    yield y
            
            elif self.nexttok.value=="do":
                
                for y in self.p_doStatement():
                    yield y

            elif self.nexttok.value=="return":
                
                for y in self.p_returnStatement():
                    yield y
                    
        yield("</statements>")
    
                    
    def p_letStatement(self):
        "letStatement ::= 'let' varName ('[' expression ']')? '=' expression ';'"
        
        yield("<letStatement>")
        
        self._expect(Token(value="let"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_varName():
            yield y
        
        if self._accept(Token(value="[")):
            for y in self.p_expression():
                yield y
            self._expect(Token(value="]"))
        
        self._expect(Token(value="="))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        for y in self.p_expression():
            yield y
        
        self._expect(Token(value=";"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</letStatement>")

    def p_ifStatement(self):
        "ifStatement ::= 'if' '(' expression ')' '{' statements '}'\
                         ('else' '{' statements '}')?"
                         
        yield("<ifStatement>")
        
        self._expect(Token(value="if"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        self._expect(Token(value="("))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_expression():
            yield y
        
        self._expect(Token(value=")"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        self._expect(Token(value="{"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_statements():
            yield y
        
        self._expect(Token(value="}"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        if self._accept(Token(value="else")):
            self._expect(Token(value="{"))
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_statements():
                yield y
            
            self._expect(Token(value="}"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

        yield ("</ifStatement>")
            
    def p_whileStatement(self):
        "whileStatement ::= 'while' '(' expression ')' '{' statements '}'"
        
        yield("<whileStatement>")
        
        self._expect(Token(value="while"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        self._expect(Token(value="("))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_expression():
            yield y
            
        self._expect(Token(value=")"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        self._expect(Token(value="{"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_statements():
            yield y
        
        self._expect(Token(value="}"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</whileStatement>")

        
    def p_doStatement(self):
        "doStatement ::= 'do' subroutineCall ';'"
        
        yield("<doStatement>")
        
        self._expect(Token(value="do"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        for y in self.p_subroutineCall():
            yield y
        
        self._expect(Token(value=";"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</doStatement>")
        
    def p_returnStatement(self):
        "returnStatement ::= 'return' expression? ';'"
        
        yield("<returnStatement>")
        
        self._expect(Token(value="return"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        for y in self.p_expression():
            yield y
            
        self._expect(Token(value=";"))
        yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</returnStatement>")


##### Expressions #####

        
    def p_expression(self):
        "expression ::= term (op term)*"
        
        op = "+", "-", "*", "/", "&", "|", "<", ">", "="
        
        yield("<expression>")
        
        for y in self.p_term():
            yield y
        
        while self._accept(Token(value=op)):
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_term():
                yield y
        
        yield("</expression>") 
            
    
    def p_term(self):
        "term ::= integerConstant | stringConstant | keywordConstant |\
                  varName | varName '[' expression ']' | subroutineCall |\
                  '(' expression ')' | unaryOp term"

        keywordConstant = "true", "false", "null", "this"
 
        unaryOp = "-", "~"
        
        yield("<term>")
        
        if self._accept(Token(type=("integerConstant", "stringConstant"))):
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
        elif self._accept(Token(value=keywordConstant)):
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
        elif self._accept(Token(value=unaryOp)):
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_term():
                yield y
        
        elif self._accept(Token(value="(")):
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_expression():
                yield y
            
            self._expect(Token(value=")"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

        
        elif self.nexttok.type=="identifier":
                
                look = self.tokens[0]
                
                if look.value in (".", "("):
                    
                    # call subroutine
                    
                    for y in self.p_subroutineCall():
                        yield y
                        
                elif look.value == "[":
                    
                    # this is an array
                    
                    self._expect(Token(type="identifier"))
                    yield(tag(tag=self.tok.type, value=self.tok.value))
                    
                    self._expect(Token(value="["))
                    yield(tag(tag=self.tok.type, value=self.tok.value))
                    
                    for y in self.p_expression():
                        yield y
                    
                    self._expect(Token(value="]"))
                    yield(tag(tag=self.tok.type, value=self.tok.value))

                else:
                    
                    # this is a varName
                    self._expect(Token(type="identifier"))
                    yield(tag(tag=self.tok.type, value=self.tok.value))

        yield("</term>")
    
    def p_expressionList(self):
        "expressionList  ::= (expression (',' expression)*)?"
        
        yield("<expressionList>")
        
        for y in self.p_expression():
            yield y
        
        while self._accept(Token(value=",")):
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            for y in self.p_expression():
                yield y
                
        yield("</expressionList>")

    def p_subroutineCall(self):
        "subroutineCall ::= subroutineName '(' expressionList ')' |\
                            (className | varName) '.' subroutineName \
                            '(' expressionList ')'"

        self._expect(Token(type="identifier"))
        yield(tag(tag=self.tok.type, value=self.tok.value))
        
        name = self.tok.value
        
        if self._accept(Token(value="(")):
            yield(tag(tag=self.tok.type, value=self.tok.value))

            for y in self.p_expressionList():
                yield y
            
            self._expect(Token(value=")"))
            yield(tag(tag=self.tok.type, value=self.tok.value))
        
        else:
            self._expect(Token(value="."))
            yield(tag(tag=self.tok.type, value=self.tok.value))
            
            self._expect(Token(type="identifier"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

            self._expect(Token(value="("))
            yield(tag(tag=self.tok.type, value=self.tok.value))

            for y in self.p_expressionList():
                yield y
                
            self._expect(Token(value=")"))
            yield(tag(tag=self.tok.type, value=self.tok.value))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

                    





