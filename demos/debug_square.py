#!/usr/bin/env python3
"""Debug script to trace memory operations in the Petri net."""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser

# Hack memory map
SCREEN_BASE = 16384
SCREEN_END = 24575
KBD_ADDR = 24576


class DebugMemory:
    """Debug memory that traces all operations."""
    
    def __init__(self):
        self.ram = [0] * 32768
        self.read_count = 0
        self.write_count = 0
        self.screen_writes = 0
        
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
        """Memory read callback."""
        self.read_count += 1
        if 0 <= addr < len(self.ram):
            return self.ram[addr]
        return 0
    
    def write(self, addr, value):
        """Memory write callback."""
        self.write_count += 1
        value = value & 0xFFFF
        
        if SCREEN_BASE <= addr <= SCREEN_END:
            self.screen_writes += 1
        
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value


def main():
    print("=" * 70)
    print("  Debug: Square Petri Net Execution")
    print("=" * 70)
    print()
    
    memory = DebugMemory()
    
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    
    temp_dir = tempfile.mkdtemp(prefix="debug_")
    
    try:
        for f in os.listdir(project_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(project_dir, f), temp_dir)
        
        print("  Compiling Jack to VM...")
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        os_files = ['Sys.vm', 'Memory.vm', 'Screen.vm', 'Keyboard.vm', 
                    'Math.vm', 'Output.vm', 'String.vm', 'Array.vm']
        for f in os_files:
            src = os.path.join(os_dir, f)
            if os.path.exists(src):
                shutil.copy(src, temp_dir)
        
        print("  Building Petri net with memory callbacks...")
        parser = VMParser(
            temp_dir,
            memory_read_callback=memory.read,
            memory_write_callback=memory.write
        )
        net = parser.emitter.net
        
        print(f"  Places: {len(net.places)}")
        print(f"  Transitions: {len(net.transitions)}")
        print()
        
        # Initialize the enabled set for event-driven execution
        net.initialize_enabled_set()
        
        print("  Executing Petri net...")
        for step in range(2000000):
            if step % 200000 == 0:
                print(f"  Step {step}... (screen_writes={memory.screen_writes})")
            
            fired = net.execute_step_single()
            if not fired:
                print(f"\n  Step {step}: No enabled transitions")
                break
        
        print()
        print(f"  Total reads: {memory.read_count}")
        print(f"  Total writes: {memory.write_count}")
        print(f"  Screen writes: {memory.screen_writes}")
        
    finally:
        shutil.rmtree(temp_dir)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
