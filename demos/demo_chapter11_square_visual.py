#!/usr/bin/env python3
"""
Chapter 11 Square Game - Petri Net with Memory-Mapped I/O
=========================================================
Compiles Square Jack program to VM, builds Petri net with
memory callbacks, and executes with real-time screen display.

Architecture:
- Memory callbacks hook into PetriEmitter
- Screen writes (16384-24575) update display buffer
- Keyboard reads (24576) return current key
- Display mirrors screen RAM in real-time
"""

import sys
import os
import tempfile
import shutil
import threading

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pygame
except ImportError:
    print("pygame not installed. Run: pip install pygame")
    sys.exit(1)

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser

# Hack memory map
SCREEN_BASE = 16384
SCREEN_END = 24575
KBD_ADDR = 24576
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256
SCALE = 2

# Hack key codes
KEY_MAP = {
    pygame.K_q: 81, pygame.K_z: 90, pygame.K_x: 88,
    pygame.K_UP: 131, pygame.K_DOWN: 133,
    pygame.K_LEFT: 130, pygame.K_RIGHT: 132,
}


class SharedMemory:
    """Shared memory with screen and keyboard I/O."""
    
    def __init__(self):
        self.ram = [0] * 32768
        self.screen = [0] * 8192  # Screen buffer (16384-24575)
        self.keyboard = 0
        self.lock = threading.Lock()
        
        # Initialize pointers
        self.ram[0] = 256   # SP
        self.ram[1] = 300   # LCL
        self.ram[2] = 400   # ARG
        self.ram[3] = 3000  # THIS
        self.ram[4] = 3010  # THAT
        
        # Initialize heap
        self.ram[2048] = 14334
        self.ram[2049] = 2050
        
        # Stats
        self.screen_writes = 0
        self.screen_reads = 0
        self.keyboard_reads = 0
        self.total_writes = 0
    
    def read(self, addr):
        """Memory read callback - called by Petri net transitions."""
        with self.lock:
            if addr == KBD_ADDR:
                self.keyboard_reads += 1
                return self.keyboard
            elif SCREEN_BASE <= addr <= SCREEN_END:
                self.screen_reads += 1
                return self.screen[addr - SCREEN_BASE]
            elif 0 <= addr < len(self.ram):
                return self.ram[addr]
            return 0
    
    def write(self, addr, value):
        """Memory write callback - called by Petri net transitions."""
        with self.lock:
            self.total_writes += 1
            value = value & 0xFFFF
            if SCREEN_BASE <= addr <= SCREEN_END:
                self.screen[addr - SCREEN_BASE] = value
                self.screen_writes += 1
            elif 0 <= addr < len(self.ram):
                self.ram[addr] = value
    
    def set_keyboard(self, key):
        with self.lock:
            self.keyboard = key
    
    def get_screen_word(self, offset):
        with self.lock:
            return self.screen[offset] if 0 <= offset < 8192 else 0


def compile_with_io(memory: SharedMemory):
    """Compile Square and build Petri net with memory callbacks."""
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"Project not found: {project_dir}")
    
    temp_dir = tempfile.mkdtemp(prefix="square_")
    
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
        
        return net, temp_dir, parser.emitter
        
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e


class PetriExecutor:
    """Executes Petri net in background thread."""
    
    def __init__(self, net):
        self.net = net
        self.running = False
        self.cycles = 0
        self.fired_total = 0
        self.thread = None
    
    def execute_step(self):
        enabled = [t for t in self.net.transitions.values() if t.can_fire()]
        for t in enabled:
            t.fire()
            self.fired_total += 1
        self.cycles += 1
        return len(enabled)
    
    def run_loop(self):
        import time
        while self.running:
            fired = self.execute_step()
            if fired == 0:
                time.sleep(0.001)
    
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run_loop, daemon=True)
        self.thread.start()
    
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)


def render_screen(surface, memory: SharedMemory):
    """Render screen memory to pygame surface."""
    surface.fill((255, 255, 255))
    
    for y in range(SCREEN_HEIGHT):
        for word_idx in range(32):
            word = memory.get_screen_word(y * 32 + word_idx)
            if word == 0:
                continue
            for bit in range(16):
                if word & (1 << bit):
                    x = word_idx * 16 + bit
                    pygame.draw.rect(surface, (0, 0, 0),
                                   (x * SCALE, y * SCALE, SCALE, SCALE))


def main():
    print("=" * 70)
    print("  Chapter 11: Square - Petri Net with Memory-Mapped I/O")
    print("=" * 70)
    print()
    
    # Create shared memory with I/O callbacks
    memory = SharedMemory()
    
    # Compile with memory callbacks hooked in
    try:
        net, temp_dir, emitter = compile_with_io(memory)
    except Exception as e:
        print(f"  [ERROR] {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # Create executor
    executor = PetriExecutor(net)
    
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Square - Petri Net (Memory-Mapped I/O)")
    
    display = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE + 60))
    font = pygame.font.Font(None, 22)
    clock = pygame.time.Clock()
    
    running = True
    current_key = 0
    
    # Start Petri execution
    executor.start()
    print()
    print("  Petri net executing with memory callbacks")
    print("  Controls: Arrows=Move, Z/X=Size, Q=Quit")
    print()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in KEY_MAP:
                    current_key = KEY_MAP[event.key]
                    memory.set_keyboard(current_key)
                    if current_key == 81:
                        running = False
            elif event.type == pygame.KEYUP:
                if event.key in KEY_MAP:
                    current_key = 0
                    memory.set_keyboard(0)
        
        # Render screen from memory
        render_screen(display, memory)
        
        # Status bar
        pygame.draw.rect(display, (220, 220, 220),
                        (0, SCREEN_HEIGHT * SCALE, SCREEN_WIDTH * SCALE, 60))
        
        s1 = f"Cycles:{executor.cycles}  Fired:{executor.fired_total}  Key:{current_key or '-'}"
        s2 = f"ScreenWrites:{memory.screen_writes}  KbdReads:{memory.keyboard_reads}"
        
        display.blit(font.render(s1, True, (0, 0, 0)), (10, SCREEN_HEIGHT * SCALE + 8))
        display.blit(font.render(s2, True, (0, 0, 100)), (10, SCREEN_HEIGHT * SCALE + 32))
        
        pygame.display.flip()
        clock.tick(60)
    
    executor.stop()
    pygame.quit()
    shutil.rmtree(temp_dir)
    
    print(f"  Done. Cycles:{executor.cycles} Fired:{executor.fired_total}")
    print(f"  Total writes: {memory.total_writes}")
    print(f"  Screen writes: {memory.screen_writes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
