#!/usr/bin/env python3
"""Debug Screen.drawRectangle loop."""

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
        self.screen_writes = 0
        
        self.ram[0] = 256   # SP
        self.ram[1] = 300   # LCL
        self.ram[2] = 400   # ARG
        self.ram[3] = 3000  # THIS
        self.ram[4] = 3010  # THAT
        self.ram[2048] = 14334
        self.ram[2049] = 2050
    
    def read(self, addr):
        if 0 <= addr < len(self.ram):
            return self.ram[addr]
        return 0
    
    def write(self, addr, value):
        value = value & 0xFFFF
        if 16384 <= addr <= 24575:
            self.screen_writes += 1
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value

def main():
    memory = DebugMemory()
    
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    temp_dir = tempfile.mkdtemp(prefix="debug_")
    
    try:
        for f in os.listdir(project_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(project_dir, f), temp_dir)
        
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        os_files = ['Sys.vm', 'Memory.vm', 'Screen.vm', 'Keyboard.vm', 
                    'Math.vm', 'Output.vm', 'String.vm', 'Array.vm']
        for f in os_files:
            src = os.path.join(os_dir, f)
            if os.path.exists(src):
                shutil.copy(src, temp_dir)
        
        parser = VMParser(temp_dir, memory_read_callback=memory.read, memory_write_callback=memory.write)
        net = parser.emitter.net
        net.initialize_enabled_set()
        
        # Trace ifgoto operations
        for name, trans in list(net.transitions.items()):
            if 'ifgoto_' in name and 'WHILE_END' in name:
                original_op = trans.operation
                def make_traced_ifgoto(orig, tname):
                    def traced_ifgoto(tokens):
                        result = orig(tokens)
                        if memory.screen_writes > 0 and memory.screen_writes <= 20:
                            condition = 0
                            for t in tokens:
                                if hasattr(t, 'value') and isinstance(t.value, int):
                                    condition = t.value
                            print(f"  {tname}: condition={condition}, result[0]={result[0]}, result[1]={result[1]}")
                        return result
                    return traced_ifgoto
                trans.operation = make_traced_ifgoto(original_op, name)
        
        print("Running...")
        for step in range(2000000):
            fired = net.execute_step_single()
            if memory.screen_writes >= 100:
                break
        
        print(f"Steps: {step}, Screen writes: {memory.screen_writes}")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
