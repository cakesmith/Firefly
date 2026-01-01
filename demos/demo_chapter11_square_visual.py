#!/usr/bin/env python3
"""
Chapter 11 Square Game Visual Simulation
========================================
Interactive visual simulation of the Square game with:
- Pygame window showing 512x256 pixel screen (scaled 2x)
- Keyboard input mapped to Hack key codes
- Real-time screen memory visualization

Controls:
- Arrow keys: Move square
- Z: Decrease size
- X: Increase size  
- Q: Quit

This simulates the Square game logic with visual I/O,
demonstrating how the Petri net would execute with
keyboard input tokens and screen output.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pygame
except ImportError:
    print("pygame not installed. Run: pip install pygame")
    sys.exit(1)

# Hack screen dimensions
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256
SCALE = 2  # Display scale factor

# Hack key codes
KEY_MAP = {
    pygame.K_q: 81,
    pygame.K_z: 90,
    pygame.K_x: 88,
    pygame.K_UP: 131,
    pygame.K_DOWN: 133,
    pygame.K_LEFT: 130,
    pygame.K_RIGHT: 132,
}


class HackScreen:
    """Simulated Hack screen memory (512x256 pixels)."""
    
    def __init__(self):
        # Use a 2D array for simplicity
        self.pixels = [[False] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]
        self.color = True  # True = black, False = white
    
    def set_color(self, color: bool):
        """Set drawing color."""
        self.color = color
    
    def draw_pixel(self, x: int, y: int):
        """Draw a single pixel."""
        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
            self.pixels[y][x] = self.color
    
    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int):
        """Draw a filled rectangle."""
        x1, x2 = max(0, min(x1, x2)), min(SCREEN_WIDTH - 1, max(x1, x2))
        y1, y2 = max(0, min(y1, y2)), min(SCREEN_HEIGHT - 1, max(y1, y2))
        
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.pixels[y][x] = self.color
    
    def clear(self):
        """Clear the screen."""
        self.pixels = [[False] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]


class SquareSimulator:
    """Simulates the Square game logic."""
    
    def __init__(self, screen: HackScreen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.size = 30
        self.direction = 0  # 0=none, 1=up, 2=down, 3=left, 4=right
        self.running = True
        self.draw()
    
    def draw(self):
        """Draw the square."""
        self.screen.set_color(True)
        self.screen.draw_rectangle(self.x, self.y, 
                                   self.x + self.size, self.y + self.size)
    
    def erase(self):
        """Erase the square."""
        self.screen.set_color(False)
        self.screen.draw_rectangle(self.x, self.y,
                                   self.x + self.size, self.y + self.size)
    
    def move_up(self):
        if self.y > 1:
            self.screen.set_color(False)
            self.screen.draw_rectangle(self.x, (self.y + self.size) - 1,
                                       self.x + self.size, self.y + self.size)
            self.y -= 2
            self.screen.set_color(True)
            self.screen.draw_rectangle(self.x, self.y, self.x + self.size, self.y + 1)
    
    def move_down(self):
        if (self.y + self.size) < 254:
            self.screen.set_color(False)
            self.screen.draw_rectangle(self.x, self.y, self.x + self.size, self.y + 1)
            self.y += 2
            self.screen.set_color(True)
            self.screen.draw_rectangle(self.x, (self.y + self.size) - 1,
                                       self.x + self.size, self.y + self.size)
    
    def move_left(self):
        if self.x > 1:
            self.screen.set_color(False)
            self.screen.draw_rectangle((self.x + self.size) - 1, self.y,
                                       self.x + self.size, self.y + self.size)
            self.x -= 2
            self.screen.set_color(True)
            self.screen.draw_rectangle(self.x, self.y, self.x + 1, self.y + self.size)
    
    def move_right(self):
        if (self.x + self.size) < 510:
            self.screen.set_color(False)
            self.screen.draw_rectangle(self.x, self.y, self.x + 1, self.y + self.size)
            self.x += 2
            self.screen.set_color(True)
            self.screen.draw_rectangle((self.x + self.size) - 1, self.y,
                                       self.x + self.size, self.y + self.size)
    
    def inc_size(self):
        if ((self.y + self.size) < 254) and ((self.x + self.size) < 510):
            self.erase()
            self.size += 2
            self.draw()
    
    def dec_size(self):
        if self.size > 2:
            self.erase()
            self.size -= 2
            self.draw()
    
    def move_square(self):
        """Move based on current direction."""
        if self.direction == 1:
            self.move_up()
        elif self.direction == 2:
            self.move_down()
        elif self.direction == 3:
            self.move_left()
        elif self.direction == 4:
            self.move_right()
    
    def handle_key(self, key_code: int):
        """Handle key press (creates input token)."""
        if key_code == 81:  # Q - quit
            self.running = False
        elif key_code == 90:  # Z - decrease size
            self.dec_size()
        elif key_code == 88:  # X - increase size
            self.inc_size()
        elif key_code == 131:  # Up
            self.direction = 1
        elif key_code == 133:  # Down
            self.direction = 2
        elif key_code == 130:  # Left
            self.direction = 3
        elif key_code == 132:  # Right
            self.direction = 4
    
    def handle_key_release(self):
        """Handle key release."""
        self.direction = 0


def render_screen(surface, screen: HackScreen):
    """Render HackScreen to pygame surface."""
    surface.fill((255, 255, 255))  # White background
    
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if screen.pixels[y][x]:
                pygame.draw.rect(surface, (0, 0, 0),
                               (x * SCALE, y * SCALE, SCALE, SCALE))


def main():
    print("=" * 60)
    print("  Chapter 11: Square Game Visual Simulation")
    print("=" * 60)
    print()
    print("  Controls:")
    print("    Arrow keys - Move the square")
    print("    Z - Decrease size")
    print("    X - Increase size")
    print("    Q - Quit")
    print()
    print("  Starting visual simulation...")
    
    pygame.init()
    pygame.display.set_caption("Hack Square Game - Petri Net Simulation")
    
    # Create display
    display = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE + 40))
    font = pygame.font.Font(None, 24)
    
    # Create screen and simulator
    screen = HackScreen()
    simulator = SquareSimulator(screen)
    
    clock = pygame.time.Clock()
    current_key = 0
    
    while simulator.running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulator.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    current_key = KEY_MAP[event.key]
                    simulator.handle_key(current_key)
            elif event.type == pygame.KEYUP:
                if event.key in KEY_MAP:
                    current_key = 0
                    simulator.handle_key_release()
        
        # Move square
        simulator.move_square()
        
        # Render
        render_screen(display, screen)
        
        # Draw status bar
        pygame.draw.rect(display, (200, 200, 200), 
                        (0, SCREEN_HEIGHT * SCALE, SCREEN_WIDTH * SCALE, 40))
        
        status = f"Pos: ({simulator.x}, {simulator.y})  Size: {simulator.size}  "
        status += f"Dir: {['None', 'Up', 'Down', 'Left', 'Right'][simulator.direction]}  "
        status += f"Key: {current_key if current_key else 'None'}"
        
        text = font.render(status, True, (0, 0, 0))
        display.blit(text, (10, SCREEN_HEIGHT * SCALE + 10))
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    print("  Simulation ended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
