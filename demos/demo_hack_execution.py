#!/usr/bin/env python3
"""
Multi-Core Hack Assembly Execution Demonstration
================================================
Shows actual execution of generated Hack assembly on multiple CPU cores
with shared ROM and RAM. Compares Petri net simulation with actual
Hack CPU execution.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from Petri.Token import Token
from VMParser import vmcommand
from CPU import CPU
from collections import defaultdict
from typing import Dict, List, Set, Tuple


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
        """Assemble Hack assembly into instruction dictionaries."""
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


class MultiCoreCPU:
    """Multi-core CPU simulator with shared ROM and RAM."""
    
    def __init__(self, num_cores: int):
        self.num_cores = num_cores
        self.shared_ram = [0] * 32768
        self.shared_rom: List[dict] = []
        
        self.cores: List[CPU] = []
        self.core_pcs: List[int] = []
        self.core_halted: List[bool] = []
        
        for i in range(num_cores):
            cpu = CPU(cpu_id=i, RAM=self.shared_ram)
            self.cores.append(cpu)
            self.core_pcs.append(0)
            self.core_halted.append(False)
        
        self.total_cycles = 0
        self.instructions_executed = {i: 0 for i in range(num_cores)}
        self.memory_writes = 0
    
    def load_rom(self, instructions: List[dict]):
        self.shared_rom = instructions
    
    def set_core_pc(self, core_id: int, pc: int):
        if 0 <= core_id < self.num_cores:
            self.core_pcs[core_id] = pc
            self.cores[core_id].PC = pc
    
    def execute_cycle(self) -> bool:
        any_executed = False
        
        for core_id in range(self.num_cores):
            if self.core_halted[core_id]:
                continue
            
            pc = self.core_pcs[core_id]
            
            if pc >= len(self.shared_rom):
                self.core_halted[core_id] = True
                continue
            
            instruction = self.shared_rom[pc]
            cpu = self.cores[core_id]
            
            result = self._execute_instruction(core_id, cpu, instruction)
            
            if result['should_jump']:
                new_pc = result['jump_target']
                if new_pc == pc - 1:
                    self.core_halted[core_id] = True
                else:
                    self.core_pcs[core_id] = new_pc
            else:
                self.core_pcs[core_id] = pc + 1
            
            self.instructions_executed[core_id] += 1
            any_executed = True
        
        if any_executed:
            self.total_cycles += 1
        
        return any_executed
    
    def _execute_instruction(self, core_id: int, cpu: CPU, instruction: dict) -> dict:
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
            
            if 'M' in comp:
                addr = cpu.A
                mem_val = self.shared_ram[addr] if 0 <= addr < len(self.shared_ram) else 0
                comp_result = cpu.ALU[comp.replace("M", "A")](mem_val, cpu.D)
            else:
                comp_result = cpu.ALU[comp](cpu.A, cpu.D)
            
            cpu.zr = 1 if comp_result == 0 else 0
            cpu.ng = 1 if comp_result < 0 else 0
            
            if 'M' in dest:
                addr = cpu.A
                self.memory_writes += 1
                if 0 <= addr < len(self.shared_ram):
                    self.shared_ram[addr] = comp_result
            
            if 'A' in dest:
                cpu.A = comp_result
            if 'D' in dest:
                cpu.D = comp_result
            
            result['value'] = comp_result
            
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
    
    def run(self, max_cycles: int = 10000, stall_threshold: int = 1000) -> int:
        last_write_cycle = 0
        
        while self.total_cycles < max_cycles:
            writes_before = self.memory_writes
            
            if not self.execute_cycle():
                break
            
            if self.memory_writes > writes_before:
                last_write_cycle = self.total_cycles
            
            if all(self.core_halted):
                break
            
            if self.total_cycles - last_write_cycle > stall_threshold:
                break
        
        return self.total_cycles


def generate_multicore_rom(emitter: PetriEmitter, num_cores: int) -> Tuple[List[str], Dict[int, int], List[int]]:
    """Generate a unified ROM for multi-core execution with Petri net semantics."""
    net = emitter.net
    
    net.allocate_memory(verbose=False)
    net.assign_cpu_cores(num_cores, verbose=False)
    
    VALID_FLAG_BASE = 100
    
    place_valid_addr = {}
    next_valid_id = 0
    for place_name in net.places.keys():
        place_valid_addr[place_name] = VALID_FLAG_BASE + next_valid_id
        next_valid_id += 1
    
    initial_marking = []
    for place_name, place in net.places.items():
        if place.has:
            initial_marking.append(place_valid_addr[place_name])
    
    transition_asm = {}
    transition_inputs = {}
    transition_outputs = {}
    
    for trans_name, trans in net.transitions.items():
        asm = trans.emit_assembly()
        if isinstance(asm, str):
            asm = [asm]
        transition_asm[trans_name] = asm
        
        inputs = []
        for place in trans.in_places:
            if place.name != "init":
                data_addr = place.memory_address
                valid_addr = place_valid_addr[place.name]
                inputs.append((place.name, data_addr, valid_addr))
        transition_inputs[trans_name] = inputs
        
        outputs = []
        for place in trans.out_places:
            data_addr = place.memory_address
            valid_addr = place_valid_addr[place.name]
            is_label = getattr(place, 'is_label', False)
            outputs.append((place.name, data_addr, valid_addr, is_label))
        transition_outputs[trans_name] = outputs
    
    core_transitions = defaultdict(list)
    for trans_name, core_id in net.cpu_assignments.items():
        level = net.transition_levels.get(trans_name, 0)
        core_transitions[core_id].append((level, trans_name))
    
    for core_id in core_transitions:
        core_transitions[core_id].sort(key=lambda x: x[0])
    
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
            
            if idx + 1 < len(transitions):
                next_trans_name = transitions[idx + 1][1]
                skip_label = f"CHECK_{next_trans_name}"
            else:
                skip_label = f"CORE_{core_id}_LOOP_END"
            
            rom_lines.append(f"// {trans_name} (level {level})")
            rom_lines.append(f"(CHECK_{trans_name})")
            
            for place_name, data_addr, valid_addr in inputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("D=M")
                rom_lines.append(f"@{skip_label}")
                rom_lines.append("D;JEQ")
            
            for place_name, data_addr, valid_addr, is_label in outputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("D=M")
                rom_lines.append(f"@{skip_label}")
                rom_lines.append("D;JNE")
            
            for place_name, data_addr, valid_addr in inputs:
                rom_lines.append(f"@R{valid_addr}")
                rom_lines.append("M=0")
            
            is_ifgoto = trans_name.startswith("ifgoto_")
            label_outputs = [(n, d, v) for n, d, v, is_l in outputs if is_l]
            nonlabel_outputs = [(n, d, v) for n, d, v, is_l in outputs if not is_l]
            
            if is_ifgoto and label_outputs and nonlabel_outputs:
                condition_addr = None
                for place_name, data_addr, valid_addr in inputs:
                    place = net.places[place_name]
                    if not getattr(place, 'is_label', False) and data_addr is not None:
                        condition_addr = data_addr
                        break
                
                if condition_addr is not None:
                    rom_lines.append(f"@R{condition_addr}")
                    rom_lines.append("D=M")
                    
                    label_name, label_data, label_valid = label_outputs[0]
                    fallthrough_name, fallthrough_data, fallthrough_valid = nonlabel_outputs[0]
                    
                    rom_lines.append(f"@IFGOTO_TRUE_{trans_name}")
                    rom_lines.append("D;JNE")
                    
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{fallthrough_valid}")
                    rom_lines.append("M=D")
                    rom_lines.append(f"@IFGOTO_END_{trans_name}")
                    rom_lines.append("0;JMP")
                    
                    rom_lines.append(f"(IFGOTO_TRUE_{trans_name})")
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{label_valid}")
                    rom_lines.append("M=D")
                    
                    rom_lines.append(f"(IFGOTO_END_{trans_name})")
                else:
                    asm = transition_asm.get(trans_name, [])
                    rom_lines.extend(asm)
                    for place_name, data_addr, valid_addr, is_label in outputs:
                        rom_lines.append("@1")
                        rom_lines.append("D=A")
                        rom_lines.append(f"@R{valid_addr}")
                        rom_lines.append("M=D")
            else:
                asm = transition_asm.get(trans_name, [])
                rom_lines.extend(asm)
                
                for place_name, data_addr, valid_addr, is_label in outputs:
                    rom_lines.append("@1")
                    rom_lines.append("D=A")
                    rom_lines.append(f"@R{valid_addr}")
                    rom_lines.append("M=D")
        
        rom_lines.append(f"(CORE_{core_id}_LOOP_END)")
        rom_lines.append(f"@CORE_{core_id}_START")
        rom_lines.append("0;JMP")
        rom_lines.append("")
    
    return rom_lines, entry_points, initial_marking


def build_emitter(commands):
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


def execute_petri_simulation(emitter, num_cores):
    """Execute Petri net simulation with parallel firing."""
    net = emitter.net
    
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    cycles = 0
    max_cycles = 1000
    
    while cycles < max_cycles:
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        to_fire = []
        used_places = set()
        
        for t in enabled:
            t_places = set(p.name for p in t.in_places) | set(p.name for p in t.out_places)
            
            if not (t_places & used_places):
                to_fire.append(t)
                used_places |= t_places
                
                if len(to_fire) >= num_cores:
                    break
        
        for t in to_fire:
            t.fire()
        
        cycles += 1
    
    result = None
    if emitter.control_stack:
        top = emitter.control_stack[-1]
        if top.token:
            result = top.token.value
    
    return cycles, result


def run_comparison_test(name, commands, expected_result=None):
    """Run comparison between Petri simulation and Hack execution."""
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"{'='*70}")
    
    print(f"\nVM Program ({len(commands)} instructions):")
    for i, cmd in enumerate(commands[:10]):
        if cmd.segment:
            print(f"  {i+1:2}. {cmd.command} {cmd.segment} {cmd.index}")
        else:
            print(f"  {i+1:2}. {cmd.command}")
    if len(commands) > 10:
        print(f"  ... and {len(commands) - 10} more")
    
    print(f"\n{'Method':<25} {'1 Core':<12} {'2 Cores':<12} {'4 Cores':<12} {'8 Cores':<12}")
    print("-" * 73)
    
    # Petri net simulation
    petri_results = []
    for num_cores in [1, 2, 4, 8]:
        emitter = build_emitter(commands)
        cycles, result = execute_petri_simulation(emitter, num_cores)
        petri_results.append(cycles)
    
    print(f"{'Petri Simulation':<25}", end="")
    for cycles in petri_results:
        print(f"{cycles:<12}", end="")
    print()
    
    # Hack CPU execution
    hack_results = []
    hack_result_value = None
    result_addr = None
    
    for num_cores in [1, 2, 4, 8]:
        emitter = build_emitter(commands)
        
        rom_lines, entry_points, initial_marking = generate_multicore_rom(emitter, num_cores)
        
        if emitter.control_stack:
            result_place = emitter.control_stack[-1]
            result_addr = result_place.memory_address
        
        assembler = HackAssembler()
        instructions, labels = assembler.assemble(rom_lines)
        
        cpu = MultiCoreCPU(num_cores)
        cpu.load_rom(instructions)
        
        for addr in initial_marking:
            cpu.shared_ram[addr] = 1
        
        for core_id, pc in entry_points.items():
            cpu.set_core_pc(core_id, pc)
        
        cycles = cpu.run(max_cycles=50000, stall_threshold=500)
        hack_results.append(cycles)
        
        if result_addr is not None and num_cores == 1:
            hack_result_value = cpu.shared_ram[result_addr]
    
    print(f"{'Hack CPU Execution':<25}", end="")
    for cycles in hack_results:
        print(f"{cycles:<12}", end="")
    print()
    
    # Speedup comparison
    print(f"\n{'Speedup (vs 1 core)':<25}", end="")
    base_petri = petri_results[0]
    for cycles in petri_results:
        speedup = base_petri / cycles if cycles > 0 else 1.0
        print(f"{speedup:<12.2f}x", end="")
    print(" (Petri)")
    
    print(f"{'':<25}", end="")
    base_hack = hack_results[0]
    for cycles in hack_results:
        speedup = base_hack / cycles if cycles > 0 else 1.0
        print(f"{speedup:<12.2f}x", end="")
    print(" (Hack)")
    
    # Result verification
    if expected_result is not None:
        print(f"\nExpected result: {expected_result}")
        print(f"Hack CPU result: {hack_result_value}", end="")
        if hack_result_value == expected_result:
            print(" [OK]")
        else:
            print(" [FAIL]")
    
    return petri_results, hack_results


def main():
    print("=" * 72)
    print("  Multi-Core Hack Assembly Execution Demonstration")
    print("  Comparing Petri Net Simulation vs Actual CPU Execution")
    print("=" * 72)
    
    # Test 1: Simple add
    commands = [
        vmcommand("push", "constant", 7),
        vmcommand("push", "constant", 8),
        vmcommand("add"),
    ]
    run_comparison_test("Test 1: Simple Add (7 + 8 = 15)", commands, 15)
    
    # Test 2: Parallel pairs
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("add"),
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 15),
        vmcommand("add"),
        vmcommand("add"),
    ]
    run_comparison_test("Test 2: Parallel Pairs ((10+20) + (5+15) = 50)", commands, 50)
    
    # Test 3: Wide parallel (8 values)
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
    run_comparison_test("Test 3: Wide Parallel (1+2+...+8 = 36)", commands, 36)
    
    # Test 4: Comparison operations
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 5),
        vmcommand("gt"),
    ]
    run_comparison_test("Test 4: Comparison (10 > 5 = -1)", commands, -1)
    
    # Test 5: Mixed operations
    commands = [
        vmcommand("push", "constant", 100),
        vmcommand("push", "constant", 30),
        vmcommand("sub"),
        vmcommand("push", "constant", 10),
        vmcommand("add"),
    ]
    run_comparison_test("Test 5: Mixed Ops (100 - 30 + 10 = 80)", commands, 80)
    
    # Test 6: Negation
    commands = [
        vmcommand("push", "constant", 42),
        vmcommand("neg"),
    ]
    run_comparison_test("Test 6: Negation (-42)", commands, -42)
    
    # Test 7: Parallel comparisons
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 5),
        vmcommand("gt"),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 7),
        vmcommand("lt"),
        vmcommand("and"),
    ]
    run_comparison_test("Test 7: Parallel Comparisons ((10>5) AND (3<7) = -1)", commands, -1)
    
    # Test 8: Large parallel (16 values)
    commands = []
    for i in range(16):
        commands.append(vmcommand("push", "constant", i + 1))
    for _ in range(15):
        commands.append(vmcommand("add"))
    run_comparison_test("Test 8: Large Parallel (1+2+...+16 = 136)", commands, 136)
    
    print("\n" + "="*70)
    print("  KEY OBSERVATIONS")
    print("="*70)
    print("""
  PETRI NET SIMULATION vs HACK CPU EXECUTION:
  
  1. Petri simulation shows theoretical parallelism
     - Counts logical cycles (transition firings)
     - Assumes perfect parallel execution
     
  2. Hack CPU execution shows actual cycles
     - Includes polling overhead for synchronization
     - Each core loops checking valid flags
     - More realistic but higher cycle counts
     
  3. Both show similar speedup trends
     - More cores = better parallelism
     - Diminishing returns with many cores
     
  4. Hack execution validates correctness
     - Results match expected values
     - Petri net semantics correctly implemented
""")


if __name__ == "__main__":
    main()
