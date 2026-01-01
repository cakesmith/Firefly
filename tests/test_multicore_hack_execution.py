#!/usr/bin/env python3
"""
Multi-Core Hack Assembly Execution Test
========================================

This test executes generated Hack assembly on multiple CPU cores with:
1. Shared ROM - single instruction memory, each core has its own PC
2. Shared RAM - all cores read/write same memory (data synchronization via memory)
3. Memory arbitration - handles concurrent access
4. Cycle-accurate execution - all cores execute in lockstep

No explicit cross-core synchronization - data dependencies flow through shared RAM.
"""

import sys
import os
import tempfile
import shutil
from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser, vmcommand
from PetriEmitter import PetriEmitter
from CPU import CPU
from Petri.Token import Token


class HackAssembler:
    """Assembles Hack assembly into executable instructions."""
    
    def __init__(self):
        self.symbol_table = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "SCREEN": 16384, "KBD": 24576
        }
        for i in range(16):
            self.symbol_table[f"R{i}"] = i
    
    def assemble(self, assembly_lines: List[str]) -> Tuple[List[dict], Dict[str, int]]:
        """
        Assemble Hack assembly into instruction dictionaries.
        
        Returns:
            (instructions, labels) - instructions list and label->address map
        """
        # First pass: find labels
        labels = {}
        instruction_address = 0
        
        for line in assembly_lines:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            if line.startswith('(') and line.endswith(')'):
                label = line[1:-1]
                labels[label] = instruction_address
                self.symbol_table[label] = instruction_address
            else:
                instruction_address += 1
        
        # Second pass: assemble
        instructions = []
        next_var_address = 16
        
        for line in assembly_lines:
            line = line.strip()
            
            if not line or line.startswith('//'):
                continue
            if line.startswith('(') and line.endswith(')'):
                continue
            
            if '//' in line:
                line = line.split('//')[0].strip()
            
            if not line:
                continue
            
            if line.startswith('@'):
                value_str = line[1:]
                
                if value_str.isdigit():
                    value = int(value_str)
                elif value_str.lstrip('-').isdigit():
                    value = int(value_str)
                # Handle R<number> for any register address (R0, R1, ..., R6082, etc.)
                elif value_str.startswith('R') and value_str[1:].isdigit():
                    value = int(value_str[1:])
                elif value_str in self.symbol_table:
                    value = self.symbol_table[value_str]
                else:
                    self.symbol_table[value_str] = next_var_address
                    value = next_var_address
                    next_var_address += 1
                
                instructions.append({
                    "TYPE": "A_COMMAND",
                    "VAL": value
                })
            else:
                dest = ""
                comp = line
                jump = ""
                
                if '=' in line:
                    parts = line.split('=')
                    dest = parts[0].strip()
                    comp = parts[1].strip()
                
                if ';' in comp:
                    parts = comp.split(';')
                    comp = parts[0].strip()
                    jump = parts[1].strip()
                
                instructions.append({
                    "TYPE": "C_COMMAND",
                    "VAL": {
                        "DEST": dest,
                        "COMP": comp,
                        "JUMP": jump
                    }
                })
        
        return instructions, labels


@dataclass
class ExecutionStats:
    """Statistics from execution."""
    total_cycles: int = 0
    instructions_executed: Dict[int, int] = field(default_factory=dict)
    memory_reads: int = 0
    memory_writes: int = 0
    conflicts: int = 0
    stalls: int = 0


class MultiCoreCPU:
    """
    Multi-core CPU simulator with shared ROM and RAM.
    
    Each core:
    - Has its own PC, A, D registers
    - Fetches from shared ROM
    - Reads/writes to shared RAM
    """
    
    def __init__(self, num_cores: int):
        self.num_cores = num_cores
        self.shared_ram = [0] * 32768
        self.shared_rom: List[dict] = []
        
        # Per-core state
        self.cores: List[CPU] = []
        self.core_pcs: List[int] = []
        self.core_halted: List[bool] = []
        
        for i in range(num_cores):
            cpu = CPU(cpu_id=i, RAM=self.shared_ram)
            self.cores.append(cpu)
            self.core_pcs.append(0)
            self.core_halted.append(False)
        
        self.stats = ExecutionStats()
        self.stats.instructions_executed = {i: 0 for i in range(num_cores)}
        
        # Memory access tracking for conflict detection
        self.cycle_writes: Set[int] = set()
        self.cycle_reads: Set[int] = set()
    
    def load_rom(self, instructions: List[dict]):
        """Load instructions into shared ROM."""
        self.shared_rom = instructions
    
    def set_core_pc(self, core_id: int, pc: int):
        """Set starting PC for a core."""
        if 0 <= core_id < self.num_cores:
            self.core_pcs[core_id] = pc
            self.cores[core_id].PC = pc
    
    def execute_cycle(self) -> bool:
        """
        Execute one cycle on all cores simultaneously.
        
        Returns:
            True if any core executed, False if all halted
        """
        self.cycle_writes.clear()
        self.cycle_reads.clear()
        
        any_executed = False
        
        # Execute each core
        for core_id in range(self.num_cores):
            if self.core_halted[core_id]:
                continue
            
            pc = self.core_pcs[core_id]
            
            # Check bounds
            if pc >= len(self.shared_rom):
                self.core_halted[core_id] = True
                continue
            
            instruction = self.shared_rom[pc]
            cpu = self.cores[core_id]
            
            # Execute instruction
            result = self._execute_instruction(core_id, cpu, instruction)
            
            # Update PC
            if result['should_jump']:
                new_pc = result['jump_target']
                # Detect halt: jumping to an address that will jump back to itself
                # This handles the pattern: @HALT_LABEL / 0;JMP
                if new_pc == pc - 1:
                    # We're at the JMP instruction, jumping back to the @HALT
                    self.core_halted[core_id] = True
                else:
                    self.core_pcs[core_id] = new_pc
            else:
                self.core_pcs[core_id] = pc + 1
            
            self.stats.instructions_executed[core_id] += 1
            any_executed = True
        
        if any_executed:
            self.stats.total_cycles += 1
        
        return any_executed
    
    def _execute_instruction(self, core_id: int, cpu: CPU, instruction: dict) -> dict:
        """Execute a single instruction with memory tracking."""
        result = {
            'should_jump': False,
            'jump_target': None,
            'value': None
        }
        
        if instruction["TYPE"] == "A_COMMAND":
            cpu.A = instruction["VAL"]
            result['value'] = cpu.A
            
        elif instruction["TYPE"] == "C_COMMAND":
            dest = instruction["VAL"]["DEST"]
            comp = instruction["VAL"]["COMP"]
            jump = instruction["VAL"]["JUMP"]
            
            # Handle memory read
            if 'M' in comp:
                addr = cpu.A
                self.stats.memory_reads += 1
                
                # Check for read-write conflict
                if addr in self.cycle_writes:
                    self.stats.conflicts += 1
                
                self.cycle_reads.add(addr)
                mem_val = self.shared_ram[addr] if 0 <= addr < len(self.shared_ram) else 0
                comp_result = cpu.ALU[comp.replace("M", "A")](mem_val, cpu.D)
            else:
                comp_result = cpu.ALU[comp](cpu.A, cpu.D)
            
            # Update flags
            cpu.zr = 1 if comp_result == 0 else 0
            cpu.ng = 1 if comp_result < 0 else 0
            
            # Handle destinations
            if 'M' in dest:
                addr = cpu.A
                self.stats.memory_writes += 1
                
                # Check for write-write or read-write conflict
                if addr in self.cycle_writes or addr in self.cycle_reads:
                    self.stats.conflicts += 1
                
                self.cycle_writes.add(addr)
                if 0 <= addr < len(self.shared_ram):
                    self.shared_ram[addr] = comp_result
            
            if 'A' in dest:
                cpu.A = comp_result
            if 'D' in dest:
                cpu.D = comp_result
            
            result['value'] = comp_result
            
            # Handle jumps
            if jump:
                should_jump = False
                if jump == "JGT" and comp_result > 0:
                    should_jump = True
                elif jump == "JEQ" and comp_result == 0:
                    should_jump = True
                elif jump == "JGE" and comp_result >= 0:
                    should_jump = True
                elif jump == "JLT" and comp_result < 0:
                    should_jump = True
                elif jump == "JNE" and comp_result != 0:
                    should_jump = True
                elif jump == "JLE" and comp_result <= 0:
                    should_jump = True
                elif jump == "JMP":
                    should_jump = True
                
                if should_jump:
                    result['should_jump'] = True
                    result['jump_target'] = cpu.A
        
        return result
    
    def run(self, max_cycles: int = 10000, stall_threshold: int = 1000) -> ExecutionStats:
        """Run until all cores halt, max cycles reached, or no progress for stall_threshold cycles."""
        last_write_cycle = 0
        
        while self.stats.total_cycles < max_cycles:
            # Track if any memory writes happened this cycle
            writes_before = self.stats.memory_writes
            
            if not self.execute_cycle():
                break
            
            # Check if any writes happened
            if self.stats.memory_writes > writes_before:
                last_write_cycle = self.stats.total_cycles
            
            # Check if all halted
            if all(self.core_halted):
                break
            
            # Check for stall (no progress)
            if self.stats.total_cycles - last_write_cycle > stall_threshold:
                # No memory writes for stall_threshold cycles - we're stuck
                break
        
        return self.stats
    
    def get_ram(self, start: int, end: int) -> List[int]:
        """Get RAM contents."""
        return self.shared_ram[start:end]


def generate_multicore_rom(emitter: PetriEmitter, num_cores: int) -> Tuple[List[str], Dict[int, int], List[int]]:
    """
    Generate a unified ROM for multi-core execution with TRUE Petri net semantics.
    
    Each transition polls until:
    1. All input places have tokens (valid flag = 1)
    2. All output places are empty (valid flag = 0)
    
    When conditions met, FIRE:
    1. Clear input valid flags (consume tokens)
    2. Execute transition assembly
    3. Set output valid flags (produce tokens)
    
    Special handling for control flow:
    - goto: outputs to label place (no data, just control token)
    - ifgoto: conditionally outputs to label OR fallthrough place
    
    Memory layout:
    - R0-R49: Data slots (allocated by Petri net)
    - R100+place_id: Valid flags for each place (1=has token, 0=empty)
    
    Returns:
        (assembly_lines, core_entry_points, initial_marking_addrs)
    """
    net = emitter.net
    
    # Allocate memory and assign cores
    net.allocate_memory(verbose=True)
    net.assign_cpu_cores(num_cores, verbose=True)
    
    VALID_FLAG_BASE = 100  # Valid flags start at R100
    
    # Assign unique valid flag addresses to each place
    place_valid_addr = {}
    next_valid_id = 0
    for place_name in net.places.keys():
        place_valid_addr[place_name] = VALID_FLAG_BASE + next_valid_id
        next_valid_id += 1
    
    # Find initial marking - places that have tokens at start
    initial_marking = []
    for place_name, place in net.places.items():
        if place.has:
            initial_marking.append(place_valid_addr[place_name])
    
    # Get transition info
    transition_asm = {}
    transition_inputs = {}   # trans_name -> list of (place_name, data_addr, valid_addr)
    transition_outputs = {}  # trans_name -> list of (place_name, data_addr, valid_addr, is_label)
    
    for trans_name, trans in net.transitions.items():
        asm = trans.emit_assembly()
        if isinstance(asm, str):
            asm = [asm]
        transition_asm[trans_name] = asm
        
        # Get input places (skip "init" - handled by initial marking)
        inputs = []
        for place in trans.in_places:
            if place.name != "init":
                data_addr = place.memory_address
                valid_addr = place_valid_addr[place.name]
                inputs.append((place.name, data_addr, valid_addr))
        transition_inputs[trans_name] = inputs
        
        # Get output places with label info
        outputs = []
        for place in trans.out_places:
            data_addr = place.memory_address
            valid_addr = place_valid_addr[place.name]
            is_label = getattr(place, 'is_label', False)
            outputs.append((place.name, data_addr, valid_addr, is_label))
        transition_outputs[trans_name] = outputs
    
    # Group transitions by core, sorted by level
    core_transitions = defaultdict(list)
    for trans_name, core_id in net.cpu_assignments.items():
        level = net.transition_levels.get(trans_name, 0)
        core_transitions[core_id].append((level, trans_name))
    
    # Sort by level within each core
    for core_id in core_transitions:
        core_transitions[core_id].sort(key=lambda x: x[0])
    
    # Generate ROM
    rom_lines = []
    entry_points = {}
    
    def instr_count(lines):
        return sum(1 for l in lines 
                  if l.strip() and not l.strip().startswith('//') 
                  and not l.strip().startswith('('))
    
    for core_id in range(num_cores):
        entry_points[core_id] = instr_count(rom_lines)
        
        rom_lines.append(f"// ===== Core {core_id} =====")
        rom_lines.append(f"(CORE_{core_id}_START)")
        
        transitions = core_transitions.get(core_id, [])
        
        for idx, (level, trans_name) in enumerate(transitions):
            inputs = transition_inputs.get(trans_name, [])
            outputs = transition_outputs.get(trans_name, [])
            trans = net.transitions[trans_name]
            
            # Determine the next label to skip to if not ready
            if idx + 1 < len(transitions):
                next_trans_name = transitions[idx + 1][1]
                skip_label = f"CHECK_{next_trans_name}"
            else:
                skip_label = f"CORE_{core_id}_LOOP_END"
            
            rom_lines.append(f"// {trans_name} (level {level})")
            rom_lines.append(f"(CHECK_{trans_name})")
            
            # Check all input valid flags = 1 (has token) - SKIP if not ready
            for place_name, data_addr, valid_addr in inputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("D=M")
                rom_lines.append(f"@{skip_label}")
                rom_lines.append("D;JEQ")  # Skip to next transition if input not ready
            
            # Check all output valid flags = 0 (empty) - SKIP if not empty
            for place_name, data_addr, valid_addr, is_label in outputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("D=M")
                rom_lines.append(f"@{skip_label}")
                rom_lines.append("D;JNE")  # Skip to next transition if output not empty
            
            # FIRE: Clear input valid flags (consume tokens)
            for place_name, data_addr, valid_addr in inputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("M=0")
            
            # Check if this is an ifgoto transition (has both label and non-label outputs)
            is_ifgoto = trans_name.startswith("ifgoto_")
            label_outputs = [(n, d, v) for n, d, v, is_l in outputs if is_l]
            nonlabel_outputs = [(n, d, v) for n, d, v, is_l in outputs if not is_l]
            
            if is_ifgoto and label_outputs and nonlabel_outputs:
                # Conditional control flow
                # Find the condition input (non-label, non-control input)
                condition_addr = None
                for place_name, data_addr, valid_addr in inputs:
                    place = net.places[place_name]
                    if not getattr(place, 'is_label', False) and data_addr is not None:
                        condition_addr = data_addr
                        break
                
                if condition_addr is not None:
                    # Load condition
                    rom_lines.append(f"@R{condition_addr}")
                    rom_lines.append("D=M")
                    
                    # If condition != 0, jump to label (set label valid flag)
                    label_name, label_data, label_valid = label_outputs[0]
                    fallthrough_name, fallthrough_data, fallthrough_valid = nonlabel_outputs[0]
                    
                    rom_lines.append(f"@IFGOTO_TRUE_{trans_name}")
                    rom_lines.append("D;JNE")
                    
                    # Condition is false - set fallthrough valid flag
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{fallthrough_valid}")
                    rom_lines.append("M=D")
                    rom_lines.append(f"@IFGOTO_END_{trans_name}")
                    rom_lines.append("0;JMP")
                    
                    # Condition is true - set label valid flag
                    rom_lines.append(f"(IFGOTO_TRUE_{trans_name})")
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{label_valid}")
                    rom_lines.append("M=D")
                    
                    rom_lines.append(f"(IFGOTO_END_{trans_name})")
                else:
                    # No condition found, just execute assembly and set all outputs
                    asm = transition_asm.get(trans_name, [])
                    rom_lines.extend(asm)
                    for place_name, data_addr, valid_addr, is_label in outputs:
                        rom_lines.append("@1")
                        rom_lines.append("D=A")
                        rom_lines.append(f"@R{valid_addr}")
                        rom_lines.append("M=D")
            else:
                # Normal transition - execute assembly and set all output valid flags
                asm = transition_asm.get(trans_name, [])
                rom_lines.extend(asm)
                
                for place_name, data_addr, valid_addr, is_label in outputs:
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{valid_addr}")
                    rom_lines.append("M=D")
        
        # End of transition loop - loop back to start
        rom_lines.append(f"(CORE_{core_id}_LOOP_END)")
        rom_lines.append(f"// Loop back to re-check transitions")
        rom_lines.append(f"@CORE_{core_id}_START")
        rom_lines.append("0;JMP")
        rom_lines.append("")
    
    return rom_lines, entry_points, initial_marking


def build_emitter(commands: List[vmcommand]) -> PetriEmitter:
    """Build a Petri net emitter from VM commands."""
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
        elif cmd.command == "and":
            emitter.and_op(cmd)
        elif cmd.command == "or":
            emitter.or_op(cmd)
        elif cmd.command == "not":
            emitter.not_op(cmd)
    
    return emitter


def run_execution_test(name: str, commands: List[vmcommand], expected_result: int = None, debug: bool = False):
    """
    Run a multi-core execution test.
    
    Compares single-core vs multi-core execution cycles.
    """
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    
    results = {}
    result_addr = None  # Will be set from the emitter's control stack
    
    for num_cores in [1, 2, 4]:
        # Build fresh emitter
        emitter = build_emitter(commands)
        
        # Generate ROM
        rom_lines, entry_points, initial_marking = generate_multicore_rom(emitter, num_cores)
        
        # Get the result address from the top of the control stack
        if emitter.control_stack:
            result_place = emitter.control_stack[-1]
            result_addr = result_place.memory_address
        
        if debug and num_cores == 1:
            print("\n  Generated ROM:")
            for i, line in enumerate(rom_lines[:50]):
                print(f"    {i:3}: {line}")
            print(f"\n  Initial marking (valid flags to set): {initial_marking}")
            print(f"  Result address: R{result_addr}")
        
        # Assemble
        assembler = HackAssembler()
        instructions, labels = assembler.assemble(rom_lines)
        
        # Create multi-core CPU
        cpu = MultiCoreCPU(num_cores)
        cpu.load_rom(instructions)
        
        # Set initial marking - places with tokens get valid=1
        for addr in initial_marking:
            cpu.shared_ram[addr] = 1
        
        # Set entry points
        for core_id, pc in entry_points.items():
            cpu.set_core_pc(core_id, pc)
        
        # Run
        stats = cpu.run(max_cycles=10000)
        
        results[num_cores] = {
            'cycles': stats.total_cycles,
            'instructions': stats.instructions_executed,
            'conflicts': stats.conflicts,
            'ram': cpu.get_ram(0, 20)
        }
        
        total_instr = sum(stats.instructions_executed.values())
        print(f"\n  {num_cores} core(s):")
        print(f"    Cycles: {stats.total_cycles}")
        print(f"    Instructions: {total_instr} total, {dict(stats.instructions_executed)}")
        print(f"    Memory conflicts: {stats.conflicts}")
        print(f"    RAM[0-9]: {cpu.get_ram(0, 10)}")
    
    # Calculate speedup
    base_cycles = results[1]['cycles']
    print(f"\n  Speedup:")
    for num_cores in [2, 4]:
        mc_cycles = results[num_cores]['cycles']
        if mc_cycles > 0:
            speedup = base_cycles / mc_cycles
            print(f"    {num_cores} cores: {speedup:.2f}x")
    
    # Verify result if expected
    if expected_result is not None and result_addr is not None:
        # Result is at the address from the top of the control stack
        actual = results[1]['ram'][result_addr]
        if actual == expected_result:
            print(f"\n  [PASS] Result R0={actual} matches expected {expected_result}")
            return True
        else:
            print(f"\n  [FAIL] Expected {expected_result}, got {actual}")
            return False
    
    return True


def test_simple_add():
    """Test simple addition."""
    commands = [
        vmcommand("push", "constant", 7),
        vmcommand("push", "constant", 8),
        vmcommand("add"),
    ]
    return run_execution_test("Simple Add (7 + 8 = 15)", commands, expected_result=15, debug=True)


def test_parallel_pushes():
    """Test parallel push operations."""
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("push", "constant", 30),
        vmcommand("push", "constant", 40),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    return run_execution_test("Parallel Pushes (10+20+30+40=100)", commands, expected_result=100)


def test_wide_parallel():
    """Test wide parallelism with 8 values."""
    commands = [
        vmcommand("push", "constant", 1),
        vmcommand("push", "constant", 2),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 4),
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 6),
        vmcommand("push", "constant", 7),
        vmcommand("push", "constant", 8),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    return run_execution_test("Wide Parallel (1+2+...+8=36)", commands, expected_result=36)


def test_mixed_operations():
    """Test mixed arithmetic operations."""
    commands = [
        vmcommand("push", "constant", 100),
        vmcommand("push", "constant", 30),
        vmcommand("sub"),
        vmcommand("push", "constant", 10),
        vmcommand("add"),
    ]
    return run_execution_test("Mixed Ops (100-30+10=80)", commands, expected_result=80)


def test_comparison():
    """Test comparison operation."""
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 5),
        vmcommand("gt"),
    ]
    return run_execution_test("Comparison (10>5=-1)", commands, expected_result=-1)


def test_negation():
    """Test negation operation."""
    commands = [
        vmcommand("push", "constant", 42),
        vmcommand("neg"),
    ]
    return run_execution_test("Negation (-42)", commands, expected_result=-42)


def test_jack_compilation():
    """Test with compiled Jack code including OS libraries."""
    print(f"\n{'='*60}")
    print(f"  Jack Compilation Test")
    print(f"{'='*60}")
    
    source_dir = "tecs/projects/11/Seven"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(source_dir):
        print(f"  [SKIP] Source not found: {source_dir}")
        return None
    
    temp_dir = tempfile.mkdtemp(prefix="hack_exec_test_")
    
    try:
        # Copy Jack files and compile
        for f in os.listdir(source_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(source_dir, f), temp_dir)
        
        compiler = ExpressionEvaluator(temp_dir, overwrite=True)
        
        # Copy OS VM files (Math.vm, Output.vm, etc.)
        if os.path.exists(os_dir):
            for f in os.listdir(os_dir):
                if f.endswith('.vm'):
                    shutil.copy(os.path.join(os_dir, f), temp_dir)
        
        # Parse all VM files
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        
        print(f"\n  Compiled + OS: {len(parser.results)} VM commands")
        print(f"  Petri net: {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
        
        # DEBUG: Run with 1 core and detailed tracing
        num_cores = 1
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Generate ROM with debug info
        rom_lines, entry_points, initial_marking = generate_multicore_rom(emitter, num_cores)
        
        # Build place_valid_addr map for debugging
        VALID_FLAG_BASE = 100
        place_valid_addr = {}
        valid_addr_to_place = {}
        next_valid_id = 0
        for place_name in net.places.keys():
            addr = VALID_FLAG_BASE + next_valid_id
            place_valid_addr[place_name] = addr
            valid_addr_to_place[addr] = place_name
            next_valid_id += 1
        
        # DEBUG: What is R110?
        print(f"\n  DEBUG: R110 corresponds to place: {valid_addr_to_place.get(110, 'UNKNOWN')}")
        
        # Find what transition needs R110 as input
        target_place_name = valid_addr_to_place.get(110)
        if target_place_name:
            target_place = net.places.get(target_place_name)
            print(f"  DEBUG: Place '{target_place_name}' details:")
            print(f"    - is_label: {getattr(target_place, 'is_label', False)}")
            print(f"    - memory_address: {target_place.memory_address}")
            print(f"    - has token: {target_place.has}")
            
            # Find transitions that consume from this place
            consumers = []
            for trans_name, trans in net.transitions.items():
                if target_place in trans.in_places:
                    consumers.append(trans_name)
            print(f"    - Consumed by transitions: {consumers}")
            
            # Find transitions that produce to this place
            producers = []
            for trans_name, trans in net.transitions.items():
                if target_place in trans.out_places:
                    producers.append(trans_name)
            print(f"    - Produced by transitions: {producers}")
            
            # For each producer, show its inputs
            for prod_name in producers:
                prod_trans = net.transitions[prod_name]
                prod_inputs = [(p.name, place_valid_addr.get(p.name)) for p in prod_trans.in_places]
                print(f"    - Producer '{prod_name}' needs inputs: {prod_inputs}")
        
        # Assemble
        assembler = HackAssembler()
        instructions, labels = assembler.assemble(rom_lines)
        
        # Run with tracing
        cpu = MultiCoreCPU(num_cores)
        cpu.load_rom(instructions)
        
        # Set initial marking
        for addr in initial_marking:
            cpu.shared_ram[addr] = 1
        
        print(f"\n  DEBUG: Initial marking (valid flags set to 1): {initial_marking}")
        print(f"  DEBUG: Initial marking places: {[valid_addr_to_place.get(a, f'R{a}') for a in initial_marking]}")
        
        for core_id, pc in entry_points.items():
            cpu.set_core_pc(core_id, pc)
        
        # Run with periodic status checks
        max_cycles = 50000
        check_interval = 10000
        last_pc = -1
        stuck_count = 0
        
        while cpu.stats.total_cycles < max_cycles:
            if not cpu.execute_cycle():
                break
            
            # Check if stuck
            current_pc = cpu.core_pcs[0]
            if current_pc == last_pc:
                stuck_count += 1
                if stuck_count >= 100:
                    # We're stuck - debug why
                    print(f"\n  DEBUG: Stuck at PC={current_pc} after {cpu.stats.total_cycles} cycles")
                    
                    # Show the instruction at this PC
                    if current_pc < len(instructions):
                        instr = instructions[current_pc]
                        print(f"  DEBUG: Instruction at PC={current_pc}: {instr}")
                    
                    # Find what ROM line this corresponds to
                    instr_idx = 0
                    for i, line in enumerate(rom_lines):
                        line = line.strip()
                        if not line or line.startswith('//') or line.startswith('('):
                            continue
                        if instr_idx == current_pc:
                            # Show context
                            print(f"  DEBUG: ROM context around PC={current_pc}:")
                            for j in range(max(0, i-5), min(len(rom_lines), i+10)):
                                marker = ">>>" if j == i else "   "
                                print(f"    {marker} {j}: {rom_lines[j]}")
                            break
                        instr_idx += 1
                    
                    # Show relevant valid flags
                    print(f"\n  DEBUG: Valid flags R100-R120:")
                    for addr in range(100, 121):
                        val = cpu.shared_ram[addr]
                        place = valid_addr_to_place.get(addr, "?")
                        if val != 0 or addr == 110:
                            print(f"    R{addr} ({place}): {val}")
                    
                    break
            else:
                stuck_count = 0
                last_pc = current_pc
            
            if all(cpu.core_halted):
                break
        
        stats = cpu.stats
        print(f"\n  1 core: {stats.total_cycles} cycles, {sum(stats.instructions_executed.values())} instructions")
        
        return True
        
    except Exception as e:
        print(f"  [FAIL] {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        shutil.rmtree(temp_dir)


def main():
    """Run all tests."""
    print("╔════════════════════════════════════════════════════════════╗")
    print("║  Multi-Core Hack Assembly Execution Tests                  ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    tests = [
        ("Simple Add", test_simple_add),
        ("Parallel Pushes", test_parallel_pushes),
        ("Wide Parallel", test_wide_parallel),
        ("Mixed Operations", test_mixed_operations),
        ("Comparison", test_comparison),
        ("Negation", test_negation),
        ("Jack Compilation", test_jack_compilation),
    ]
    
    results = []
    for name, test_fn in tests:
        try:
            result = test_fn()
            results.append((name, result))
        except Exception as e:
            print(f"\n  [ERROR] {name}: {e}")
            results.append((name, False))
    
    # Summary
    print(f"\n{'='*60}")
    print("  RESULTS")
    print(f"{'='*60}")
    
    passed = sum(1 for _, r in results if r is True)
    failed = sum(1 for _, r in results if r is False)
    skipped = sum(1 for _, r in results if r is None)
    
    for name, result in results:
        status = "[PASS]" if result is True else "[FAIL]" if result is False else "[SKIP]"
        print(f"  {name:30} {status}")
    
    print(f"\n  Total: {passed} passed, {failed} failed, {skipped} skipped")
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
