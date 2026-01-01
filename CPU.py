class CPU:
    def __init__(self, cpu_id=0, RAM=None):
        
        self.cpu_id = cpu_id  # Unique identifier for this CPU core
        
        # Initialize RAM - use provided RAM or create new one
        if RAM is not None:
            self.RAM = RAM
        else:
            self.RAM = []
        
        # Each CPU has its own PC register for shared ROM execution
        self.PC = 0
        
        # Reset the CPU state
        self.reset()

    def __str__(self):
        return str({"CPU": self.cpu_id, "PC": self.PC, "A": self.A, "D": self.D, "zr": self.zr, "ng": self.ng})

    def reset(self):
        # Initialize memory and registers

        self.zr = 0
        self.ng = 0
        self.A = 0
        self.D = 0
        self.KBD = 0
        self.PC = 0  # Reset program counter

        # Initialize RAM if it's empty or ensure it has the right size
        if len(self.RAM) == 0:
            self.RAM = [0] * 24576
        elif len(self.RAM) < 24576:
            # Extend RAM to required size
            self.RAM.extend([0] * (24576 - len(self.RAM)))

    def step(self, instruction):
        """
        Execute one instruction.
        
        Args:
            instruction: Single instruction dictionary to execute
            
        Returns:
            New PC value after instruction execution
        """
        
        if instruction["TYPE"] == "A_COMMAND":
            self.A = instruction["VAL"]

        elif instruction["TYPE"] == "C_COMMAND":

            dest = instruction["VAL"]["DEST"]
            comp = instruction["VAL"]["COMP"]
            jump = instruction["VAL"]["JUMP"]

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
                self.PC += 1
                return self.PC
            else:
                if jump == "JGT":
                    if result > 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JEQ":
                    if result == 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JGE":
                    if result >= 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JLT":
                    if result < 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JNE":
                    if result != 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JLE":
                    if result <= 0:
                        self.PC = self.A
                        return self.PC
                elif jump == "JMP":
                    self.PC = self.A
                    return self.PC

        self.PC += 1
        return self.PC
    
    def set_pc(self, address):
        """Set the program counter to a specific address"""
        self.PC = address
    
    def get_pc(self):
        """Get the current program counter value"""
        return self.PC

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
