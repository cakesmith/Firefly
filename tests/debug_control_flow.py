#!/usr/bin/env python3
"""
Debug control flow (label, goto, if-goto) with a minimal example.

Tests a simple loop pattern:
  push constant 0    // counter = 0
  label LOOP
  push constant 1
  add                // counter++
  push constant 3
  lt                 // counter < 3?
  if-goto LOOP       // if true, loop
  // result should be 3
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import vmcommand
from PetriEmitter import PetriEmitter
from Petri.Token import Token

from test_multicore_hack_execution import (
    HackAssembler, MultiCoreCPU, generate_multicore_rom
)


def build_emitter_with_control_flow(commands):
    """Build a Petri net emitter from VM commands including control flow."""
    emitter = PetriEmitter()
    
    for cmd in commands:
        if cmd.command == "push" and cmd.segment == "constant":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
        elif cmd.command == "sub":
            emitter.sub(cmd)
        elif cmd.command == "neg":
            emitter.neg(cmd)
        elif cmd.command == "lt":
            emitter.lt(cmd)
        elif cmd.command == "eq":
            emitter.eq(cmd)
        elif cmd.command == "gt":
            emitter.gt(cmd)
        elif cmd.command == "not":
            emitter.not_op(cmd)
        elif cmd.command == "label":
            emitter.label(cmd)
        elif cmd.command == "goto":
            emitter.goto(cmd)
        elif cmd.command == "if-goto":
            emitter.ifgoto(cmd)
    
    return emitter


def run_petri_simulation(emitter, max_steps=50, verbose=True):
    """Run Petri net simulation and track which transitions fire."""
    net = emitter.net
    
    print("\n" + "="*60)
    print("  PETRI NET SIMULATION")
    print("="*60)
    
    # Show initial marking
    print("\nInitial marking (places with tokens):")
    for place_name, place in net.places.items():
        if place.has:
            print(f"  {place_name}: {place.token}")
    
    fired_history = []
    
    for step in range(max_steps):
        # Find enabled transitions
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        
        if not enabled:
            print(f"\nStep {step}: No enabled transitions - simulation complete")
            break
        
        if verbose:
            print(f"\nStep {step}: {len(enabled)} enabled transitions")
            for t in enabled:
                inputs = [p.name for p in t.in_places]
                outputs = [p.name for p in t.out_places]
                print(f"  - {t.name}")
                print(f"      inputs: {inputs}")
                print(f"      outputs: {outputs}")
        
        # Fire all enabled transitions
        fired = net.execute_step()
        fired_history.append(fired)
        
        if verbose:
            print(f"  Fired: {fired}")
            
            # Show current marking
            print("  Current marking:")
            for place_name, place in net.places.items():
                if place.has:
                    print(f"    {place_name}: {place.token}")
    
    print(f"\nSimulation completed in {len(fired_history)} steps")
    print(f"Total transitions fired: {sum(len(f) for f in fired_history)}")
    
    return fired_history


def analyze_petri_net(emitter):
    """Analyze the Petri net structure."""
    net = emitter.net
    
    print("\n" + "="*60)
    print("  PETRI NET STRUCTURE")
    print("="*60)
    
    print(f"\nPlaces ({len(net.places)}):")
    for name, place in net.places.items():
        is_label = getattr(place, 'is_label', False)
        has_token = place.has
        print(f"  {name}: is_label={is_label}, has_token={has_token}")
    
    print(f"\nTransitions ({len(net.transitions)}):")
    for name, trans in net.transitions.items():
        inputs = [p.name for p in trans.in_places]
        outputs = [p.name for p in trans.out_places]
        print(f"  {name}:")
        print(f"    inputs: {inputs}")
        print(f"    outputs: {outputs}")
    
    print(f"\nLabels registry:")
    if hasattr(net, 'labels'):
        for label_name, place in net.labels.items():
            print(f"  {label_name} -> {place.name}")


def run_assembly_execution(emitter, num_cores=1, max_cycles=200, verbose=True):
    """Run assembly execution with tracing."""
    net = emitter.net
    
    # Generate ROM
    rom_lines, entry_points, initial_marking = generate_multicore_rom(emitter, num_cores)
    
    print("\n" + "="*60)
    print("  ASSEMBLY EXECUTION")
    print("="*60)
    
    print(f"\nInitial marking (valid flags set to 1): {initial_marking}")
    print(f"Entry points: {entry_points}")
    
    if verbose:
        print("\nGenerated ROM:")
        for i, line in enumerate(rom_lines):
            print(f"  {i:3}: {line}")
    
    # Assemble
    assembler = HackAssembler()
    instructions, labels = assembler.assemble(rom_lines)
    
    print(f"\nROM size: {len(instructions)} instructions")
    print(f"Labels: {labels}")
    
    # Create CPU
    cpu = MultiCoreCPU(num_cores)
    cpu.load_rom(instructions)
    
    # Set initial marking
    for addr in initial_marking:
        cpu.shared_ram[addr] = 1
    
    for core_id, pc in entry_points.items():
        cpu.set_core_pc(core_id, pc)
    
    # Track valid flag changes
    VALID_FLAG_BASE = 100
    valid_flags_to_watch = list(range(100, 115))
    
    prev_valid_state = {addr: cpu.shared_ram[addr] for addr in valid_flags_to_watch}
    
    print(f"\nInitial valid flags R100-R114: {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
    
    # Run with tracing
    for cycle in range(max_cycles):
        # Check for valid flag changes
        current_valid_state = {addr: cpu.shared_ram[addr] for addr in valid_flags_to_watch}
        
        changes = []
        for addr in valid_flags_to_watch:
            if current_valid_state[addr] != prev_valid_state[addr]:
                changes.append((addr, prev_valid_state[addr], current_valid_state[addr]))
        
        if changes and verbose:
            print(f"\nCycle {cycle}: Valid flag changes:")
            for addr, old, new in changes:
                print(f"  R{addr}: {old} -> {new}")
        
        prev_valid_state = current_valid_state.copy()
        
        # Execute one cycle
        if not cpu.execute_cycle():
            print(f"\nCycle {cycle}: All cores halted")
            break
        
        # Periodic status
        if cycle % 50 == 0 and cycle > 0:
            print(f"\nCycle {cycle}: PCs = {cpu.core_pcs}")
            print(f"  Valid flags: {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
            print(f"  Data R0-R10: {cpu.get_ram(0, 11)}")
    
    print(f"\nExecution completed after {cpu.stats.total_cycles} cycles")
    print(f"Final valid flags R100-R114: {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
    print(f"Final data R0-R10: {cpu.get_ram(0, 11)}")
    
    return cpu


def test_simple_ifgoto():
    """Test a simple if-goto pattern."""
    print("\n" + "="*60)
    print("  TEST: Simple if-goto")
    print("="*60)
    
    # push 5, push 3, gt (5 > 3 = true = -1), if-goto SKIP, push 100, label SKIP, push 200
    # If if-goto works: result should be 200
    # If if-goto fails: result would be 100 then 200
    commands = [
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 3),
        vmcommand("gt"),  # 5 > 3 = -1 (true)
        vmcommand("if-goto", "SKIP", 0),  # should jump
        vmcommand("push", "constant", 100),  # should be skipped
        vmcommand("label", "SKIP", 0),
        vmcommand("push", "constant", 200),  # should execute
    ]
    
    emitter = build_emitter_with_control_flow(commands)
    
    analyze_petri_net(emitter)
    run_petri_simulation(emitter, max_steps=20, verbose=True)
    
    # Fresh emitter for assembly
    emitter2 = build_emitter_with_control_flow(commands)
    run_assembly_execution(emitter2, num_cores=1, max_cycles=200, verbose=True)


def test_simple_goto():
    """Test a simple goto pattern."""
    print("\n" + "="*60)
    print("  TEST: Simple goto")
    print("="*60)
    
    # push 10, goto END, push 20, label END, push 30
    # Result should be 10, then 30 (20 skipped)
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("goto", "END", 0),
        vmcommand("push", "constant", 20),  # should be skipped
        vmcommand("label", "END", 0),
        vmcommand("push", "constant", 30),
    ]
    
    emitter = build_emitter_with_control_flow(commands)
    
    analyze_petri_net(emitter)
    run_petri_simulation(emitter, max_steps=20, verbose=True)
    
    # Fresh emitter for assembly
    emitter2 = build_emitter_with_control_flow(commands)
    run_assembly_execution(emitter2, num_cores=1, max_cycles=200, verbose=True)


def main():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║  Debug Control Flow (label, goto, if-goto)                 ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    test_simple_goto()
    test_simple_ifgoto()


if __name__ == "__main__":
    main()
