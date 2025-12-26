"""
Assembly Generator for Petri Net VM
Generates multi-core assembly code with distributed coordination
"""

import os

class AssemblyGenerator:
    """
    Generates assembly code for multi-core execution
    Uses unified core generation logic for both single and multi-core cases
    """
    
    def __init__(self, translator):
        self.translator = translator
        
    def generate_multicore_assembly(self, num_cores=1, output_dir="test_results"):
        """
        Analyze the Petri net and generate assembly code for n cores
        Uses unified core generation logic for both single and multi-core cases
        """
        if num_cores < 1:
            raise ValueError("Number of cores must be >= 1")
            
        print(f"\n" + "=" * 60)
        print(f"GENERATING ASSEMBLY FOR {num_cores} CORE(S)")
        print("=" * 60)
        
        # Analyze the network for parallelization opportunities
        execution_plan = self.translator._analyze_execution_dependencies()
        
        # Generate core assignments
        core_assignments = self.translator._assign_operations_to_cores(execution_plan, num_cores)
        memory_map = self.translator._optimize_memory_allocation()
        
        if num_cores == 1:
            # Single core - use same core generation logic but return assembly directly
            operations = core_assignments[0]
            assembly_code = self._generate_core_rom(0, operations, memory_map, num_cores)
            return assembly_code
        else:
            # Multi-core - create separate ROM files for each core
            return self._generate_multicore_roms(core_assignments, num_cores, output_dir)
            
    def _generate_multicore_roms(self, core_assignments, num_cores, output_dir="test_results"):
        """
        Generate separate ROM files for each core in multi-core execution
        Creates a folder with coreX.asm files for each core
        """
        # Create multicore output folder inside the specified directory
        folder_name = os.path.join(output_dir, f"multicore_{num_cores}cores")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        memory_map = self.translator._optimize_memory_allocation()
        
        print(f"Creating {num_cores} separate ROM files in folder: {folder_name}/")
        
        # Generate ROM for each core
        all_roms = {}
        
        for core_id in range(num_cores):
            operations = core_assignments[core_id]
            
            if operations:
                print(f"Core {core_id}: {len(operations)} operations")
                rom_content = self._generate_core_rom(core_id, operations, memory_map, num_cores)
            else:
                print(f"Core {core_id}: No operations (idle core)")
                rom_content = self._generate_idle_core_rom(core_id, num_cores)
            
            # Save ROM file
            rom_filename = f"{folder_name}/core{core_id}.asm"
            with open(rom_filename, 'w') as f:
                f.write('\n'.join(rom_content))
            
            all_roms[core_id] = rom_content
            print(f"  Saved: {rom_filename} ({len(rom_content)} lines)")
        
        # Generate shared memory initialization file
        shared_init = self._generate_shared_memory_init(memory_map, num_cores)
        shared_filename = f"{folder_name}/shared_init.asm"
        with open(shared_filename, 'w') as f:
            f.write('\n'.join(shared_init))
        print(f"  Saved: {shared_filename} (shared memory initialization)")
        
        # Generate coordination protocol documentation
        coord_doc = self._generate_coordination_documentation(core_assignments, num_cores)
        doc_filename = f"{folder_name}/coordination.md"
        with open(doc_filename, 'w') as f:
            f.write(coord_doc)
        print(f"  Saved: {doc_filename} (coordination protocol)")
        
        return all_roms
        
    def _generate_core_rom(self, core_id, operations, memory_map, num_cores):
        """Generate ROM content for a specific core with unified single/multi-core logic"""
        rom_lines = [
            f"// Core {core_id} ROM - Unified Petri-net Execution",
            f"// Generated for {num_cores}-core system",
            f"// Operations: {len(operations)}",
            "//",
        ]
        
        # Add memory layout info
        if num_cores == 1:
            rom_lines.extend([
                f"// Single-core Memory Layout:",
                f"// @0-15: System registers",
                f"// @256+: Optimized place memory",
                f"// @512+: Stack area",
                "//",
                "",
                "// Initialize stack pointer", 
                "@512",  # Use higher stack for consistency
                "D=A",
                "@SP",
                "M=D",
                ""
            ])
        else:
            rom_lines.extend([
                f"// Multi-core Memory Layout:",
                f"// @0-15: System registers",
                f"// @16-31: Core status flags (debugging only)",
                f"// @32-47: Level synchronization area (coordination)", 
                f"// @256+: Optimized place memory",
                f"// @512+: Shared results area",
                "//",
                "",
                f"// Core {core_id} initialization",
                f"@{16 + core_id}",
                "M=0  // Set status to idle (debugging)",
                ""
            ])
        
        # Initialize constants in optimized memory locations (same for both single/multi-core)
        rom_lines.append("// Initialize constants in optimized memory")
        for place_name, place in self.translator.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                rom_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        rom_lines.append("")
        
        # Check if this core has any operations
        if not operations:
            # Idle core - different handling for single vs multi-core
            if num_cores == 1:
                rom_lines.extend([
                    "// No operations to execute",
                    "(END)",
                    "@END", 
                    "0;JMP"
                ])
            else:
                rom_lines.extend([
                    f"(CORE_{core_id}_IDLE)",
                    f"// Core {core_id} has no operations - wait for program completion",
                    f"// Wait for final level completion (distributed termination)",
                    f"@{32 + self._get_final_level(operations)}",  # Final level sync
                    "D=M",
                    f"@{(1 << num_cores) - 1}",  # All cores mask
                    "D=D-A",
                    f"@CORE_{core_id}_TERMINATE",
                    "D;JEQ",  # Final level complete, terminate
                    f"@CORE_{core_id}_IDLE",
                    "0;JMP",  # Keep waiting
                    "",
                    f"(CORE_{core_id}_TERMINATE)",
                    f"// Program complete - core {core_id} self-terminates",
                    f"@{16 + core_id}",
                    "M=2  // Set status to done (debugging)",
                    f"@CORE_{core_id}_HALT",
                    "0;JMP"
                ])
            return rom_lines
        
        # Working core - execute operations
        if num_cores == 1:
            rom_lines.extend([
                f"// Single-core execution begins",
                ""
            ])
        else:
            rom_lines.extend([
                f"(CORE_{core_id}_START)",
                f"// Core {core_id} execution begins",
                f"@{16 + core_id}",
                "M=1  // Set status to working (debugging)",
                ""
            ])
        
        # Group operations by execution level for synchronization
        operations_by_level = {}
        for op_info in operations:
            level = op_info['level']
            if level not in operations_by_level:
                operations_by_level[level] = []
            operations_by_level[level].append(op_info)
        
        final_level = max(operations_by_level.keys()) if operations_by_level else 0
        
        # Generate code for each level - simplified for single-core
        for level in sorted(operations_by_level.keys()):
            level_ops = operations_by_level[level]
            
            rom_lines.extend([
                f"// === Level {level} Operations ===",
            ])
            
            # Level barrier synchronization (only for multi-core)
            if num_cores > 1:
                rom_lines.extend([
                    f"// Level-based barrier synchronization",
                    f"(LEVEL_{level}_BARRIER)",
                    f"// Signal ready for level {level}",
                    f"@{32 + level}",  # Sync area for this level
                    "D=M",
                    f"@{1 << core_id}",  # Set bit for this core
                    "D=D|A",
                    f"@{32 + level}",
                    "M=D",
                    "",
                    f"// Wait for all cores ready at level {level}",
                    f"(LEVEL_{level}_WAIT)",
                    f"@{32 + level}",
                    "D=M",
                    f"@{self._get_active_cores_mask(num_cores)}",  # Only active cores
                    "D=D-A",
                    f"@LEVEL_{level}_EXECUTE",
                    "D;JEQ",  # All active cores ready, proceed
                    f"@LEVEL_{level}_WAIT",
                    "0;JMP",  # Keep waiting
                    "",
                    f"(LEVEL_{level}_EXECUTE)"
                ])
            
            # Execute operations for this level (same logic for single/multi-core)
            for op_info in level_ops:
                operation = op_info['operation']
                transition = op_info['transition']
                
                rom_lines.extend([
                    f"// Operation: {operation}",
                ])
                
                if num_cores > 1:
                    rom_lines.append(f"// Core {core_id} executing {operation}")
                
                # Generate memory-optimized operation code (unified logic)
                op_code = self._generate_core_operation_code(operation, transition, memory_map)
                rom_lines.extend(op_code)
                rom_lines.append("")
        
        # Termination logic - different for single vs multi-core
        if num_cores == 1:
            # Single-core: push results to stack and terminate
            rom_lines.extend([
                "// Push final results onto stack"
            ])
            
            for place in self.translator.result_places:
                if place.name in memory_map['location_map']:
                    memory_loc = memory_map['location_map'][place.name]
                    rom_lines.extend([
                        f"// Push result from @{memory_loc}",
                        f"@{memory_loc}",
                        "D=M",
                        "@SP",
                        "M=M+1",
                        "A=M-1",
                        "M=D"
                    ])
                    
            rom_lines.extend([
                "//",
                "// End of program",
                "(END)",
                "@END", 
                "0;JMP"
            ])
        else:
            # Multi-core: distributed termination
            rom_lines.extend([
                f"// Distributed termination - final level barrier IS completion detection",
                f"// Core {core_id} completed all operations",
                f"@{16 + core_id}",
                "M=2  // Set status to done (debugging)",
                "",
                f"// Wait for final level completion (level {final_level})",
                f"(FINAL_BARRIER_WAIT)",
                f"@{32 + final_level}",
                "D=M", 
                f"@{self._get_active_cores_mask(num_cores)}",  # All active cores mask
                "D=D-A",
                f"@CORE_{core_id}_TERMINATE",
                "D;JEQ",  # All cores finished final level
                f"@FINAL_BARRIER_WAIT",
                "0;JMP",  # Keep waiting
                "",
                f"(CORE_{core_id}_TERMINATE)",
                f"// Program complete - core {core_id} self-terminates",
                f"(CORE_{core_id}_HALT)",
                f"@CORE_{core_id}_HALT",
                "0;JMP  // Halt core"
            ])
        
        return rom_lines
        
    def _get_final_level(self, operations):
        """Get the final execution level from operations"""
        if not operations:
            # For idle cores, we need to determine the final level from the overall execution plan
            execution_plan = self.translator._analyze_execution_dependencies()
            return len(execution_plan['execution_levels']) - 1 if execution_plan['execution_levels'] else 0
        return max(op['level'] for op in operations)
    
    def _get_active_cores_mask(self, num_cores):
        """Get the mask for cores that actually have work assigned"""
        # For now, assume all cores are active (this could be optimized)
        # In a more sophisticated implementation, we'd track which cores have operations
        return (1 << num_cores) - 1
        
    def _generate_idle_core_rom(self, core_id, num_cores):
        """Generate ROM for cores with no operations assigned"""
        return [
            f"// Core {core_id} ROM - Idle Core",
            f"// No operations assigned in {num_cores}-core system",
            "//",
            f"@{16 + core_id}",
            "M=0  // Set status to idle",
            "",
            f"(CORE_{core_id}_IDLE)",
            "// Idle loop - could be used for other tasks",
            f"@CORE_{core_id}_IDLE", 
            "0;JMP"
        ]
        
    def _generate_core_operation_code(self, operation, transition, memory_map):
        """Generate assembly code for a specific operation on a core"""
        if not transition:
            return [f"// Placeholder operation: {operation}"]
            
        op_type = operation.split('_')[0]
        code_lines = []
        
        if op_type in ['add', 'sub', 'mul', 'div', 'and', 'or', 'eq', 'lt', 'gt'] and len(transition.in_places) >= 2:
            # Binary operations
            loc_a = memory_map['location_map'][transition.in_places[0].name]
            loc_b = memory_map['location_map'][transition.in_places[1].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Binary operation: {op_type}",
                f"// Load operands from @{loc_a} and @{loc_b}",
                f"@{loc_a}",
                "D=M",
                f"@{loc_b}",
            ])
            
            if op_type == 'add':
                code_lines.append("D=D+M")
            elif op_type == 'sub':
                code_lines.append("D=D-M")
            elif op_type == 'and':
                code_lines.append("D=D&M")
            elif op_type == 'or':
                code_lines.append("D=D|M")
            elif op_type in ['eq', 'lt', 'gt']:
                # Comparison operations
                code_lines.extend([
                    "D=D-M  // Compare",
                    f"@{operation.upper()}_TRUE",
                    f"D;J{op_type.upper()}",
                    "D=0  // False",
                    f"@{operation.upper()}_DONE",
                    "0;JMP",
                    f"({operation.upper()}_TRUE)",
                    "D=-1  // True (-1)",
                    f"({operation.upper()}_DONE)"
                ])
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
            
        elif op_type in ['neg', 'not'] and len(transition.in_places) >= 1:
            # Unary operations
            loc_input = memory_map['location_map'][transition.in_places[0].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Unary operation: {op_type}",
                f"// Load operand from @{loc_input}",
                f"@{loc_input}",
                "D=M",
            ])
            
            if op_type == 'neg':
                code_lines.append("D=-D")
            elif op_type == 'not':
                code_lines.append("D=!D")
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
        
        return code_lines
        
    def _generate_shared_memory_init(self, memory_map, num_cores):
        """Generate shared memory initialization code"""
        init_lines = [
            f"// Shared Memory Initialization for {num_cores}-core system",
            "// Run this before starting any cores",
            "//",
            "// Initialize core status flags to idle",
        ]
        
        for core_id in range(num_cores):
            init_lines.extend([
                f"@{16 + core_id}",
                "M=0  // Core idle"
            ])
        
        init_lines.extend([
            "",
            "// Initialize synchronization area",
        ])
        
        # Initialize sync areas for each level (assuming max 10 levels)
        for level in range(10):
            init_lines.extend([
                f"@{32 + level}",
                "M=0  // Level sync"
            ])
        
        init_lines.extend([
            "",
            "// Initialize constants in optimized memory locations"
        ])
        
        # Initialize constants
        for place_name, place in self.translator.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                init_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        
        init_lines.extend([
            "",
            "// Shared memory initialization complete",
            "(INIT_DONE)",
            "@INIT_DONE",
            "0;JMP"
        ])
        
        return init_lines
        
    def _generate_coordination_documentation(self, core_assignments, num_cores):
        """Generate documentation for the distributed multi-core coordination protocol"""
        doc = f"""# Distributed Multi-Core Coordination Protocol

## System Overview
- **Cores**: {num_cores}
- **Coordination**: Distributed level-based synchronization (NO COORDINATOR)
- **Memory**: Shared optimized memory layout
- **Termination**: Self-terminating cores via final level barrier

## Memory Layout
- `@0-15`: System registers
- `@16-31`: Core status flags (debugging only - not used for coordination)
- `@32-47`: Level synchronization area (distributed coordination)
- `@256+`: Optimized place memory (shared)
- `@512+`: Results collection area

## Core Assignments
"""
        
        for core_id, operations in core_assignments.items():
            doc += f"\n### Core {core_id}\n"
            if operations:
                doc += f"Operations: {len(operations)}\n"
                for op_info in operations:
                    doc += f"- Level {op_info['level']}: {op_info['operation']}\n"
            else:
                doc += "No operations assigned (idle core)\n"
        
        doc += f"""
## Distributed Synchronization Protocol

For detailed information about the distributed synchronization protocol,
see: docs/distributed-synchronization-protocol.md

This protocol eliminates the need for a centralized coordinator by using
level-based barriers for synchronization and distributed termination detection.
"""
        
        return doc