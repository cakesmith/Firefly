#!/usr/bin/env python3
"""
Multicore Speedup Demo
======================
Demonstrates parallel speedup on real-world computational patterns:
- Signal processing (FFT-like butterfly operations)
- Graphics (color channel processing)
- Scientific computing (matrix operations, reductions)
- Game physics (collision detection, particle systems)

Architecture:
- SHARED ROM: Single instruction memory, each core has its own PC
- SHARED RAM: All cores read/write same memory with arbitration
- Event-driven execution: transitions fire when inputs ready
"""

import sys
import os
import tempfile
import shutil
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from CPU import CPU


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
        self.instructions_per_core = {i: 0 for i in range(num_cores)}
    
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
            result = self._execute_instruction(cpu, instruction)
            
            if result['should_jump']:
                new_pc = result['jump_target']
                if new_pc == pc - 1:
                    self.core_halted[core_id] = True
                else:
                    self.core_pcs[core_id] = new_pc
            else:
                self.core_pcs[core_id] = pc + 1
            
            self.instructions_per_core[core_id] += 1
            any_executed = True
        
        if any_executed:
            self.total_cycles += 1
        return any_executed
    
    def _execute_instruction(self, cpu: CPU, instruction: dict) -> dict:
        result = {'should_jump': False, 'jump_target': None}
        
        if instruction["TYPE"] == "A_COMMAND":
            cpu.A = instruction["VAL"]
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
            
            if 'M' in dest:
                addr = cpu.A
                if 0 <= addr < len(self.shared_ram):
                    self.shared_ram[addr] = comp_result
            if 'A' in dest:
                cpu.A = comp_result
            if 'D' in dest:
                cpu.D = comp_result
            
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
    
    def run(self, max_cycles: int = 100000) -> int:
        while self.total_cycles < max_cycles:
            if not self.execute_cycle():
                break
            if all(self.core_halted):
                break
        return self.total_cycles


class SharedMemory:
    def __init__(self):
        self.ram = [0] * 32768
        self.ram[0] = 256
    
    def read(self, addr):
        return self.ram[addr] if 0 <= addr < len(self.ram) else 0
    
    def write(self, addr, value):
        if 0 <= addr < len(self.ram):
            self.ram[addr] = value & 0xFFFF


def compile_and_run(jack_source: str, num_cores: int) -> int:
    """Compile Jack to assembly and run on multicore CPU."""
    temp_dir = tempfile.mkdtemp()
    
    try:
        jack_file = os.path.join(temp_dir, "Main.jack")
        with open(jack_file, 'w') as f:
            f.write(jack_source)
        
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        memory = SharedMemory()
        parser = VMParser(temp_dir, memory_read_callback=memory.read,
                         memory_write_callback=memory.write)
        
        emitter = parser.emitter
        net = emitter.net
        net.allocate_memory(verbose=False)
        net.assign_cpu_cores(num_cores, verbose=False)
        
        rom_lines, entry_points, initial_valid, initial_counters = net.generate_shared_rom()
        
        assembler = HackAssembler()
        instructions, _ = assembler.assemble(rom_lines)
        
        cpu = MultiCoreCPU(num_cores)
        cpu.load_rom(instructions)
        
        for addr in initial_valid:
            cpu.shared_ram[addr] = 1
        for addr, count in initial_counters:
            cpu.shared_ram[addr] = count
        
        for core_id, pc in entry_points.items():
            cpu.set_core_pc(core_id, pc)
        
        return cpu.run(max_cycles=500000)
    finally:
        shutil.rmtree(temp_dir)


# =============================================================================
# BENCHMARK PROGRAMS - Real-world parallel patterns
# =============================================================================

# FFT Butterfly: Core operation in Fast Fourier Transform
# 8 independent butterfly operations (each combines 2 inputs)
FFT_BUTTERFLY = '''
class Main {
    static int y0, y1, y2, y3, y4, y5, y6, y7;
    function void main() {
        // 8 parallel butterfly operations: y = (a+b) + (c-d) style
        let y0 = ((10+20) + (30+40)) + ((50+60) + (70+80));
        let y1 = ((11+21) + (31+41)) + ((51+61) + (71+81));
        let y2 = ((12+22) + (32+42)) + ((52+62) + (72+82));
        let y3 = ((13+23) + (33+43)) + ((53+63) + (73+83));
        let y4 = ((14+24) + (34+44)) + ((54+64) + (74+84));
        let y5 = ((15+25) + (35+45)) + ((55+65) + (75+85));
        let y6 = ((16+26) + (36+46)) + ((56+66) + (76+86));
        let y7 = ((17+27) + (37+47)) + ((57+67) + (77+87));
        return;
    }
}
'''

# RGB Color Processing: Process 4 pixels, each with R+G+B channels
COLOR_PROCESS = '''
class Main {
    static int p0, p1, p2, p3;
    function void main() {
        // 4 pixels: combine RGB channels with weights
        let p0 = (((100+50)+(25+10)) + ((200+100)+(50+25))) + (((150+75)+(37+18)) + ((175+87)+(43+21)));
        let p1 = (((110+55)+(27+11)) + ((210+105)+(52+26))) + (((160+80)+(40+20)) + ((185+92)+(46+23)));
        let p2 = (((120+60)+(30+12)) + ((220+110)+(55+27))) + (((170+85)+(42+21)) + ((195+97)+(48+24)));
        let p3 = (((130+65)+(32+13)) + ((230+115)+(57+28))) + (((180+90)+(45+22)) + ((205+102)+(51+25)));
        return;
    }
}
'''

# Matrix Multiply Row: Compute 4 elements of result row (dot products)
MATRIX_ROW = '''
class Main {
    static int c0, c1, c2, c3;
    function void main() {
        // 4 dot products for one row of matrix multiply
        let c0 = (((1+5)+(2+6))+((3+7)+(4+8))) + (((9+13)+(10+14))+((11+15)+(12+16)));
        let c1 = (((1+6)+(2+7))+((3+8)+(4+9))) + (((9+14)+(10+15))+((11+16)+(12+17)));
        let c2 = (((1+7)+(2+8))+((3+9)+(4+10))) + (((9+15)+(10+16))+((11+17)+(12+18)));
        let c3 = (((1+8)+(2+9))+((3+10)+(4+11))) + (((9+16)+(10+17))+((11+18)+(12+19)));
        return;
    }
}
'''

# Parallel Reduction: Sum 32 values using tree reduction
TREE_REDUCE_32 = '''
class Main {
    static int sum;
    function void main() {
        // 32->16->8->4->2->1 parallel reduction
        let sum = 
            ((((1+2)+(3+4))+((5+6)+(7+8)))+(((9+10)+(11+12))+((13+14)+(15+16)))) +
            ((((17+18)+(19+20))+((21+22)+(23+24)))+(((25+26)+(27+28))+((29+30)+(31+32))));
        return;
    }
}
'''

# Physics: 6 independent force calculations
PHYSICS_FORCES = '''
class Main {
    static int f1, f2, f3, f4, f5, f6;
    function void main() {
        // 6 force vectors: each is sum of component forces
        let f1 = (((10+20)+(30+40))+((50+60)+(70+80))) + (((5+10)+(15+20))+((25+30)+(35+40)));
        let f2 = (((11+21)+(31+41))+((51+61)+(71+81))) + (((6+11)+(16+21))+((26+31)+(36+41)));
        let f3 = (((12+22)+(32+42))+((52+62)+(72+82))) + (((7+12)+(17+22))+((27+32)+(37+42)));
        let f4 = (((13+23)+(33+43))+((53+63)+(73+83))) + (((8+13)+(18+23))+((28+33)+(38+43)));
        let f5 = (((14+24)+(34+44))+((54+64)+(74+84))) + (((9+14)+(19+24))+((29+34)+(39+44)));
        let f6 = (((15+25)+(35+45))+((55+65)+(75+85))) + (((10+15)+(20+25))+((30+35)+(40+45)));
        return;
    }
}
'''

# Neural Network Layer: 4 neurons, each sums 8 weighted inputs
NEURAL_LAYER = '''
class Main {
    static int n1, n2, n3, n4;
    function void main() {
        // 4 neurons computing weighted sums
        let n1 = ((((1+10)+(2+20))+((3+30)+(4+40)))+(((5+50)+(6+60))+((7+70)+(8+80)))) + 100;
        let n2 = ((((2+11)+(3+21))+((4+31)+(5+41)))+(((6+51)+(7+61))+((8+71)+(9+81)))) + 100;
        let n3 = ((((3+12)+(4+22))+((5+32)+(6+42)))+(((7+52)+(8+62))+((9+72)+(10+82)))) + 100;
        let n4 = ((((4+13)+(5+23))+((6+33)+(7+43)))+(((8+53)+(9+63))+((10+73)+(11+83)))) + 100;
        return;
    }
}
'''

# Convolution: 4 output pixels from 3x3 kernel
CONVOLUTION = '''
class Main {
    static int out1, out2, out3, out4;
    function void main() {
        // 4 convolution outputs (simplified 3x3 kernel sums)
        let out1 = ((((1+2)+(3+4))+((5+6)+(7+8)))+((9+10)+(11+12))) + (((13+14)+(15+16))+((17+18)+(19+20)));
        let out2 = ((((2+3)+(4+5))+((6+7)+(8+9)))+((10+11)+(12+13))) + (((14+15)+(16+17))+((18+19)+(20+21)));
        let out3 = ((((3+4)+(5+6))+((7+8)+(9+10)))+((11+12)+(13+14))) + (((15+16)+(17+18))+((19+20)+(21+22)));
        let out4 = ((((4+5)+(6+7))+((8+9)+(10+11)))+((12+13)+(14+15))) + (((16+17)+(18+19))+((20+21)+(22+23)));
        return;
    }
}
'''

# Crypto Hash Round: 8 parallel mixing operations
HASH_MIX = '''
class Main {
    static int h0, h1, h2, h3, h4, h5, h6, h7;
    function void main() {
        // 8 parallel hash state updates
        let h0 = (((100+200)+(300+400))+((500+600)+(700+800))) + (((10+20)+(30+40))+((50+60)+(70+80)));
        let h1 = (((101+201)+(301+401))+((501+601)+(701+801))) + (((11+21)+(31+41))+((51+61)+(71+81)));
        let h2 = (((102+202)+(302+402))+((502+602)+(702+802))) + (((12+22)+(32+42))+((52+62)+(72+82)));
        let h3 = (((103+203)+(303+403))+((503+603)+(703+803))) + (((13+23)+(33+43))+((53+63)+(73+83)));
        let h4 = (((104+204)+(304+404))+((504+604)+(704+804))) + (((14+24)+(34+44))+((54+64)+(74+84)));
        let h5 = (((105+205)+(305+405))+((505+605)+(705+805))) + (((15+25)+(35+45))+((55+65)+(75+85)));
        let h6 = (((106+206)+(306+406))+((506+606)+(706+806))) + (((16+26)+(36+46))+((56+66)+(76+86)));
        let h7 = (((107+207)+(307+407))+((507+607)+(707+807))) + (((17+27)+(37+47))+((57+67)+(77+87)));
        return;
    }
}
'''


def run_benchmark(name: str, jack_source: str, description: str):
    """Run a benchmark and report speedup."""
    print(f"\n{'─'*70}")
    print(f"  {name}")
    print(f"  {description}")
    print(f"{'─'*70}")
    
    results = {}
    base_cycles = None
    
    for cores in [1, 2, 4, 8]:
        cycles = compile_and_run(jack_source, cores)
        if base_cycles is None:
            base_cycles = cycles
        
        speedup = base_cycles / cycles if cycles > 0 else 1.0
        efficiency = (speedup / cores) * 100
        results[cores] = (cycles, speedup, efficiency)
    
    print(f"\n  {'Cores':<8} {'Cycles':<12} {'Speedup':<12} {'Efficiency':<12}")
    print(f"  {'─'*44}")
    
    for cores in [1, 2, 4, 8]:
        cycles, speedup, efficiency = results[cores]
        marker = ""
        if efficiency >= 90:
            marker = " ★ linear"
        elif efficiency >= 70:
            marker = " ✓ good"
        elif speedup > 1.0:
            marker = ""
        print(f"  {cores:<8} {cycles:<12} {speedup:<12.2f}x {efficiency:>5.0f}%{marker}")
    
    return results


def main():
    print("=" * 70)
    print("  MULTICORE SPEEDUP DEMONSTRATION")
    print("  Petri Net → Assembly → Parallel Execution")
    print("=" * 70)
    print("""
  This demo shows parallel speedup on real computational patterns.
  Each benchmark runs the same Jack program on 1, 2, 4, and 8 cores.
  
  Architecture:
  • Shared ROM with per-core program counters
  • Shared RAM with memory arbitration  
  • Event-driven execution (no polling overhead)
""")
    
    benchmarks = [
        ("FFT Butterfly", FFT_BUTTERFLY, "8 parallel butterfly operations"),
        ("RGB Processing", COLOR_PROCESS, "4 pixels × RGB channel mixing"),
        ("Matrix Row", MATRIX_ROW, "4 dot products (matrix multiply)"),
        ("Tree Reduce 32", TREE_REDUCE_32, "32→1 parallel reduction"),
        ("Physics Forces", PHYSICS_FORCES, "6 force vector calculations"),
        ("Neural Layer", NEURAL_LAYER, "4 neurons × 8 weighted inputs"),
        ("Convolution", CONVOLUTION, "4 output pixels, 3×3 kernel"),
        ("Hash Mixing", HASH_MIX, "8 parallel hash state updates"),
    ]
    
    all_results = {}
    for name, source, desc in benchmarks:
        all_results[name] = run_benchmark(name, source, desc)
    
    # Summary
    print("\n" + "=" * 70)
    print("  SPEEDUP SUMMARY")
    print("=" * 70)
    
    print(f"\n  {'Benchmark':<20} {'2-Core':<14} {'4-Core':<14} {'8-Core':<14}")
    print(f"  {'─'*56}")
    
    for name in all_results:
        r = all_results[name]
        s2 = f"{r[2][1]:.2f}x ({r[2][2]:.0f}%)"
        s4 = f"{r[4][1]:.2f}x ({r[4][2]:.0f}%)"
        s8 = f"{r[8][1]:.2f}x ({r[8][2]:.0f}%)"
        print(f"  {name:<20} {s2:<14} {s4:<14} {s8:<14}")
    
    # Best results
    print(f"\n  {'─'*56}")
    best_8 = max(all_results.items(), key=lambda x: x[1][8][1])
    best_eff = max(all_results.items(), key=lambda x: x[1][4][2])
    print(f"  Best 8-core speedup: {best_8[0]} ({best_8[1][8][1]:.2f}x)")
    print(f"  Best 4-core efficiency: {best_eff[0]} ({best_eff[1][4][2]:.0f}%)")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
