#!/usr/bin/env python3
"""
Debug script to trace why R110 never gets set in the Jack compilation test.

Compares:
1. Petri net simulation (step by step)
2. Assembly execution (cycle by cycle)

Identifies which place R110 corresponds to and what transition should enable it.
"""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser, vmcommand
from PetriEmitter import PetriEmitter
from Petri.Token import Token

# Import from the test file
from test_multicore_hack_execution import (
    HackAssembler, MultiCoreCPU, generate_multicore_rom
)


def run_petri_simulation(emitter, max_steps=100, verbose=True):
    """
    Run Petri net simulation and track which transitions fire.
    """
    net = emitter.net
    
    print("\n" + "="*70)
    print("  PETRI NET SIMULATION")
    print("="*70)
    
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
            for t in enabled[:10]:  # Show first 10
                inputs = [p.name for p in t.in_places]
                outputs = [p.name for p in t.out_places]
                print(f"  - {t.name}")
                print(f"      inputs: {inputs}")
                print(f"      outputs: {outputs}")
            if len(enabled) > 10:
                print(f"  ... and {len(enabled) - 10} more")
        
        # Fire all enabled transitions
        fired = net.execute_step()
        fired_history.append(fired)
        
        if verbose:
            print(f"  Fired: {fired[:10]}{'...' if len(fired) > 10 else ''}")
    
    print(f"\nSimulation completed in {len(fired_history)} steps")
    print(f"Total transitions fired: {sum(len(f) for f in fired_history)}")
    
    return fired_history


def analyze_place_r110(emitter, num_cores=1):
    """
    Analyze what place corresponds to valid flag R110 and what should enable it.
    """
    net = emitter.net
    
    # Allocate memory to get valid flag assignments
    net.allocate_memory(verbose=False)
    net.assign_cpu_cores(num_cores, verbose=False)
    
    VALID_FLAG_BASE = 100
    
    # Build place -> valid_addr mapping
    place_valid_addr = {}
    valid_addr_to_place = {}
    next_valid_id = 0
    
    for place_name in net.places.keys():
        addr = VALID_FLAG_BASE + next_valid_id
        place_valid_addr[place_name] = addr
        valid_addr_to_place[addr] = place_name
        next_valid_id += 1
    
    print("\n" + "="*70)
    print("  PLACE R110 ANALYSIS")
    print("="*70)
    
    if 110 in valid_addr_to_place:
        place_name = valid_addr_to_place[110]
        place = net.places[place_name]
        
        print(f"\nR110 corresponds to place: {place_name}")
        print(f"  is_label: {getattr(place, 'is_label', False)}")
        print(f"  memory_address: {place.memory_address}")
        print(f"  has token initially: {place.has}")
        
        # Find transitions that OUTPUT to this place (would set R110)
        producers = []
        for trans_name, trans in net.transitions.items():
            if place in trans.out_places:
                producers.append(trans_name)
        
        print(f"\nTransitions that OUTPUT to {place_name} (would set R110):")
        for trans_name in producers:
            trans = net.transitions[trans_name]
            inputs = [(p.name, place_valid_addr[p.name]) for p in trans.in_places]
            print(f"  - {trans_name}")
            print(f"      inputs: {inputs}")
            print(f"      level: {net.transition_levels.get(trans_name, '?')}")
            print(f"      core: {net.cpu_assignments.get(trans_name, '?')}")
        
        # Find transitions that INPUT from this place (would consume R110)
        consumers = []
        for trans_name, trans in net.transitions.items():
            if place in trans.in_places:
                consumers.append(trans_name)
        
        print(f"\nTransitions that INPUT from {place_name} (waiting for R110):")
        for trans_name in consumers:
            trans = net.transitions[trans_name]
            all_inputs = [(p.name, place_valid_addr[p.name]) for p in trans.in_places]
            print(f"  - {trans_name}")
            print(f"      all inputs: {all_inputs}")
            print(f"      level: {net.transition_levels.get(trans_name, '?')}")
            print(f"      core: {net.cpu_assignments.get(trans_name, '?')}")
        
        # Trace back: what enables the producers?
        print(f"\nTrace back - what enables the producers of R110?")
        for trans_name in producers:
            trans = net.transitions[trans_name]
            print(f"\n  Producer: {trans_name}")
            for input_place in trans.in_places:
                input_valid = place_valid_addr[input_place.name]
                print(f"    Needs: {input_place.name} (R{input_valid})")
                
                # What produces this input?
                for t2_name, t2 in net.transitions.items():
                    if input_place in t2.out_places:
                        print(f"      <- produced by: {t2_name}")
    else:
        print(f"\nR110 not found in valid address mapping!")
        print(f"Valid addresses range: R{VALID_FLAG_BASE} to R{VALID_FLAG_BASE + len(net.places) - 1}")
    
    return place_valid_addr, valid_addr_to_place


def run_assembly_with_trace(emitter, num_cores=1, max_cycles=1000):
    """
    Run assembly execution with detailed tracing of valid flag changes.
    """
    net = emitter.net
    
    # Generate ROM
    rom_lines, entry_points, initial_marking = generate_multicore_rom(emitter, num_cores)
    
    print("\n" + "="*70)
    print("  ASSEMBLY EXECUTION TRACE")
    print("="*70)
    
    print(f"\nInitial marking (valid flags set to 1): {initial_marking}")
    print(f"Entry points: {entry_points}")
    
    # Assemble
    assembler = HackAssembler()
    instructions, labels = assembler.assemble(rom_lines)
    
    print(f"\nROM size: {len(instructions)} instructions")
    
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
    valid_flags_to_watch = list(range(100, 120))  # Watch R100-R119
    
    prev_valid_state = {addr: cpu.shared_ram[addr] for addr in valid_flags_to_watch}
    
    print(f"\nInitial valid flag state (R100-R119):")
    print(f"  {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
    
    # Run with tracing
    transitions_fired = []
    
    for cycle in range(max_cycles):
        # Check for valid flag changes before this cycle
        current_valid_state = {addr: cpu.shared_ram[addr] for addr in valid_flags_to_watch}
        
        changes = []
        for addr in valid_flags_to_watch:
            if current_valid_state[addr] != prev_valid_state[addr]:
                changes.append((addr, prev_valid_state[addr], current_valid_state[addr]))
        
        if changes:
            print(f"\nCycle {cycle}: Valid flag changes:")
            for addr, old, new in changes:
                print(f"  R{addr}: {old} -> {new}")
        
        prev_valid_state = current_valid_state.copy()
        
        # Execute one cycle
        if not cpu.execute_cycle():
            print(f"\nCycle {cycle}: All cores halted")
            break
        
        # Check if stuck (all cores at same PC for too long)
        if cycle > 100 and cycle % 100 == 0:
            print(f"\nCycle {cycle}: PCs = {cpu.core_pcs}, halted = {cpu.core_halted}")
            print(f"  Valid flags R100-R119: {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
            
            # Check what instruction we're stuck on
            for core_id in range(num_cores):
                if not cpu.core_halted[core_id]:
                    pc = cpu.core_pcs[core_id]
                    if pc < len(rom_lines):
                        # Find the assembly line around this PC
                        instr_idx = 0
                        for i, line in enumerate(rom_lines):
                            if line.strip() and not line.strip().startswith('//') and not line.strip().startswith('('):
                                if instr_idx == pc:
                                    print(f"  Core {core_id} at PC={pc}: {line.strip()}")
                                    # Show context
                                    for j in range(max(0, i-2), min(len(rom_lines), i+3)):
                                        marker = ">>>" if j == i else "   "
                                        print(f"    {marker} {rom_lines[j]}")
                                    break
                                instr_idx += 1
    
    print(f"\nExecution completed after {cpu.stats.total_cycles} cycles")
    print(f"Final valid flags R100-R119: {[cpu.shared_ram[addr] for addr in valid_flags_to_watch]}")
    
    # Check R110 specifically
    print(f"\nR110 final value: {cpu.shared_ram[110]}")
    
    return cpu


def main():
    """Run debug analysis on Jack compilation test."""
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║  Debug R110 - Jack Compilation Test                                ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    
    source_dir = "tecs/projects/11/Seven"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(source_dir):
        print(f"Source not found: {source_dir}")
        return
    
    temp_dir = tempfile.mkdtemp(prefix="debug_r110_")
    
    try:
        # Copy Jack files and compile
        for f in os.listdir(source_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(source_dir, f), temp_dir)
        
        compiler = ExpressionEvaluator(temp_dir, overwrite=True)
        
        # Copy OS VM files
        if os.path.exists(os_dir):
            for f in os.listdir(os_dir):
                if f.endswith('.vm'):
                    shutil.copy(os.path.join(os_dir, f), temp_dir)
        
        # Parse all VM files
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        
        print(f"\nCompiled + OS: {len(parser.results)} VM commands")
        print(f"Petri net: {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
        
        # Analyze R110
        place_valid_addr, valid_addr_to_place = analyze_place_r110(emitter, num_cores=1)
        
        # Run Petri simulation (limited steps)
        print("\n" + "="*70)
        print("  Running Petri net simulation (first 20 steps)...")
        print("="*70)
        
        # Reset the net for simulation
        parser2 = VMParser(temp_dir)
        emitter2 = parser2.emitter
        fired_history = run_petri_simulation(emitter2, max_steps=20, verbose=True)
        
        # Run assembly execution with trace
        print("\n" + "="*70)
        print("  Running assembly execution with trace...")
        print("="*70)
        
        parser3 = VMParser(temp_dir)
        emitter3 = parser3.emitter
        cpu = run_assembly_with_trace(emitter3, num_cores=1, max_cycles=500)
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    main()
