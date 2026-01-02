#!/usr/bin/env python3
"""Debug function call argument passing."""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser

SCREEN_BASE = 16384

class DebugMemory:
    def __init__(self):
        self.ram = [0] * 32768
        self.call_log = []
        
        # Initialize pointers
        self.ram[0] = 256   # SP
        self.ram[1] = 300   # LCL
        self.ram[2] = 400   # ARG
        self.ram[3] = 3000  # THIS
        self.ram[4] = 3010  # THAT
        
        # Initialize heap
        self.ram[2048] = 14334
        self.ram[2049] = 2050
    
    def read(self, addr):
        if 0 <= addr < len(self.ram):
            return self.ram[addr]
        return 0
    
    def write(self, addr, value):
        value = value & 0xFFFF
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value

def main():
    print("=" * 70)
    print("  Debug Call Arguments")
    print("=" * 70)
    
    memory = DebugMemory()
    
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    temp_dir = tempfile.mkdtemp(prefix="debug_")
    
    try:
        for f in os.listdir(project_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(project_dir, f), temp_dir)
        
        print("  Compiling...")
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        os_files = ['Sys.vm', 'Memory.vm', 'Screen.vm', 'Keyboard.vm', 
                    'Math.vm', 'Output.vm', 'String.vm', 'Array.vm']
        for f in os_files:
            src = os.path.join(os_dir, f)
            if os.path.exists(src):
                shutil.copy(src, temp_dir)
        
        print("  Building Petri net...")
        parser = VMParser(temp_dir, memory_read_callback=memory.read, memory_write_callback=memory.write)
        net = parser.emitter.net
        emitter = parser.emitter
        
        # Patch call operations to log arguments
        original_calls = {}
        for name, trans in net.transitions.items():
            if name.startswith("call_Screen.updateLocation"):
                original_op = trans.operation
                def make_logged_op(orig, tname):
                    def logged_op(tokens):
                        arg_values = []
                        for t in tokens:
                            if hasattr(t, 'value'):
                                val = t.value
                                if isinstance(val, int):
                                    arg_values.append(val)
                        print(f"  {tname}: args={arg_values}")
                        # Also print ARG pointer and what's at ARG
                        arg_ptr = memory.ram[2]
                        print(f"    ARG={arg_ptr}, ARG[0]={memory.ram[arg_ptr]}, ARG[1]={memory.ram[arg_ptr+1]}")
                        return orig(tokens)
                    return logged_op
                trans.operation = make_logged_op(original_op, name)
        
        net.initialize_enabled_set()
        
        print(f"\n  Running until Screen.updateLocation is called...\n")
        
        steps = 0
        while steps < 2000000:
            fired = net.execute_step_single()
            steps += 1
            if fired and any("Screen.updateLocation" in t.name for t in fired):
                break
            if steps % 500000 == 0:
                print(f"  Step {steps}...")
        
        print(f"\n  Steps: {steps}")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
