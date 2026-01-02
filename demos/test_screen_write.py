#!/usr/bin/env python3
"""
Test screen writes by directly executing Screen.drawRectangle
"""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser

# Hack memory map
SCREEN_BASE = 16384
SCREEN_END = 24575


class TestMemory:
    """Test memory with screen write tracking."""
    
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
        
        # Initialize Screen.color to -1 (black)
        self.ram[16] = -1 & 0xFFFF  # Screen.color static variable
    
    def read(self, addr):
        if 0 <= addr < len(self.ram):
            return self.ram[addr]
        return 0
    
    def write(self, addr, value):
        value = value & 0xFFFF
        if SCREEN_BASE <= addr <= SCREEN_END:
            self.screen_writes.append((addr, value))
            print(f"  SCREEN WRITE [{addr}] = {value:016b}")
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value


def main():
    print("=" * 70)
    print("  Test: Direct Screen Write")
    print("=" * 70)
    print()
    
    memory = TestMemory()
    
    # Create a minimal VM program that draws a horizontal line
    # This simulates what Screen.drawHorizontal does
    vm_code = """
// Simple screen write test
// Write to screen address 16384 (first word of screen)
function Test.main 0
push constant 16384
push constant 65535
call Memory.poke 2
pop temp 0
push constant 0
return

// Memory.poke implementation
function Memory.poke 0
push argument 0
push argument 1
pop temp 0
pop pointer 1
push temp 0
pop that 0
push constant 0
return
"""
    
    temp_dir = tempfile.mkdtemp(prefix="test_screen_")
    
    try:
        # Write VM code
        with open(os.path.join(temp_dir, "Test.vm"), "w") as f:
            f.write(vm_code)
        
        print("  Building Petri net...")
        parser = VMParser(
            temp_dir,
            memory_read_callback=memory.read,
            memory_write_callback=memory.write
        )
        net = parser.emitter.net
        
        print(f"  Places: {len(net.places)}")
        print(f"  Transitions: {len(net.transitions)}")
        print()
        
        # Execute
        print("  Executing...")
        for step in range(100):
            enabled = [t for t in net.transitions.values() if t.can_fire()]
            if not enabled:
                print(f"  Step {step}: No enabled transitions")
                break
            
            t = enabled[0]
            print(f"  Step {step}: {t.name}")
            t.fire()
        
        print()
        print(f"  Screen writes: {len(memory.screen_writes)}")
        for addr, val in memory.screen_writes:
            print(f"    [{addr}] = {val}")
        
    finally:
        shutil.rmtree(temp_dir)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
