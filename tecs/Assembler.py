i#!/usr/bin/python3

import sys
import getopt
import time

myname = "Assembler.py"
suffix = ".hack"


def usage():


    print ("Usage: " + myname + " -i <inputfile> [-o <outputfile>]")
"""
if len(sys.argv) == 1:
    usage()
    sys.exit(1)
"""
"""
def main(argv):
    # TODO make -o optional
    # cleanup command line argument processing

    # Start timer
    ticks = time.time()

    inputfile = ''
    outputfile = ''

    try:

        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':
           usage()
           sys.exit()

        elif opt in ("-i", "--ifile"):
           inputfile = arg
           outputfile = arg.split(".")[0] + suffix

        if opt in ("-o", "--ofile"):
           outputfile = arg

    # Create a new Parser object on the input file

    # TODO actual error handling

    print("Initializing Assembler...\n")

    p = Parser(inputfile)
    o = open(outputfile, "w")

    assembledWords = 0


    print ("Recticulating splines...\n")


# MAIN LOOP

    c = p.advance()

    while c:


        binary = p.assemble(c)

        if binary is None:
            c = p.advance()
            continue

        assembledWords += 1
        o.write(binary)
        c = p.advance()

        if c:
            o.write("\n")


    # Cleanup and report

    print ("Cleaning up...")
    o.close()

    print ("\nAssembled %d words in %f seconds." % (assembledWords, time.time()-ticks))
"""
class Parser:
    'Assembly Parser'

    class command:

        line = ''
        commandType = ''
        text = ''

        dest = ''
        comp = ''
        jump = ''


        def print(self):

            print ("\ncommandType: " + self.commandType)
            print ("text: " + self.text)
            print ("line: " + str(self.line))



    commands = []

    def __init__(self, filename):
        # Initalize the Parser module
        # open the input file/stream and get ready to parse it.
        # Also create symbol table and populate with labels.

        print ("Initializing Parser...")

        self.symbolTable = SymbolTable()

        line = 0
        labelizer = 0

        for i in open(filename).readlines():
            line += 1

            i = i.strip()

            index = i.find("//")

            if index != -1:
                i = i[:index]

            if len(i) is 0 or i.isspace():
                continue

            c = Parser.command()


            c.line = line

            if i.startswith("@"):
                c.commandType = ("A_COMMAND")
                c.text = i.lstrip("@")
                labelizer += 1

            elif i.startswith("(") and i.endswith(")"):
                c.commandType = ("L_COMMAND")
                c.text = i.strip("()")
                self.symbolTable.add(c.text, labelizer)

            else:
                c.commandType = ("C_COMMAND")

                c.text = i

                if i.find("=") != -1:

                    split = i.split("=")
                    c.dest = split[0]
                    c.comp = split[1]

                else:
                    c.dest = None

                if i.find(";") != -1:

                    split = i.split(";")
                    c.comp = split[0]
                    c.jump = split[1]

                else:
                    c.jump = None

                labelizer += 1

            self.commands.append(c)

        self.currentCommand = 0
        print ("Parser initialized. " + str(line + 1) + " lines read.\n")



    def advance(self):

        if self.currentCommand == len(self.commands):
            return False
        else:
            self.currentCommand += 1
            return self.commands[self.currentCommand - 1]



    def assemble(self, command):

            bitstring = ''

            if command.commandType is "C_COMMAND":

                bitstring += "111"

                x = Code.asmComp(command.comp)

                if x is False:
                    print("In command: %s on line %i:" % (command.text, command.line))
                    print("Unrecognized computation %s" % (command.comp))
                    sys.exit(2)
                else:
                    bitstring += x

                x = Code.asmDest(command.dest)
                if x is False:
                    print("In command: %s on line %i:" % (command.text, command.line))
                    print("Unrecognized destination %s" % (command.dest))
                    sys.exit(2)
                else:
                    bitstring += x

                x = Code.asmJump(command.jump)
                if x is False:
                    print("In command: %s on line %i:" % (command.text, command.line))
                    print("Unrecognized jump %s" % (command.jump))
                    sys.exit(2)
                else:
                    bitstring += x

            elif command.commandType is "A_COMMAND":

                bitstring += "0"

                if command.text.isdecimal():
                    bitstring += Code.binary(int(command.text))

                else:

                    i = self.symbolTable.lookup(command.text)

                    if i is False:
                        i = self.symbolTable.getIndex()
                        self.symbolTable.add(command.text)

                    bitstring += Code.binary(i)

            elif command.commandType is "L_COMMAND":
                return None

            return bitstring


class SymbolTable:
    'Create and manage a symbolic table for address and offset calculation.'

# TODO encapsulate access methods

    def __init__(self, index = 16):

        print("Initializing symbol table...")

        self.index = index

        # Load predefined symbols into table

        self.data = {   "SP"     : 0,
                        "LCL"    : 1,
                        "ARG"    : 2,
                        "THIS"   : 3,
                        "THAT"   : 4,
                        "SCREEN" : 16384,    # 0x4000
                        "KBD"    : 24576 }   # 0x6000

        # R0 - R15 = memory locations 0 - 15 respectively.

        for i in range(0,self.index):
            self.data["R" + str(i)] = i


        print("Predefined symbols loaded.")

    def getIndex(self):
        return self.index

    def add(self, symbol, value=False):

        if value:
            self.data[symbol] = value
        else:
            self.data[symbol] = self.index
            self.index += 1

    def lookup(self, symbol):

        if symbol in self.data.keys():
            return self.data[symbol]
        else:
            return False




    def print(self):
        print ("Symbol table:\n")
        for key in self.data.keys():
            print ("%s    ->   %i" % (key, self.data[key]))



class Code:

    def binary(integer, bits=15):
        """Return binary representation of integer
           default range is 0-65535 (15 bits)"""

        return "".join(str((integer >> i) & 1) for i in range(bits - 1, -1, -1))


    def asmDest(dest):
        "Assembles and returns the 3 bit binary code of the dest mnemonic."

        d = 0

        if dest == None:
            return Code.binary(d, bits = 3)


        for letter in dest:
            if letter == "A":
                d = d ^ 4
            elif letter == "D":
                d = d ^ 2
            elif letter == "M":
                d = d ^ 1
            else:
                return False

        return (Code.binary(d, bits = 3))

    def asmComp(comp):
        "Assembles and returns the 7 bit binary code of the comp mnemonic."

        compTable = { "0"   : "101010",
                      "1"   : "111111",
                      "-1"  : "111010",
                      "D"   : "001100",
                      "A"   : "110000",
                      "!D"  : "001101",
                      "!A"  : "110001",
                      "-D"  : "001111",
                      "-A"  : "110011",
                      "D+1" : "011111",
                      "A+1" : "110111",
                      "D-1" : "001110",
                      "A-1" : "110010",
                      "D+A" : "000010",
                      "A+D" : "000010",
                      "D-A" : "010011",
                      "A-D" : "000111",
                      "D&A" : "000000",
                      "D|A" : "010101" }

        instruction = ""

        # Determine if we are addressing the M register or the A
        # register. Set the most significant bit to "1" if we are
        # and "0" otherwise.

        c = comp

        if "M" in comp:
            c = comp.replace("M", "A")
            instruction += "1"
        else:
            instruction += "0"


        if c in compTable.keys():
            instruction = instruction + compTable[c]
        else:
            return False

        return instruction


    def asmJump(jump):
        "Assembles and returns the 3 bit binary code of the jump mnemonic."

        if jump == None:
            return "000"

        jumpTable = { "JGT" : "001",
                      "JEQ" : "010",
                      "JGE" : "011",
                      "JLT" : "100",
                      "JNE" : "101",
                      "JLE" : "110",
                      "JMP" : "111" }

        if jump in jumpTable.keys():
            return jumpTable[jump]
        else:
            return False


"""
if __name__ == "__main__":
   main(sys.argv[1:])
"""
