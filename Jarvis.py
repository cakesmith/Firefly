#!/usr/bin/python3

# This code is due for a major tuneup.

from tkinter import Tk, Frame, PhotoImage, Label, BOTH
from os import system
from collections import namedtuple

import re, types, itertools, threading, time

debug = True
debugKBD = True

"""
******A_COMMAND******
0 v v v  v v v v   v v v v   v v v v

where v is 0 or 1
*********************

******C_COMMAND******
1 1 1 a   c1 c2 c3 c4   c5 c6 d1 d2   d3 j1 j2 j3

(Dest=)Comp(;Jump)

*********************
"""

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

jumpTable = { "JGT" : "001",
              "JEQ" : "010",
              "JGE" : "011",
              "JLT" : "100",
              "JNE" : "101",
              "JLE" : "110",
              "JMP" : "111" }

def clean(line):

    """Strips out comments to the end of the input string
     and also removes whitespace at the beginning and end of the string.

     Returns: cleaned string"""

    line = line.split("//")[0].strip()

    if len(line) is 0 or line.isspace():
        return None
    else:
        return line

def make_symboltable(program):

    linenum = 0

    symbolTable = { "SP"     : 0,
                    "LCL"    : 1,
                    "ARG"    : 2,
                    "THIS"   : 3,
                    "THAT"   : 4,
                    "SCREEN" : 16384,    # 0x4000
                    "KBD"    : 24576 }   # 0x6000

    for i in range(16):
        symbolTable["R" + str(i)] = i
        
    for line in program:

        line = clean(line)

        if line:
            line = line.upper()
        elif line == None:
            continue

        if line.startswith("(") and line.endswith(")"):
            symbolTable[line.strip("()")] = linenum
            continue

        linenum += 1

    return symbolTable

def parse(program, nextRAM = 16, maxRAM = 16383, A_bits = 15):
    """Builds a symbol table and parses a full program before assembly."""

    
    symbols = make_symboltable(program)

    linenum = 0

    for line in program:

        linenum += 1

        line = clean(line)
        
        if line:
            line = line.upper()
        elif line == None:
            continue


        if line.startswith("@"):

            ########## A_COMMAND ###########
            val = line.lstrip("@")

            if val.isdecimal():
                yield {"LINE": linenum, "TYPE": "A_COMMAND", "VAL": int(val)}
            elif val in symbols.keys():
                yield {"LINE": linenum, "TYPE": "A_COMMAND", "VAL": symbols[val]}
            else:

                if nextRAM >= maxRAM:

                    raise ParseError("on line %i: Symbol Table out of bounds\nnextRAM(%i) >= maxRAM(%i)" % (linenum, nextRAM, maxRAM))

                else:

                    symbols[val] = nextRAM

                    yield {"LINE": linenum, "TYPE": "A_COMMAND", "VAL": nextRAM}

                    nextRAM += 1

        elif line.startswith("(") and line.endswith(")"):
            ########### L_COMMAND ###########
            pass

        else:
            ########### C_COMMAND ###########

            comp = line

            if line.find("=") != -1:

                dest, comp = line.split("=")
                
            else:
                dest = ""

            if line.find(";") != -1:

                comp, jump = line.split(";")
                
            else:
                jump = ""

            yield {"LINE": linenum, "TYPE": "C_COMMAND", "VAL": {"DEST": dest, "COMP": comp, "JUMP":jump}}

def disassemble(bitstring):

    for i in bitstring:
        try:
            if not (i == '0' or i == '1'):
                raise Exception
        except Exception as e:
            raise BitstringError(e)

    if bitstring[0] == '0':
        return {"TYPE": "A_COMMAND", "VAL": bin2int(bitstring[1:])}

    elif bitstring[0:3] == "111":

        M_bit = bitstring[3]
        comp_bits = bitstring[4:10]
        dest_bits = bitstring[10:13]
        jump_bits = bitstring[13:16]

        comp = ''
        dest = ''
        jump = ''

        for i in compTable.keys():
            if comp_bits == compTable[i]:
                comp = i

        if comp == '':
            raise DisassembleError("Unknown COMP: %s" %comp_bits)

        for i in jumpTable.keys():
            if jump_bits == jumpTable[i]:
                jump = i

        dest = "".join(itertools.compress(list("ADM"), map(bin2int, list(dest_bits))))


        return {"TYPE": "C_COMMAND", "VAL": {"DEST": dest, "COMP": comp, "JUMP": jump}}

def assemble(command, linenum=0, bits=15):
    """Assembles a parsed command

    bits is the number of bits to assemble the A_COMMAND into

    Returns => bitstring"""

    bitstring = ''
    try:
        linenum = command["LINE"]
    except:
        linenum = 0

    cmdType = command["TYPE"]
    val = command["VAL"]

    if cmdType == "A_COMMAND":

        bitstring += '0'

        if val <= 2**bits - 1:
            bitstring += binary(val, bits)
        else:
            raise AssembleError("on line: %i value too large for A_COMMAND: %i" % (linenum, val))

    elif cmdType == "C_COMMAND":

        header_bin = "111"
        M_bin = '0'
        comp_bin = "000000"
        dest_bin = "000"
        jump_bin = "000"


        # Unpack command arguments
        dest, comp, jump = (val["DEST"], val["COMP"], val["JUMP"])



        # Determine and assemble the comp portion of the command

        if 'M' in comp:
            M_bin = '1'
            comp = comp.replace('M', 'A')

        try:
            compTable[comp]
        except Exception as e:
            raise CompError("on line %i: Invalid COMP value: \"%s\"" % (linenum, comp))

        comp_bin = compTable[comp]

        # Determine the destination of the command

        d = 0

        if dest:

            for letter in dest:
                if letter == "A":
                    d = d ^ 4
                elif letter == "D":
                    d = d ^ 2
                elif letter == "M":
                    d = d ^ 1
                else:
                    raise DestError("on line %i: Invalid DEST value: \"%s\"" % (linenum, dest))

            dest_bin = binary(d, bits=3)

        # Determine and assemble the jump portion of the command

        if jump:

            try:
                jumpTable[jump]
            except Exception as e:
                raise JumpError("on line %i: invalid JUMP value: \"%s\"" % (linenum, jump))

            jump_bin = jumpTable[jump]

        bitstring = header_bin + M_bin + comp_bin + dest_bin + jump_bin

    else:

        raise CommandError("on line %i: invalid command: \"%s\"" % (linenum, val))

    return bitstring

def binary(integer, bits=15):
        """Return string representation of binary integer value
           default length is 15 bits for A_COMMAND"""

        return "".join(str((integer >> i) & 1) for i in range(bits - 1, -1, -1))

def bin2int(X):
    """return integer representation of bitstring"""

    for i in X:
        try:
            if not (i == '0' or i == '1'):
                raise Exception
        except Exception as e:
            raise BitstringError(e)

    # I had to throw in at least one line of unpythonic functional trickery:

    return sum(map(lambda x,y: int(x)*y, reversed(X), map(lambda i: 2**i, range(len(X)))))


####### Error Classes #########

class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

class StepError(Error):
    """Exception raised when PC is greater than ROM length."""
    pass

class AssembleError(Error):
    """Exception raised when attempting to load a value in A Register that is too large."""
    pass

class DisassembleError(Error):
    pass

class ParseError(Error):
    """Exception raised for errors in parse_program"""
    pass

class CommandError(Error):
    """Base class for all invalid commands"""
    pass

class CompError(CommandError):
    """Exception raised when comp field is invalid"""
    pass

class JumpError(CommandError):
    pass

class DestError(CommandError):
    pass

class BitstringError(Error):
    pass

class IndexOutOfBoundsError(Error):
    pass


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stopflag = threading.Event()

    def stop(self):
        self._stopflag.set()

    def stopped(self):
        return self._stopflag.isSet()

class IO:
    
    def __init__(self, thread):
         
       # set up screen, width = 512, height = 256

        self.mythread = thread
        self.screen = Tk()
        self.screen.title("Jarvis Simulator")
        self.screen.geometry("512x256+1600+500")
        self.screen.wm_maxsize(width=512, height=256)
        self.screen.wm_minsize(width=512, height=256)
        self.screen.wm_resizable(width=False, height=False)

        self.image = PhotoImage(width = 512, height = 256)

        self.label = Label(self.screen, image=self.image)

        self.label.grid()

        # set up keyboard

        for c in self.Keycodes.keys():
            exec("self.screen.bind(\"<%s>\", self.%s)" % (c, c))

        self.screen.bind("<Any-KeyPress>", self.KeyPressed)
        self.screen.bind("<Any-KeyRelease>", self.KeyReleased)

        system("xset r off")
        self.screen.protocol("WM_DELETE_WINDOW", self.delete_callback)

    def delete_callback(self):
        system("xset r on")
        self.mythread.stop()
        self.screen.destroy()
        
        
        
    KBD = 0
    
    Keycodes = { "Return"     : 128,
                 "BackSpace"  : 129,
                 "Left"       : 130,
                 "Up"         : 131,
                 "Right"      : 132,
                 "Down"       : 133,
                 "Home"       : 134,
                 "End"        : 135,
                 "Prior"      : 136,
                 "Next"       : 137,
                 "Insert"     : 138,
                 "Delete"     : 139,
                 "Escape"     : 140 }

    for i in range(1,13):
        k = { "F" + str(i) : 140+i }
        Keycodes.update(k)

    for key in Keycodes.keys():
        code = Keycodes[key]

        exec("""def %s(self, event):
                    self.KBD = %s
                    if debugKBD:
                        print(%s)""" % (key, code, code))

    def KeyPressed(self, event):

        if event.char:
            self.KBD = ord(event.char)
            if debugKBD:
                print(str(ord(event.char)))

    def KeyReleased(self, event):

        self.KBD = 0

        if debugKBD:
            print("Key Released.\n")


    def drawFill(self, color):

        horizontal_line = "{" + " ".join([color]*self.image.width()) + "}"
        self.image.put(" ".join([horizontal_line] * self.image.height()))

    def drawPoint(self, x, y, color):

        #~ print("Drawing %s point at (%i, %i)" % (color, x, y))

        self.image.put(color, (x, y))

    def drawmem(self, location, value):

        (y, x) = divmod(location,32)

        x = x * 16

        memword = binary(value, bits=16)
        
        for i in range(0, 16):
            if memword[15-i] == '1':
                self.drawPoint(x+i, y, "green")
            else:
                self.drawPoint(x+i, y, "black")
                
                


class CPU:

    ALU = { "0"   : lambda a,d: 0,
            "1"   : lambda a,d: 1,
            "-1"  : lambda a,d: -1,
            "D"   : lambda a,d: d,
            "A"   : lambda a,d: a,
            "!D"  : lambda a,d: ~d,
            "!A"  : lambda a,d: ~a,
            "-D"  : lambda a,d: -d,
            "-A"  : lambda a,d: -a,
            "D+1" : lambda a,d: d+1,
            "A+1" : lambda a,d: a+1,
            "D-1" : lambda a,d: d-1,
            "A-1" : lambda a,d: a-1,
            "D+A" : lambda a,d: a+d,
            "A+D" : lambda a,d: a+d,
            "D-A" : lambda a,d: d-a,
            "A-D" : lambda a,d: a-d,
            "D&A" : lambda a,d: a&d,
            "A&D" : lambda a,d: a&d,
            "D|A" : lambda a,d: a|d,
            "A|D" : lambda a,d: a|d }




    def __init__(self, program=None):

        self.mythread = StoppableThread(target = self._run)
        self.IO = IO(self.mythread)
        
        # Load the passed program into the ROM and reset the CPU
        
        self.reset()
        
        if program:
            self.ROM = program

    def __str__(self):
        return ({"PC":self.PC, "A":self.A, "D":self.D, "zr":self.zr, "ng": self.ng})

    def reset(self):
        # Initialize memory and registers

        self.PC = 0
        self.zr = 0
        self.ng = 0
        self.A = 0
        self.D = 0
        self.KBD = 0
        
        self.RAM = []

        for i in range(24576):
            self.RAM.append(0)

        # reset screen

        self.IO.drawFill("black")

    def start(self):
                
        self.ticks = float(time.time())
        self.hz = 0
        self.iterations = 1

        self.mythread.start()

    def _run(self):


        while self.mythread.stopped() == False:

            self.step()

            self.hz = (self.iterations / (time.time() - self.ticks))


            #~ print("Iterations: %i Hz: %i" % (self.iterations, self.hz))

            self.iterations += 1

 
    def step(self):

        command = self.ROM[self.PC]


        if command["TYPE"] == "A_COMMAND":

            self.A = command["VAL"]
            self.PC += 1

        elif command["TYPE"] == "C_COMMAND":

            dest = command["VAL"]["DEST"]
            comp = command["VAL"]["COMP"]
            jump = command["VAL"]["JUMP"]


            if 'M' in comp:

                if self.A == 24576:
                    result = self.ALU[comp.replace("M", "A")](self.IO.KBD, self.D)
                else:

                    result = self.ALU[comp.replace("M", "A")](self.RAM[self.A], self.D)

            else:
                result = self.ALU[comp](self.A, self.D)


            self.zr = 0
            self.ng = 0

            if result == 0:
                self.zr = 1
            elif result < 0:
                self.ng = 1

            if jump == "":
                self.PC += 1
            else:

                if jump == "JGT":
                    if result > 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JEQ":
                    if result == 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JGE":
                    if result >= 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JLT":
                    if result < 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JNE":
                    if result != 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JLE":
                    if result <= 0:
                        self.PC = self.A
                    else:
                        self.PC += 1
                elif jump == "JMP":
                    self.PC = self.A
                else:
                    self.PC += 1


            if 'M' in dest:

                if self.A >= 16384 and self.A < 24576:

                    if result != self.RAM[self.A]:
                        self.IO.drawmem(location = self.A - 16384, value = result)
                        
            
                self.RAM[self.A] = result

            if 'A' in dest:
                self.A = result

            if 'D' in dest:
                self.D = result






t = []

inputfile = "OS/OS.asm"

#~ inputfile = "projects/11/Average/Average.asm"
#~ inputfile = "projects/06/pong/Pong.asm"

for i in open(inputfile).readlines():
    t.append(i)

rom = []

for i in parse(t):
    rom.append(i)
    
#~ inputfile.close()



c = CPU(rom)
c.IO.screen.after(1000, c.start())

try:
    c.IO.screen.mainloop()
finally:
    c.mythread.stop()
    print("Total iterations: %i" % c.iterations)
    print("Average Hz: %i" % c.hz)

#####
