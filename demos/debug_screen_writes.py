#!/usr/bin/env python3
"""Debug screen writes to find corruption issue."""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser

SCREEN_BASE = 16384
SCREEN_END = 24575

class DebugMemory:
    def __init__(self):
        self.ram = [0] * 32768
        self.screen_writes = []
        
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
        if SCREEN_BASE <= addr <= SCREEN_END:
            offset = addr - SCREEN_BASE
            row = offset // 32
            col = offset % 32
            self.screen_writes.append((row, col, value))
            if len(self.screen_writes) <= 20:
                print(f"  SCREEN row={row:3d} col={col:2d} val={value:016b}")
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value

def main():
    print("=" * 70)
    print("  Debug Screen Writes")
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
        
        print(f"\n  Running until screen writes stabilize...\n")
        
        steps = 0
        while len(memory.screen_writes) < 1000 and steps < 2000000:
            net.execute_step_single()
            steps += 1
        
        print(f"\n  Steps: {steps}")
        print(f"  Total screen writes: {len(memory.screen_writes)}")
        
        # Analyze
        rows = set(w[0] for w in memory.screen_writes)
        cols = set(w[1] for w in memory.screen_writes)
        print(f"  Unique rows: {len(rows)} -> {sorted(rows)}")
        print(f"  Unique cols: {cols}")
            
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
