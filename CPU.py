class CPU:
    def __init__(self, program=None, RAM=None):
        
        # Initialize RAM - use provided RAM or create new one
        if RAM is not None:
            self.RAM = RAM
        else:
            self.RAM = []
        
        # Load the passed program into the ROM and reset the CPU
        self.reset()
        
        if program:
            self.ROM = program

    def __str__(self):
        return ({"A": self.A, "D": self.D, "zr": self.zr, "ng": self.ng})

    def reset(self):
        # Initialize memory and registers

        self.zr = 0
        self.ng = 0
        self.A = 0
        self.D = 0
        self.KBD = 0

        # Initialize RAM if it's empty or ensure it has the right size
        if len(self.RAM) == 0:
            self.RAM = [0] * 24576
        elif len(self.RAM) < 24576:
            # Extend RAM to required size
            self.RAM.extend([0] * (24576 - len(self.RAM)))

    def step(self, PC):

        command = self.ROM[PC]

        if command["TYPE"] == "A_COMMAND":
            self.A = command["VAL"]

        elif command["TYPE"] == "C_COMMAND":

            dest = command["VAL"]["DEST"]
            comp = command["VAL"]["COMP"]
            jump = command["VAL"]["JUMP"]

            if 'M' in comp:
                result = self.ALU[comp.replace("M", "A")](self.RAM[self.A], self.D)
            else:
                result = self.ALU[comp](self.A, self.D)

            self.zr = 0
            self.ng = 0

            if result == 0:
                self.zr = 1
            elif result < 0:
                self.ng = 1

            if 'M' in dest:
                self.RAM[self.A] = result
            if 'A' in dest:
                self.A = result
            if 'D' in dest:
                self.D = result

            if jump == "":
                return PC+1
            else:
                if jump == "JGT":
                    if result > 0:
                        return self.A
                elif jump == "JEQ":
                    if result == 0:
                        return self.A
                elif jump == "JGE":
                    if result >= 0:
                        return self.A
                elif jump == "JLT":
                    if result < 0:
                        return self.A
                elif jump == "JNE":
                    if result != 0:
                        return self.A
                elif jump == "JLE":
                    if result <= 0:
                        return self.A
                elif jump == "JMP":
                    return self.A

        return PC+1

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
