import os
from collections import namedtuple
from datetime import datetime
from functools import wraps, partial

from Toolkit.LabelGenerator import LabelGenerator
from Toolkit.LookAhead import LookAhead
from Toolkit.functions import flatten, scanpattern, safewrite, loctoline

class vmcommand(namedtuple('vmcommand', ('command', 'segment', 'index', 'loc'))):
    def __new__(cls, command, segment=None, index=None, loc=None):
        return super(vmcommand, cls).__new__(cls, command, segment, index, loc)
        
class VMTranslator:

    def __init__(self, programdir, input_extension=".vm", output_extension=".asm", bootstrap=True, debug=True, overwrite=False):
        
        self.countlines = 0
        
        self.debug = debug
        
        dirname = os.path.dirname(programdir)

        _, self.progname = os.path.split(dirname)
    
        outputfilename = os.path.join(dirname, self.progname)  + output_extension
                   
        if not (overwrite or not os.path.exists(outputfilename)):
            raise Exception("File %s already exists" % outputfilename)
                    
        with open(outputfilename, "wt") as outputfile:
            
            
            safewrite(self.bootstrap(), outputfile)
            safewrite(self.header(), outputfile)

            
            inputfilenames = [os.path.join(programdir, name) for name in os.listdir(programdir) if name.endswith(input_extension)]
            
            for inputfile, self.filename, self.classname in [(open(f), f, os.path.basename(os.path.splitext(f)[0])) for f in inputfilenames]:
                
                try:
                    for line in self.translate(inputfile.read()):
                        safewrite(line, outputfile)
                        
                except Exception as exc:
                    args = exc.args
                    
                    if not args:
                        arg0 = ''
                    else:
                        arg0 = args[0]
                    
                    if isinstance(arg0, str):                    
                        arg0 += "\nIn file: { %s } " % self.filename
    
                    exc.args = flatten((arg0, args[1:]))
                    raise
                    
        print ("lines: %d" % self.countlines)
        
    def header(self, bootstrap=True):
        
        header = [ "// ***",
                   "// " + self.progname,
                   "// compiled on " + datetime.strftime(datetime.now(), '%A %B %d, %Y'),
                   "// ***",
                   "// Begin hardcode",
                   "// ***",
                   
                   "//",
                   "(call)",
                   "//",
           
                   "@SP",
                   "M=M+1",
                   "A=M-1",
                   "M=D",
                
                   "@LCL",
                   "D=M",
                   "@SP",
                   "M=M+1",
                   "A=M-1",
                   "M=D",
                  
                   "@ARG",
                   "D=M",
                   "@SP",
                   "M=M+1",
                   "A=M-1",
                   "M=D",
                
                   "@THIS",
                   "D=M",
                   "@SP",
                   "M=M+1",
                   "A=M-1",
                   "M=D",
                    
                   "@THAT",
                   "D=M",
                   "@SP",
                   "M=M+1",
                   "A=M-1",
                   "M=D",
                   
                   "@R14",
                   "D=M",
                   "@5",
                   "D=D+A",
                   "@SP",
                   "D=M-D",
                   "@ARG",
                   "M=D",
                   
                
                   "@SP",
                   "D=M",
                   "@LCL",
                   "M=D",
                
                   "@R15",      # functionAddress
                   "A=M",
                   "0;JMP",
                 
                   "//",
                   "(return)",
                   "//",
                 
                   "@LCL",
                   "D=M",
                   "@R15",
                   "M=D",
                 
                   "@5",
                   "A=D-A",
                   "D=M",
                   "@R14",
                   "M=D",
                
                   "@SP",
                   "A=M-1",
                   "D=M",
                   "@ARG",
                   "A=M",
                   "M=D",
                 
                   "D=A+1",
                   "@SP",
                   "M=D",
                 
                   "@R15",
                   "AM=M-1",
                   "D=M",
                   "@THAT",
                   "M=D",
                 
                   "@R15",
                   "AM=M-1",
                   "D=M",
                   "@THIS",
                   "M=D",
                 
                   "@R15",
                   "AM=M-1",
                   "D=M",
                   "@ARG",
                   "M=D",
                 
                   "@R15",
                   "AM=M-1",
                   "D=M",
                   "@LCL",
                   "M=D",
                 
                   "@R14",
                   "A=M",
                   "0;JMP",
                   
                   "//",
                   "(lt)",
                   "//",
                    
                   "@SP",
                   "AM=M-1",
                   "D=M",
                   "A=A-1",
                   "D=M-D",
                   "M=0",
                   "@LT.TRUE",
                   "D;JLT",
                   "@SP",
                   "A=M-1",
                   "M=1",
                   "(LT.TRUE)",
                   "@SP",
                   "A=M-1",
                   "M=M-1",
                   "@R14",
                   "A=M",
                   "0;JMP",
                   
                   "//",
                   "(gt)",
                   "//",
       
                   "@SP",
                   "AM=M-1",
                   "D=M",
                   "A=A-1",
                   "D=M-D",
                   "M=0",
                   "@GT.TRUE",
                   "D;JGT",
                   "@SP",
                   "A=M-1",
                   "M=1",
                   "(GT.TRUE)",
                   "@SP",
                   "A=M-1",
                   "M=M-1",
                   "@R14",
                   "A=M",
                   "0;JMP",
                     
                   "//",
                   "(eq)",
                   "//",
                   
                   "@SP",
                   "AM=M-1",
                   "D=M",
                   "A=A-1",
                   "D=M-D",
                   "M=0",
                   "@EQ.TRUE",
                   "D;JEQ",
                   "@SP",
                   "A=M-1",
                   "M=1",
                   "(EQ.TRUE)",
                   "@SP",
                   "A=M-1",
                   "M=M-1",
                   "@R14",
                   "A=M",
                   "0;JMP"]
                   
                 
        return header
        
    def _tokenize(text):
        
        zeroargs = "add", "sub", "neg", "lt", "eq", "gt", "and", "or", "not", "return"
        onearg   = "label", "goto", "if-goto"
        twoargs  = "function", "call", "push", "pop"
        
        allcommands = flatten((zeroargs, onearg, twoargs))
        
        line_comment    = r"(?P<line_comment>//.*\n)"
        block_comment   = r"(?P<block_comment>\/\*[^*]*\*+([^/][^*]*\*+)*\/)"
        whitespace      = r"(?P<whitespace>\s+)"
        identifier      = r"(?P<identifier>[^\s]+)"
        
        master_pat = "|".join((line_comment, block_comment, identifier, whitespace))
        
        ignore_types = "line_comment", "block_comment", "whitespace"
        
        # use a generator comprehension to pull matches one at a time.
        
        matches = ((scanmatch.value, scanmatch.loc) for scanmatch in scanpattern(master_pat, text, ignore_types))
        
        for token, loc in matches:
            
            if token in zeroargs:
                yield vmcommand(command=token, loc=loc)
                next
                
            elif token in onearg:
                command = token
                try:
                    segment, _ = next(matches)
                    if segment in allcommands:
                        raise Exception("\"%s\" expects one argument on line %d" % (command, loctoline(text)(loc)))
                except StopIteration:
                    raise Exception("Unexpected end of file on line %d" % loctoline(text)(loc))
                yield vmcommand(command, segment, loc=loc)
                
            elif token in twoargs:
                command = token
                try:
                    segment, _ = next(matches)
                    index, _ = next(matches)
                    
                    #~ print("{%s} {%s} {%s}" % (command, segment, index))
                    
                    if (segment in allcommands) or (index in allcommands):
                        raise Exception("\"%s\" expects two arguments on line %d" % (command, loctoline(text)(loc)))
                        
                except StopIteration:
                    raise Exception("Unexpected end of file on line %d" % loctoline(text)(loc))
                
                if index.isdigit():
                    yield vmcommand(command, segment, int(index), loc)
                else:
                    raise Exception("expected int on line %d: %s" % (loctoline(text)(loc), index))
            
            else:
                raise Exception("Unknown command %s on line %d" % (token, loctoline(text)(loc)))
                
    def translate(self, text):
        
        arithcommands = [ "add", "sub", "neg", "lt", "eq", "gt", "and", "or", "not" ]
        
        self.line = loctoline(text)

        commands = LookAhead(VMTranslator._tokenize(text))

        def process(command):
    
            command = vmc.command
                
            if command == "if-goto":
                return self.ifgoto(vmc)
                    
            elif command == "return":
                return self.ret()
                    
            elif command in arithcommands:
                return self.arithmetic(vmc)
                    
            else:
                func = eval("self." + command)
            return func(vmc)
            
        for vmc in commands:
            
            
                
            command = vmc
            nextcommand = None
            
            code = process(vmc)
            
            # iterable strings *grumble*
            
            if isinstance(code, str):
                yield code
            else:

                for y in code:
                    yield y
                
    def bootstrap(self):
        
        code = [ "@256",
                 "D=A",
                 "@SP",
                 "M=D",
                 "@Sys.init",
                 "0;JMP"]
        
        if self.debug:
            code = ["// Bootstrap code"] + code
        
        return code

    def move(self, a, b):

        segment = b.segment
        index = b.index
        
        segments = { "local"    : "@LCL", 
                     "argument" : "@ARG",
                     "this"     : "@THIS",
                     "that"     : "@THAT"}
        
        if segment in segments:
            

            code = self.moveD(a)
            code += [ segments[segment],
                      "A=M"]
                      
            for i in range(index):
                code += ["A=A+1"]
                
            code += ["M=D"]
            
               
        elif segment == "pointer":

            if index == 0:
                code = [ "@THIS",
                         "M=D"]
                         
            elif index == 1:
                code = [ "@THAT",
                         "M=D"]
            else:
                raise Exception("invalid pointer segment: %s on line %d"\
                % (segment, self.line(vmc.loc)))
                


        elif segment == "temp":

            if index in range(8):
                
                code = self.moveD(a)
                code += [ "@R" + str(5+index),
                          "M=D"]
            else:
                raise Exception("temp index %d out of range (0-7) on line %d"\
                                 % (index, self.line(vmc.loc)))
                
        elif segment == "static":
            code = self.moveD(a)
            code +=  [ "@" + ".".join((self.classname, "static", str(index))),
                       "M=D"]
            
        else:
            raise Exception("unrecognized segment %s on line %d"\
            % (b.segment, self.line(b.loc)))
            
        if self.debug:
            code =["// move " + a.segment + " " + str(a.index) + " => " + b.segment + " " + str(b.index)] + code
        
        return code
        
    def label(self, vmc):
        if vmc.segment.startswith(self.funcname):
            label = vmc.segment
        else:
            label = ".".join((self.funcname, vmc.segment))
        return "(" + label + ")"
        
    def goto(self, vmc):
        
        label = self.label(vmc).strip("()")
        
        code = [ "@" + label,
                 "0;JMP"]
                
        if self.debug:
            code = ["// goto " + label] + code
        
        return code
            
    def ifgoto(self, vmc):
        
        label = self.label(vmc).strip("()")
        
        code = [ "@SP",
                 "AM=M-1",
                 "D=M",
                 "@" + label,
                 "D;JNE"]
                
        if self.debug:
            code = ["// if-goto " + label] + code
                
        return code
                
    def function(self, vmc):
        
        self.funcname = vmc.segment
        nLocals = vmc.index
        
        # set the class labeling function to use the current functionName

        self.labels = LabelGenerator(self.funcname)
        
        # process a vm label command to create a function entry point
        
        code =  ["(" + self.funcname + ")"]
 
        for k in range(nLocals):
            
            code += [ "@SP",
                      "AM=M+1",
                      "A=A-1",
                      "M=0"]
        if self.debug:
                
            code = ["// function " + self.funcname + " nLocals: " + str(nLocals)] + code
            
        return code
            
    def call(self, vmc):
        """ call f n (calling a function f after n arguments have been
            pushed on the stack)
            
                push return-address // (using the label declared below)
                push LCL            // save LCL of calling function
                push ARG            // save ARG of calling function
                push THIS           // save THIS of calling function
                push THAT           // save THAT of calling function
                ARG = SP-n-5        // n = number of arguments
                LCL = SP            // reposition LCL
                goto f              // transfer control
            (return-address)
        """
        functionName = vmc.segment
        nArgs = vmc.index
        
        returnAddress = self.labels.next("call")
        
        code = [ 
                 "@" + str(nArgs),
                 "D=A",
                 "@R14",
                 "M=D",
                 "@" + functionName,
                 "D=A",
                 "@R15",
                 "M=D",
                 "@" + returnAddress,
                 "D=A",
                 "@call",
                 "0;JMP",
                 "(" + returnAddress + ")"]
                 
            
        if self.debug:
            code = ["// call " + functionName + " nArgs: " + str(nArgs)] + code
        
        return code
            
    def ret(self):
        """ return (from a function)
        
                
                FRAME = LCL         // FRAME is a temporary variable
                RETURN = *(FRAME-5) // save Return address in temp variable
                *ARG = pop()        // reposition the return value for the caller
                SP = ARG+1          // restore SP of the caller
                THAT = *(FRAME-1)   // restore THAT of the caller
                THIS = *(FRAME-2)   // restore THIS of the caller
                ARG = *(FRAME-3)    // restore ARG of the caller
                LCL = *(FRAME-4)    // restore LCL of the caller
                goto RETURN     // goto return-address (in the caller's code)
        """
        code = ["@return",
                "0;JMP"]

                 
        if self.debug:
            code = ["// return"] + code
        
        return code

    def arithmetic(self, vmc):
        """Writes the assembly code that is the 
           translation of the given arithmetic
           command

         add       x + y  (two's compliment)
         sub       x - y  (two's compliment)
         neg       -y     (two's compliment)
         eq        true if x = y, else false
         gt        true if x > y, else false
         lt        true if x < y, else false
         and       x And y (bit-wise)
         or        x Or y  (bit-wise)
         not       Not y   (bit-wise)
        """
        cmd = vmc.command
        
        compares =  ["eq", "lt", "gt"]
        
        if cmd in compares:
            
            label = self.labels.next(cmd)
            
            code = [ "@" + label,
                     "D=A",
                     "@R14",
                     "M=D",
                     "@" + cmd,
                     "0;JMP",
                     "(" + label + ")"]
        
        elif cmd == "add":

            code = [ "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M+D"]

        elif cmd == "sub":
            
            code = [ "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M-D"]
            
        elif cmd == "neg":

            code = [ "@SP",
                     "A=M-1",
                     "M=-M"]

        elif cmd == "and":

            code = [ "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M&D"]
                     
        elif cmd == "or":

            code = [ "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M|D"]

        elif cmd == "not":

            code = [ "@SP",
                     "A=M-1",
                     "M=!M"]

        else:
            raise Exception("unknown arithmetic cmd %s on line %d"\
            % (cmd, self.loctoline(vmc.loc)))
                     
        if self.debug:
            code = ["// " + cmd] + code
        
        return code

    def moveD(self, vmc):
        
        # puts a value in the D register
        
        segment = vmc.segment
        index = vmc.index
        
        segments = { "local"    : "@LCL", 
                     "argument" : "@ARG",
                     "this"     : "@THIS",
                     "that"     : "@THAT"}
                     
        if segment == "constant":

            code =  [ "@"+str(index),
                      "D=A"]
        
        elif segment in segments.keys():

            code = [ "@" + str(index),
                     "D=A",
                     segments[segment],
                     "A=M+D",
                     "D=M"]

        elif segment == "pointer":
            if index in (0,1):
                # pointer = location (3 + index)

                code = [ "@" + str(index + 3),
                         "D=M"]
            else:
                raise Exception("pointer index %d out of bounds (0,1) on line %d"\
                % (index, self.loctoline(vmc.loc)))
            

        elif segment == "temp":

            # index should be 0 - 7
            # accesses memory segments R5-R12
            # i.e. RAM[5+index]
            
            code = [ "@" + str(index + 5),
                     "D=M"]
                     
        elif segment == "static":
            code = [ "@" + ".".join((self.classname, "static", str(index))),
                     "D=M"]
                     
        else:
            line = self.line(vmc.loc)
            
            raise Exception("unrecognized segment %s on line %d"\
            % (segment, line))
        
        return code
        
    def push(self, vmc):
        
        segment = vmc.segment
        index = vmc.index
        
        stackPush = [ "@SP",
                      "M=M+1",
                      "A=M-1",
                      "M=D"]
              
        code = self.moveD(vmc) + stackPush
        
        if self.debug:
            code = ["// push " + segment + " " + str(index)] + code
        
        return code
        
    def pop(self, vmc):
        
        stackPop = [ "@SP",
                     "AM=M-1",
                     "D=M" ]
                     
        segment = vmc.segment
        index = vmc.index
        
        segments = { "local"    : "@LCL", 
                     "argument" : "@ARG",
                     "this"     : "@THIS",
                     "that"     : "@THAT"}
        
        if segment in segments:
            
            code = [ stackPop,
                     segments[segment],
                     "A=M"]

            for i in range(index):
                code += ["A=A+1"]
            
            code += ["M=D"]

               
        elif segment == "pointer":

            if index == 0:
                code = [ stackPop,
                         "@THIS",
                         "M=D"]
                         
            elif index == 1:
                code = [ stackPop,
                         "@THAT",
                         "M=D"]
            else:
                raise Exception("invalid pointer segment: %s on line %d"\
                % (segment, self.line(vmc.loc)))
                


        elif segment == "temp":
            
            if index in range(8):
                code = [ stackPop,
                         "@R" + str(5+index),
                         "M=D"]
            else:
                raise Exception("temp index %d out of range (0-7) on line %d"\
                                 % (index, self.line(vmc.loc)))
                
        elif segment == "static":
            code =  [ stackPop,
                      "@" + ".".join((self.classname, "static", str(index))),
                      "M=D"]
            
        else:
            raise Exception("unrecognized segment %s on line %d"\
            % (segment, self.line(vmc.loc)))
            
        if self.debug:
            code =["// pop " + segment + " " + str(index)] + code
        
        return code

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
