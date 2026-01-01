class CPU:
    def __init__(self, cpu_id=0, RAM=None):
        
        self.cpu_id = cpu_id  # Unique identifier for this CPU core
        
        # Initialize shared RAM - use provided RAM or create new one
        if RAM is not None:
            self.RAM = RAM
        else:
            self.RAM = []
        
        # Reset the CPU state
        self.reset()

    def __str__(self):
        return str({"CPU": self.cpu_id, "A": self.A, "D": self.D, "zr": self.zr, "ng": self.ng})

    def reset(self):
        # Initialize registers
        self.zr = 0
        self.ng = 0
        self.A = 0
        self.D = 0
        self.KBD = 0
        self.PC = 0  # Program counter

        # Initialize RAM if it's empty or ensure it has the right size
        if len(self.RAM) == 0:
            self.RAM = [0] * 24576
        elif len(self.RAM) < 24576:
            # Extend RAM to required size
            self.RAM.extend([0] * (24576 - len(self.RAM)))

    def get_pc(self):
        """Get the current program counter value."""
        return self.PC
    
    def set_pc(self, value):
        """Set the program counter to a specific value."""
        self.PC = value

    def step(self, instruction):
        """
        Execute one instruction and update PC.
        
        Args:
            instruction: Single instruction dictionary to execute
            
        Returns:
            Dictionary with execution result
        """
        result = self.execute_instruction(instruction)
        
        # Update PC based on result
        if result['should_jump']:
            self.PC = result['jump_target']
        else:
            self.PC += 1
        
        return result

    def execute_instruction(self, instruction):
        """
        Execute one instruction without managing PC.
        PC management is handled externally by the multi-core controller.
        
        Args:
            instruction: Single instruction dictionary to execute
            
        Returns:
            Dictionary with execution result and any jump target
        """
        
        result = {
            'jump_target': None,
            'should_jump': False,
            'result_value': None
        }
        
        if instruction["TYPE"] == "A_COMMAND":
            self.A = instruction["VAL"]
            result['result_value'] = self.A

        elif instruction["TYPE"] == "C_COMMAND":

            dest = instruction["VAL"]["DEST"]
            comp = instruction["VAL"]["COMP"]
            jump = instruction["VAL"]["JUMP"]

            if 'M' in comp:
                comp_result = self.ALU[comp.replace("M", "A")](self.RAM[self.A], self.D)
            else:
                comp_result = self.ALU[comp](self.A, self.D)

            self.zr = 0
            self.ng = 0

            if comp_result == 0:
                self.zr = 1
            elif comp_result < 0:
                self.ng = 1

            # Store results in destinations
            if 'M' in dest:
                self.RAM[self.A] = comp_result
            if 'A' in dest:
                self.A = comp_result
            if 'D' in dest:
                self.D = comp_result

            result['result_value'] = comp_result

            # Handle jumps - return jump information instead of modifying PC
            if jump != "":
                should_jump = False
                
                if jump == "JGT" and comp_result > 0:
                    should_jump = True
                elif jump == "JEQ" and comp_result == 0:
                    should_jump = True
                elif jump == "JGE" and comp_result >= 0:
                    should_jump = True
                elif jump == "JLT" and comp_result < 0:
                    should_jump = True
                elif jump == "JNE" and comp_result != 0:
                    should_jump = True
                elif jump == "JLE" and comp_result <= 0:
                    should_jump = True
                elif jump == "JMP":
                    should_jump = True
                
                if should_jump:
                    result['should_jump'] = True
                    result['jump_target'] = self.A

        return result

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
