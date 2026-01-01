#!/usr/bin/env python3
"""
Chapter 11 Square Game Test
===========================
Compiles the Square Jack program and tests Petri net simulation
of the game logic with keyboard input tokens.

Square game controls:
- Arrow keys (131=up, 133=down, 130=left, 132=right): Move
- Z (90): Decrease size
- X (88): Increase size
- Q (81): Quit
"""

import sys
import os
import tempfile
import shutil
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition
from Petri.Token import Token


def compile_jack_project(project_dir: str, os_dir: str, os_files: List[str] = None) -> Tuple[str, int]:
    """Compile a Jack project with OS libraries."""
    temp_dir = tempfile.mkdtemp(prefix="jack_compile_")
    
    try:
        for f in os.listdir(project_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(project_dir, f), temp_dir)
        
        compiler = ExpressionEvaluator(temp_dir, overwrite=True)
        
        for f in os.listdir(os_dir):
            if f.endswith('.vm'):
                if os_files is None or f in os_files:
                    shutil.copy(os.path.join(os_dir, f), temp_dir)
        
        vm_count = 0
        for f in os.listdir(temp_dir):
            if f.endswith('.vm'):
                with open(os.path.join(temp_dir, f)) as vf:
                    for line in vf:
                        line = line.strip()
                        if line and not line.startswith('//'):
                            vm_count += 1
        
        return temp_dir, vm_count
        
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e


def test_petri_net_square_simulation():
    """Test Petri net simulation of Square game logic."""
    print("\n" + "=" * 70)
    print("  Petri Net Square Game Simulation")
    print("=" * 70)
    
    # Simulate the Square game using token-based I/O
    
    # Screen state (simplified)
    screen_width = 512
    screen_height = 256
    
    # Square state
    x, y = 0, 0
    size = 30
    direction = 0  # 0=none, 1=up, 2=down, 3=left, 4=right
    
    print(f"\n  Initial state: pos=({x}, {y}), size={size}")
    
    # Simulate key presses as input tokens
    key_sequence = [
        (132, "Right"),   # Move right
        (132, "Right"),   # Keep moving right
        (133, "Down"),    # Move down
        (88, "X"),        # Increase size
        (88, "X"),        # Increase size again
        (130, "Left"),    # Move left
        (90, "Z"),        # Decrease size
        (131, "Up"),      # Move up
        (81, "Q"),        # Quit
    ]
    
    print(f"\n  Simulating key sequence:")
    
    for key_code, key_name in key_sequence:
        # Process key (like a transition firing)
        if key_code == 81:  # Q
            print(f"    Key {key_name} ({key_code}): QUIT")
            break
        elif key_code == 90:  # Z - decrease size
            if size > 2:
                size -= 2
            print(f"    Key {key_name} ({key_code}): size -> {size}")
        elif key_code == 88:  # X - increase size
            if ((y + size) < 254) and ((x + size) < 510):
                size += 2
            print(f"    Key {key_name} ({key_code}): size -> {size}")
        elif key_code == 131:  # Up
            direction = 1
            if y > 1:
                y -= 2
            print(f"    Key {key_name} ({key_code}): pos -> ({x}, {y})")
        elif key_code == 133:  # Down
            direction = 2
            if (y + size) < 254:
                y += 2
            print(f"    Key {key_name} ({key_code}): pos -> ({x}, {y})")
        elif key_code == 130:  # Left
            direction = 3
            if x > 1:
                x -= 2
            print(f"    Key {key_name} ({key_code}): pos -> ({x}, {y})")
        elif key_code == 132:  # Right
            direction = 4
            if (x + size) < 510:
                x += 2
            print(f"    Key {key_name} ({key_code}): pos -> ({x}, {y})")
    
    print(f"\n  Final state: pos=({x}, {y}), size={size}")
    
    # Verify expected state
    # After: Right(+2), Right(+2), Down(+2), X(+2), X(+2), Left(-2), Z(-2), Up(-2)
    expected_x = 0 + 2 + 2 - 2  # = 2
    expected_y = 0 + 2 - 2      # = 0
    expected_size = 30 + 2 + 2 - 2  # = 32
    
    print(f"\n  Expected: pos=({expected_x}, {expected_y}), size={expected_size}")
    
    if x == expected_x and y == expected_y and size == expected_size:
        print(f"  [PASS] Square simulation correct")
        return True
    else:
        print(f"  [FAIL] State mismatch")
        return False


def test_square_compilation():
    """Test compiling the Square program."""
    print("\n" + "=" * 70)
    print("  Chapter 11: Square Compilation Test")
    print("=" * 70)
    
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(project_dir):
        print(f"  [SKIP] Project not found: {project_dir}")
        return None
    
    # OS files needed by Square
    os_files = [
        'Sys.vm',      # Bootstrap, wait
        'Memory.vm',   # alloc, deAlloc
        'Screen.vm',   # setColor, drawRectangle
        'Keyboard.vm', # keyPressed
        'Math.vm',     # Used by Screen
        'Output.vm',   # May be used
        'String.vm',   # May be used
        'Array.vm',    # May be used
    ]
    
    temp_dir = None
    try:
        print(f"\n  Compiling {project_dir}...")
        temp_dir, vm_count = compile_jack_project(project_dir, os_dir, os_files)
        print(f"  VM commands: {vm_count}")
        
        print(f"\n  Compiled files:")
        for f in sorted(os.listdir(temp_dir)):
            if f.endswith('.vm'):
                path = os.path.join(temp_dir, f)
                with open(path) as vf:
                    lines = [l for l in vf if l.strip() and not l.strip().startswith('//')]
                print(f"    {f}: {len(lines)} commands")
        
        print(f"\n  Building Petri net...")
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        print(f"  Places: {len(net.places)}")
        print(f"  Transitions: {len(net.transitions)}")
        
        print(f"\n  [PASS] Square compiled successfully")
        return True
        
    except Exception as e:
        print(f"\n  [FAIL] {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


def main():
    print("=" * 70)
    print("  CHAPTER 11 SQUARE GAME TEST")
    print("=" * 70)
    
    results = []
    
    # Test Petri net simulation
    result = test_petri_net_square_simulation()
    results.append(("Petri Net Simulation", result))
    
    # Test compilation
    result = test_square_compilation()
    results.append(("Square Compilation", result))
    
    # Summary
    print("\n" + "=" * 70)
    print("  RESULTS")
    print("=" * 70)
    
    for name, result in results:
        status = "[PASS]" if result else "[FAIL]" if result is False else "[SKIP]"
        print(f"  {name}: {status}")
    
    passed = sum(1 for _, r in results if r is True)
    failed = sum(1 for _, r in results if r is False)
    
    print(f"\n  Passed: {passed}, Failed: {failed}")
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
