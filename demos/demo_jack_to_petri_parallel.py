#!/usr/bin/env python3
"""
Jack to Petri Net to Multicore Assembly Demo
=============================================
Complete pipeline demonstrating parallel execution:
1. Jack source code (real-world examples)
2. Compiled to VM code via JackCompiler
3. VM code -> PetriEmitter -> Petri net
4. Memory allocation & core assignment
5. Assembly generation (shared ROM, per-core PCs)
6. Multicore simulation with shared RAM + arbitration

Architecture:
- SHARED ROM: Single instruction memory, each core has its own PC
- SHARED RAM: All cores read/write same memory with conflict detection
- Per-core state: PC, A register, D register
"""

import sys
import os
import tempfile
import shutil
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from Petri.Token import Token
from CPU import CPU


class SharedMemory:
    """Shared memory for VM execution."""
    def __init__(self):
        self.ram = [0] * 32768
        self.ram[0] = 256
        self.ram[1] = 300
        self.ram[2] = 400
        self.ram[3] = 3000
        self.ram[4] = 3010
        self.ram[2048] = 14334
        self.ram[2049] = 2050
    
    def read(self, addr):
        return self.ram[addr] if 0 <= addr < len(self.ram) else 0
    
    def write(self, addr, value):
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value & 0xFFFF


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
            if not line or line.startswith('//') or line.startswith('('):
                continue
            if '//' in line:
                line = line.split('//')[0].strip()
            if not line:
                continue
            
            if line.startswith('@'):
                value_str = line[1:]
                if value_str.isdigit() or value_str.lstrip('-').isdigit():
                    value = int(value_str)
                elif value_str.startswith('R') and value_str[1:].isdigit():
                    value = int(value_str[1:])
                elif value_str in self.symbol_table:
                    value = self.symbol_table[value_str]
                else:
                    self.symbol_table[value_str] = next_var_address
                    value = next_var_address
                    next_var_address += 1
                instructions.append({"TYPE": "A_COMMAND", "VAL": value})
            else:
                dest, comp, jump = "", line, ""
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
                    "VAL": {"DEST": dest, "COMP": comp, "JUMP": jump}
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
        
        self.stats = ExecutionStats()
        self.stats.instructions_executed = {i: 0 for i in range(num_cores)}
        self.cycle_writes: Set[int] = set()
        self.cycle_reads: Set[int] = set()
    
    def load_rom(self, instructions: List[dict]):
        self.shared_rom = instructions
    
    def set_core_pc(self, core_id: int, pc: int):
        if 0 <= core_id < self.num_cores:
            self.core_pcs[core_id] = pc
            self.cores[core_id].PC = pc
    
    def execute_cycle(self) -> bool:
        """Execute one cycle on all cores simultaneously."""
        self.cycle_writes.clear()
        self.cycle_reads.clear()
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
            
            self.stats.instructions_executed[core_id] += 1
            any_executed = True
        
        if any_executed:
            self.stats.total_cycles += 1
        return any_executed

    
    def _execute_instruction(self, core_id: int, cpu: CPU, instruction: dict) -> dict:
        result = {'should_jump': False, 'jump_target': None, 'value': None}
        
        if instruction["TYPE"] == "A_COMMAND":
            cpu.A = instruction["VAL"]
            result['value'] = cpu.A
        elif instruction["TYPE"] == "C_COMMAND":
            dest = instruction["VAL"]["DEST"]
            comp = instruction["VAL"]["COMP"]
            jump = instruction["VAL"]["JUMP"]
            
            if 'M' in comp:
                addr = cpu.A
                self.stats.memory_reads += 1
                if addr in self.cycle_writes:
                    self.stats.conflicts += 1
                self.cycle_reads.add(addr)
                mem_val = self.shared_ram[addr] if 0 <= addr < len(self.shared_ram) else 0
                comp_result = cpu.ALU[comp.replace("M", "A")](mem_val, cpu.D)
            else:
                comp_result = cpu.ALU[comp](cpu.A, cpu.D)
            
            cpu.zr = 1 if comp_result == 0 else 0
            cpu.ng = 1 if comp_result < 0 else 0
            
            if 'M' in dest:
                addr = cpu.A
                self.stats.memory_writes += 1
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
    
    def run(self, max_cycles: int = 50000) -> ExecutionStats:
        """Run until all cores halt or max cycles reached."""
        while self.stats.total_cycles < max_cycles:
            if not self.execute_cycle():
                break
            if all(self.core_halted):
                break
        return self.stats


def generate_multicore_rom(emitter, num_cores: int) -> Tuple[List[str], Dict[int, int], List[int], List[Tuple[int, int]]]:
    """
    Generate unified ROM using net.py's generate_shared_rom method.
    Returns (rom_lines, entry_points, initial_valid_flags, initial_counters)
    """
    net = emitter.net
    net.allocate_memory(verbose=False)
    net.assign_cpu_cores(num_cores, verbose=False)
    
    # Use the net.py method
    return net.generate_shared_rom()


# Jack source code - examples designed for parallel execution
# Key insight: nested expressions create parallel data dependencies
# Sequential let statements create control flow dependencies

JACK_PARALLEL_SUMS_8 = '''
class Main {
    static int r1, r2, r3, r4, r5, r6, r7, r8;
    function void main() {
        // 8 independent complex sums - each is ((a+b)+(c+d))
        // All 8 can compute in parallel at each level
        let r1 = ((1+2)+(3+4)) + ((5+6)+(7+8));
        let r2 = ((10+20)+(30+40)) + ((50+60)+(70+80));
        let r3 = ((11+22)+(33+44)) + ((55+66)+(77+88));
        let r4 = ((12+23)+(34+45)) + ((56+67)+(78+89));
        let r5 = ((13+24)+(35+46)) + ((57+68)+(79+90));
        let r6 = ((14+25)+(36+47)) + ((58+69)+(80+91));
        let r7 = ((15+26)+(37+48)) + ((59+70)+(81+92));
        let r8 = ((16+27)+(38+49)) + ((60+71)+(82+93));
        return;
    }
}
'''

JACK_PARALLEL_SUMS_4 = '''
class Main {
    static int r1, r2, r3, r4;
    function void main() {
        // 4 independent deep sums - more operations per result
        let r1 = (((1+2)+(3+4))+((5+6)+(7+8))) + (((9+10)+(11+12))+((13+14)+(15+16)));
        let r2 = (((17+18)+(19+20))+((21+22)+(23+24))) + (((25+26)+(27+28))+((29+30)+(31+32)));
        let r3 = (((33+34)+(35+36))+((37+38)+(39+40))) + (((41+42)+(43+44))+((45+46)+(47+48)));
        let r4 = (((49+50)+(51+52))+((53+54)+(55+56))) + (((57+58)+(59+60))+((61+62)+(63+64)));
        return;
    }
}
'''

JACK_TREE_REDUCE_16 = '''
class Main {
    static int result;
    function void main() {
        // Single deep tree: 16 leaves -> 1 result
        // Level 1: 8 parallel adds, Level 2: 4 parallel, Level 3: 2 parallel, Level 4: 1
        let result = 
            (((1+2)+(3+4))+((5+6)+(7+8))) + 
            (((9+10)+(11+12))+((13+14)+(15+16)));
        return;
    }
}
'''

JACK_WIDE_TREE = '''
class Main {
    static int a, b, c, d, e, f, g, h;
    function void main() {
        // 8 independent binary trees
        let a = (1+2) + (3+4);
        let b = (5+6) + (7+8);
        let c = (9+10) + (11+12);
        let d = (13+14) + (15+16);
        let e = (17+18) + (19+20);
        let f = (21+22) + (23+24);
        let g = (25+26) + (27+28);
        let h = (29+30) + (31+32);
        return;
    }
}
'''

JACK_DOT_PRODUCTS = '''
class Main {
    static int dot1, dot2, dot3, dot4;
    function void main() {
        // 4 independent dot products (sum of element-wise products as additions)
        let dot1 = ((1+5) + (2+6)) + ((3+7) + (4+8));
        let dot2 = ((2+6) + (3+7)) + ((4+8) + (5+9));
        let dot3 = ((1+1) + (2+2)) + ((3+3) + (4+4));
        let dot4 = ((3+2) + (3+2)) + ((3+2) + (3+2));
        return;
    }
}
'''

JACK_MATRIX_TRACE = '''
class Main {
    static int trace1, trace2, trace3, trace4;
    function void main() {
        // 4 independent matrix trace computations (sum of diagonal)
        let trace1 = ((11+22)+(33+44)) + ((55+66)+(77+88));
        let trace2 = ((10+20)+(30+40)) + ((50+60)+(70+80));
        let trace3 = ((12+24)+(36+48)) + ((60+72)+(84+96));
        let trace4 = ((15+30)+(45+60)) + ((75+90)+(105+120));
        return;
    }
}
'''


def compile_jack_to_petri(jack_source, class_name="Main"):
    """Compile Jack source to Petri net through the full pipeline."""
    temp_dir = tempfile.mkdtemp(prefix="jack_parallel_")
    
    try:
        jack_file = os.path.join(temp_dir, f"{class_name}.jack")
        with open(jack_file, 'w') as f:
            f.write(jack_source)
        
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        # Note: Not including OS files - Jack compiler handles Math.multiply inline
        
        vm_file = os.path.join(temp_dir, f"{class_name}.vm")
        with open(vm_file, 'r') as f:
            vm_code = f.read()
        
        memory = SharedMemory()
        parser = VMParser(temp_dir, memory_read_callback=memory.read, 
                         memory_write_callback=memory.write)
        
        return parser.emitter, vm_code, temp_dir
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e


def execute_petri_sequential(net, max_steps=10000):
    """Execute Petri net sequentially."""
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    steps = 0
    while steps < max_steps:
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        enabled[0].fire()
        steps += 1
    return steps


def execute_petri_parallel(net, num_cores, max_steps=10000):
    """Execute Petri net with parallel firing."""
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    steps = 0
    while steps < max_steps:
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
        steps += 1
    
    return steps


def run_demo(name: str, jack_source: str, description: str):
    """Run complete demo: Jack -> VM -> Petri -> Assembly -> Multicore Execution."""
    print(f"\n{'='*72}")
    print(f"  {name}: {description}")
    print(f"{'='*72}")
    
    try:
        emitter, vm_code, temp_dir = compile_jack_to_petri(jack_source)
    except Exception as e:
        print(f"  ERROR: {e}")
        return None
    
    vm_lines = len([l for l in vm_code.splitlines() if l.strip() and not l.strip().startswith('//')])
    net = emitter.net
    
    print(f"\n  Compilation: {vm_lines} VM -> {len(net.transitions)} transitions, {len(net.places)} places")
    
    # Petri net simulation
    seq_steps = execute_petri_sequential(net, max_steps=50000)
    
    print(f"\n  PETRI NET SIMULATION:")
    print(f"    {'Cores':<6} {'Steps':<10} {'Speedup':<12} {'Efficiency'}")
    print(f"    {'-'*44}")
    
    petri_results = []
    for cores in [1, 2, 4, 8]:
        par_steps = execute_petri_parallel(net, cores, max_steps=50000)
        speedup = seq_steps / par_steps if par_steps > 0 else 1.0
        efficiency = (speedup / cores) * 100
        marker = " <-- linear!" if efficiency >= 90 else ""
        print(f"    {cores:<6} {par_steps:<10} {speedup:<12.2f}x {efficiency:.0f}%{marker}")
        petri_results.append((cores, par_steps, speedup, efficiency))
    
    # Assembly execution
    print(f"\n  ASSEMBLY EXECUTION (Shared ROM + Shared RAM):")
    print(f"    {'Cores':<6} {'Cycles':<10} {'Speedup':<12} {'Efficiency'}")
    print(f"    {'-'*44}")
    
    asm_results = []
    base_cycles = None
    
    for num_cores in [1, 2, 4, 8]:
        emitter2, _, _ = compile_jack_to_petri(jack_source)
        rom_lines, entry_points, initial_valid, initial_counters = generate_multicore_rom(emitter2, num_cores)
        
        assembler = HackAssembler()
        instructions, _ = assembler.assemble(rom_lines)
        
        cpu = MultiCoreCPU(num_cores)
        cpu.load_rom(instructions)
        
        # Set initial valid flags for places with tokens
        for addr in initial_valid:
            cpu.shared_ram[addr] = 1
        
        # Set initial counter values for transitions
        for addr, count in initial_counters:
            cpu.shared_ram[addr] = count
        
        for core_id, pc in entry_points.items():
            cpu.set_core_pc(core_id, pc)
        
        stats = cpu.run(max_cycles=100000)
        
        if base_cycles is None:
            base_cycles = stats.total_cycles
        
        speedup = base_cycles / stats.total_cycles if stats.total_cycles > 0 else 1.0
        efficiency = (speedup / num_cores) * 100
        marker = " <-- linear!" if efficiency >= 90 else ""
        print(f"    {num_cores:<6} {stats.total_cycles:<10} {speedup:<12.2f}x {efficiency:.0f}%{marker}")
        asm_results.append((num_cores, stats.total_cycles, speedup, efficiency))
    
    shutil.rmtree(temp_dir)
    return {'petri': petri_results, 'asm': asm_results}


def main():
    print("=" * 74)
    print("  JACK -> PETRI NET -> MULTICORE ASSEMBLY EXECUTION DEMO")
    print("=" * 74)
    print("""
  Architecture:
    - SHARED ROM: Single instruction memory, each core has its own PC
    - SHARED RAM: All cores read/write same memory with arbitration
    - Petri semantics: Transitions fire when inputs ready & outputs empty
""")
    
    demos = [
        ("8 Parallel Sums", JACK_PARALLEL_SUMS_8, "8 independent 8-element tree sums"),
        ("4 Deep Sums", JACK_PARALLEL_SUMS_4, "4 independent 16-element tree sums"),
        ("Tree Reduce 16", JACK_TREE_REDUCE_16, "single 16->1 reduction tree"),
        ("Wide Tree 8", JACK_WIDE_TREE, "8 independent 4-element trees"),
        ("Dot Products", JACK_DOT_PRODUCTS, "4 independent dot products"),
        ("Matrix Traces", JACK_MATRIX_TRACE, "4 independent 8-element traces"),
    ]
    
    all_results = []
    for name, source, desc in demos:
        results = run_demo(name, source, desc)
        if results:
            all_results.append((name, results))
    
    if all_results:
        print("\n" + "=" * 74)
        print("  SUMMARY")
        print("=" * 74)
        
        print(f"\n  Petri Net Simulation Speedup:")
        print(f"  {'Application':<20} {'2-Core':<12} {'4-Core':<12} {'8-Core'}")
        print(f"  {'-'*56}")
        for name, results in all_results:
            r = results['petri']
            print(f"  {name:<20} {r[1][2]:.2f}x ({r[1][3]:.0f}%)  {r[2][2]:.2f}x ({r[2][3]:.0f}%)  {r[3][2]:.2f}x ({r[3][3]:.0f}%)")
        
        print(f"\n  Assembly Execution Speedup:")
        print(f"  {'Application':<20} {'2-Core':<12} {'4-Core':<12} {'8-Core'}")
        print(f"  {'-'*56}")
        for name, results in all_results:
            r = results['asm']
            print(f"  {name:<20} {r[1][2]:.2f}x ({r[1][3]:.0f}%)  {r[2][2]:.2f}x ({r[2][3]:.0f}%)  {r[3][2]:.2f}x ({r[3][3]:.0f}%)")
    
    print("\n" + "=" * 74)


if __name__ == "__main__":
    main()
