#!/usr/bin/python3

import sys, getopt, time, os

_myname = "VM.py"
_suffix = ".asm"

def usage():
    print ("Usage: " + _myname + " -i <inputfile> [-y -o <outputfile>]")

if len(sys.argv) == 1:
    usage()
    sys.exit(1)


def main(argv):
    # TODO
    # cleanup command line argument processing

    # Start timer
    ticks = time.time()
            
    inputfile = []
    outputfile = ''

    try:
       opts, args = getopt.getopt(argv,"hyi:o:",["help","ifile=","ofile="])

    except getopt.GetoptError:
       usage()
       sys.exit(2)
       
    for opt, arg in opts:
        
        if opt in ("-h", "--help"):
           usage()
           sys.exit()

        elif opt in ("-i", "--ifile"):

            if os.path.exists(arg):

                if os.path.isfile(arg):
                    
                    inputfile.append(arg)
                    outputfile, extension = os.path.splitext(arg)
                    outputfile = os.path.join(outputfile, _suffix)
                    
                elif os.path.isdir(arg):

                    path, outputfile = os.path.split(os.path.realpath(arg))
                    outputfile = os.path.join(path, outputfile, _suffix)
                    
                    for root, dirs, files in os.walk(arg):
                        
                        for f in files:
                            if os.path.splitext(f)[1] == ".vm":
                                inputfile.append(f)
                        
                    
        if opt in ("-o", "--ofile"):
           outputfile = arg


#    print("Initializing Stack...")
#    w.writeStackInit()

    
    print("Processing...")

    w = CodeWriter(outputfile)

    for f in inputfile:

        w.setFileName(f)

        p = Parser(f)
            
        
        while p.advance():

            a = p.command.split(" ")

            p.command = a[0]
        
            if p.commandType() == "C_PUSH":
                w.writePushPop("C_PUSH", a[1], a[2])
            elif p.commandType() == "C_POP":
                w.writePushPop("C_POP", a[1], a[2])
            elif p.commandType() == "C_ARITHMETIC":
                w.writeArithmetic(a[0])

        
        

    w.close()


    

class Parser:

    

    def __init__(self, filename):
        # Open input file/stream and get ready to parse it.

        print("Initializing Parser for \"" + filename + "\"...")
               
        self.inputlist = open(filename).readlines()
        self.inputlength = len(self.inputlist)

        self.counter = 0

        print ("Parser initialized. " + str(self.inputlength) + " lines read.\n")
 
    
    def advance(self):

        '''Reads the next command from the input and makes it the current command.
         Returns False if end of file is reached.'''

        if self.counter == self.inputlength:
            return False

        self.command = self.inputlist[self.counter].strip()
        self.counter += 1

        # strip off any trailing comments
        # or advance if whole line is a comment.

        index = self.command.find("//")

        if index != -1:
            if index == 0:
                self.advance()
            else:
                self.command = self.command[index:]

        # check if command is just whitespace

        if self.command.strip() == "":
            self.advance()

        return True

    def commandType(self):

        # Returns the type of the current VM command
        # C_ARITHMETIC is returned for all the arithmetic commands.
        #
        # Returns:
        #
        # C_ARITHMETIC
        # C_PUSH
        # C_POP
        # C_LABEL
        # C_GOTO
        # C_IF
        # C_FUNCTION
        # C_RETURN
        # C_CALL

        c = self.command
        
        if c == "push":
            return "C_PUSH"
        elif c == "pop":
            return "C_POP"
        elif (c == "add" or c == "sub" or c == "neg" or c == "eq" or c == "gt" or\
              c == "lt" or c == "and" or c == "or" or c == "not"):
            return "C_ARITHMETIC"
        
        

    def arg1(self):

        # Returns the first argument of the current command.
        # In the case of C_ARITHMETIC, the command itself (add, sub, etc.)
        # is returned.
        # Should not be called if the current command is:
        # C_RETURN.

        

        return

    def arg2(self):

        # Returns the second argument of the current command.
        # Should be called only if the current command is:
        #
        # C_PUSH
        # C_POP
        # C_FUNCTION
        # C_CALL

        return

class CodeWriter:

    def __init__(self, filename):

        # Opens the outfile/stream and gets ready to write into it.

        print("Initializing Code Writer...")

        self.setFileName(filename)
        self.file = open(filename, "w")
        
        self.eqs = 0
        self.lts = 0
        self.gts = 0

        
    def writeStackInit(self):

        code = ["@256",
                "D=A",
                "@SP",
                "M=D"]

        self.writeCode(code)
        
    def setFileName(self, name):

        # Informs the code writer that the translation of the new VM
        # file is started.

        self.name = name

    def writeCode(self, code):

        for i in code:
            self.file.write(i + "\n")

        self.file.write("\n")

        
            
    def writeArithmetic(self, cmd):

        # Writes the assembly code that is the translation of the given arithmetic
        # command

        # add       x + y  (two's compliment)
        # sub       x - y  (two's compliment)
        # neg       -y     (two's compliment)
        # eq        true if x = y, else false
        # gt        true if x > y, else false
        # lt        true if x < y, else false
        # and       x And y (bit-wise)
        # or        x Or y  (bit-wise)
        # not       Not y   (bit-wise)

        #code = ''

        if cmd == "add":

            code = [ "// add",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M+D"]


        elif cmd == "sub":
            
            code = [ "// sub",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M-D"]
              
            
        elif cmd == "neg":

            code = [ "// neg",
                     "@SP",
                     "A=M-1",
                     "M=-M"]


        elif cmd == "eq":

            code = [ "// eq",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "MD=M-D",
                     "M=M-1",
                     "@eq.false." + str(self.eqs),
                     "D;JNE",                     
                     "@eq.done." + str(self.eqs),
                     "0;JMP",
                     "(eq.false." + str(self.eqs) + ")",
                     "@SP",
                     "A=M-1",
                     "M=0",
                     "(eq.done." + str(self.eqs) + ")"]
            self.eqs += 1

        elif cmd == "gt":
            
            code = [ "// gt",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "D=M-D",
                     "@gt.true." + str(self.gts),
                     "D;JGT",
                     "@SP",
                     "A=M-1",
                     "M=0",
                     "@gt.done." + str(self.gts),
                     "0;JMP",
                     "(gt.true." + str(self.gts) + ")",
                     "@SP",
                     "A=M-1",
                     "M=-1",
                     "(gt.done." + str(self.gts) + ")"]
            self.gts += 1

        elif cmd == "lt":
            
            code = [ "// lt",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "D=M-D",
                     "@lt.true." + str(self.lts),
                     "D;JLT",
                     "@SP",
                     "A=M-1",
                     "M=0",
                     "@lt.done." + str(self.lts),
                     "0;JMP",
                     "(lt.true." + str(self.lts) + ")",
                     "@SP",
                     "A=M-1",
                     "M=-1",
                     "(lt.done." + str(self.lts) + ")"]
            self.lts += 1


        elif cmd == "and":

            code = [ "// and",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M&D"]

        elif cmd == "or":

            code = [ "// or",
                     "@SP",
                     "AM=M-1",
                     "D=M",
                     "A=A-1",
                     "M=M|D"]

        elif cmd == "not":

            code = [ "@SP",
                     "A=M-1",
                     "M=!M"]

        
        else:
            code = []
                     
        self.writeCode(code)

            
    def writePushPop(self, cmd, segment, index):

        # Writes the assembly code that is the translation of the given command,
        # where command is either C_PUSH, or C_POP

        if cmd == "C_PUSH":

            if segment == "constant":

                # TODO make sure constant is the right value
                # 15 bit? should be 16 bit.

                code = [ "// push constant " + str(index),
                         "@"+str(index),
                         "D=A",
                         "@SP",
                         "M=M+1",
                         "A=M-1",
                         "M=D"]

            elif segment == "local":
                code = [ "// push local " + str(index),
                         "@" + str(index),
                         "D=A",
                         "@LCL",
                         "A=M+D",
                         "D=M",
                         "@SP",
                         "M=M+1",
                         "A=M-1",
                         "M=D"]

            elif segment == "argument":
                code = [ "// push argument " + str(index),
                         "@" + str(index),
                         "D=A",
                         "@ARG",
                         "A=M+D",
                         "D=M",
                         "@SP",
                         "M=M+1",
                         "A=M-1",
                         "M=D"]

            elif segment == "this":
                code = [ "// push this " + str(index),
                         "@" + str(index),
                         "D=A",
                         "@THIS",
                         "A=M+D",
                         "D=M",
                         "@SP",
                         "M=M+1",
                         "A=M-1",
                         "M=D"]

            elif segment == "that":
                code = [ "// push that " + str(index),
                         "@" + str(index),
                         "D=A",
                         "@THAT",
                         "A=M+D",
                         "D=M",
                         "@SP",
                         "M=M+1",
                         "A=M-1",
                         "M=D"]

                

            elif segment == "pointer":
                # TODO check if index is in [0,1]
                # pointer = location (3 + index (THIS and THAT segments))

                code = [ "//push pointer " + str(index),
                             "@" + str(int(index) + 3),
                             "D=M",
                             "@SP",
                             "M=M+1",
                             "A=M-1",
                             "M=D"]
                
                # TODO throw pointerIndexOutOfBounds exception

            elif segment == "temp":

                # index should be 0 - 7
                # accesses memory segments R5-R12
                # i.e. RAM[5+index]
                
                code = [ "// push temp " + str(index),
                             "@" + str(int(index) + 5),
                             "D=M",
                             "@SP",
                             "M=M+1",
                             "A=M-1",
                             "M=D"]

                # TODO throw tempIndexOutOfBounds exception
                         
            else:

                # TODO throw segmentNotRecognized exception
                code = []


            if (segment != "constant" and segment != "pointer" and segment != "temp"):

                if int(index) == 0:
                    c = [code[0], code[3], "A=M"]
                    for i in code[5:]:
                        c.append(i)
                    code = c
        
                elif int(index) == 1:
                    c = [code[0], code[3], "A=M+1"]
                    for i in code[5:]:
                        c.append(i)
                    code = c
        
                    

        elif cmd == "C_POP":

            if segment == "local":

                    code = [ "// pop local " + str(index),
                             "@SP",
                             "AM=M-1",
                             "D=M",
                             "@LCL",
                             "A=M"]
                
            elif segment == "argument":

                
                    code = [ "// pop argument " + str(index),
                             "@SP",
                             "AM=M-1",
                             "D=M",
                             "@ARG",
                             "A=M"]
                    
        
                
            elif segment == "this":

                
                    code = [ "// pop this " + str(index),
                             "@SP",
                             "AM=M-1",
                             "D=M",
                             "@THIS",
                             "A=M"]

                
            elif segment == "that":

                                        
                    code = [ "// pop that " + str(index),
                             "@SP",
                             "AM=M-1",
                             "D=M",
                             "@THAT",
                             "A=M"]

                   
            elif segment == "pointer":

                # TODO check for index out of bounds
                # should be [0,1]

                code = [ "// pop pointer " + str(index),
                         "@SP",
                         "AM=M-1",
                         "D=M",
                         "@R3"]


            elif segment == "temp":

                # TODO check for index out of bounds
                # should be [0-7]

                code = [ "// pop temp " + str(index),
                         "@SP",
                         "AM=M-1",
                         "D=M",
                         "@R5"]

                
            else:
                # TODO throw segmentNotRecognized error
                code = []

        
            for i in range(0, int(index)):
                code.append("A=A+1")
            code.append("M=D")

        self.writeCode(code)
                

    def close(self):

        # Close output stream
        self.file.close()
        
if __name__ == "__main__":
   main(sys.argv[1:])
