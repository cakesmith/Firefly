#!/usr/bin/env python3
"""Debug frame allocation."""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser

class DebugMemory:
    def __init__(self):
        self.ram = [0] * 32768
        self.writes = []
        
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
    print("  Debug Frame Allocation")
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
        net.initialize_enabled_set()
        
        print(f"\n  Initial: SP={memory.ram[0]} LCL={memory.ram[1]} ARG={memory.ram[2]}")
        print(f"\n  Running 1000 steps...\n")
        
        call_counts = {}
        for step in range(2000000):
            fired = net.execute_step_single()
            if fired:
                for t in fired:
                    tname = t.name if hasattr(t, 'name') else str(t)
                    if 'call_' in tname:
                        func = tname.split('call_')[1].split('_')[0]
                        call_counts[func] = call_counts.get(func, 0) + 1
                    if 'call_Square.new' in tname:
                        arg_ptr = memory.ram[2]
                        args = [memory.ram[arg_ptr + i] for i in range(3)]
                        print(f"  Step {step}: Square.new({args})")
                        print(f"    ARG={arg_ptr}")
                    if 'pop_this_' in tname:
                        this_ptr = memory.ram[3]
                        this_vals = [memory.ram[this_ptr + i] for i in range(4)]
                        print(f"  Step {step}: {tname}")
                        print(f"    THIS={this_ptr}, this[0..3]={this_vals}")
                    if 'call_Screen.drawRectangle' in tname:
                        arg_ptr = memory.ram[2]
                        args = [memory.ram[arg_ptr + i] for i in range(4)]
                        this_ptr = memory.ram[3]
                        this_vals = [memory.ram[this_ptr + i] for i in range(4)]
                        print(f"  Step {step}: Screen.drawRectangle({args})")
                        print(f"    ARG={arg_ptr}, THIS={this_ptr}, this[0..3]={this_vals}")
                    if 'call_Square.draw' in tname:
                        this_ptr = memory.ram[3]
                        this_vals = [memory.ram[this_ptr + i] for i in range(4)]
                        print(f"  Step {step}: Square.draw()")
                        print(f"    THIS={this_ptr}, this[0..3]={this_vals}")
            if step % 500000 == 0 and step > 0:
                print(f"  Step {step}...")
        
        print(f"\n  Function calls (top 15):")
        for func, count in sorted(call_counts.items(), key=lambda x: -x[1])[:15]:
            print(f"    {func}: {count}")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
