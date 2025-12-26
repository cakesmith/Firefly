"""
Execution Dependency Analyzer for Petri Net VM
Analyzes execution dependencies and creates execution plans for multi-core systems
"""

class ExecutionAnalyzer:
    """
    Analyzes execution dependencies and creates execution plans
    Enhanced to handle control flow operations (goto, if-goto, labels)
    """
    
    def __init__(self, translator):
        self.translator = translator
        
    def analyze_execution_dependencies(self):
        """
        Analyze the Petri net to determine execution dependencies
        Enhanced to handle control flow operations (goto, if-goto, labels)
        Returns a dependency graph and execution levels with conservative level assignment
        """
        # Build dependency graph
        dependencies = {}
        reverse_deps = {}
        
        for trans_name, transition in self.translator.net.transitions.items():
            dependencies[trans_name] = []
            reverse_deps[trans_name] = []
            
        # Find dependencies based on place connections
        for trans_name, transition in self.translator.net.transitions.items():
            for input_place in transition.in_places:
                # Find which transition produces this place
                for producer_name, producer in self.translator.net.transitions.items():
                    if input_place in producer.out_places:
                        dependencies[trans_name].append(producer_name)
                        reverse_deps[producer_name].append(trans_name)
        
        # Handle control flow dependencies
        control_flow_deps = self._analyze_control_flow_dependencies()
        
        # Merge control flow dependencies with place-based dependencies
        for trans_name, cf_deps in control_flow_deps.items():
            if trans_name in dependencies:
                dependencies[trans_name].extend(cf_deps)
                # Update reverse dependencies
                for dep in cf_deps:
                    if dep in reverse_deps:
                        reverse_deps[dep].append(trans_name)
                        
        # Remove duplicates
        for trans_name in dependencies:
            dependencies[trans_name] = list(set(dependencies[trans_name]))
        for trans_name in reverse_deps:
            reverse_deps[trans_name] = list(set(reverse_deps[trans_name]))
                        
        # Topological sort to find execution levels
        execution_levels = []
        remaining = set(self.translator.net.transitions.keys())
        
        while remaining:
            # Find transitions with no unresolved dependencies
            ready = []
            for trans in remaining:
                if all(dep not in remaining for dep in dependencies[trans]):
                    ready.append(trans)
                    
            if not ready:
                # Handle cycles or isolated nodes
                ready = [next(iter(remaining))]
                
            execution_levels.append(ready)
            remaining -= set(ready)
            
        return {
            'dependencies': dependencies,
            'reverse_deps': reverse_deps,
            'execution_levels': execution_levels,
            'control_flow_deps': control_flow_deps
        }
    
    def _analyze_control_flow_dependencies(self):
        """
        Analyze dependencies created by control flow operations
        Implements conservative level assignment for goto/if-goto operations
        """
        control_flow_deps = {}
        
        # Initialize empty dependencies for all transitions
        for trans_name in self.translator.net.transitions.keys():
            control_flow_deps[trans_name] = []
        
        # Analyze each transition for control flow patterns
        for trans_name, transition in self.translator.net.transitions.items():
            
            # Handle goto operations
            if trans_name.startswith("goto_"):
                # Extract label name from transition name
                # Format: goto_LABELNAME_N
                parts = trans_name.split("_")
                if len(parts) >= 2:
                    label_name = parts[1]
                    
                    # Conservative approach: goto operations create dependencies
                    # All operations that might execute after the goto must wait for it
                    for other_trans_name in self.translator.net.transitions.keys():
                        if (other_trans_name != trans_name and 
                            not other_trans_name.startswith("goto_") and
                            not other_trans_name.startswith("if_goto_")):
                            # Other operations depend on control flow resolution
                            control_flow_deps[other_trans_name].append(trans_name)
            
            # Handle if-goto operations  
            elif trans_name.startswith("if_goto_"):
                # Extract label name from transition name
                # Format: if_goto_LABELNAME_N
                parts = trans_name.split("_")
                if len(parts) >= 3:
                    label_name = parts[2]  # Skip "if" and "goto"
                    
                    # Conservative approach: if-goto creates choice dependencies
                    # Operations that might be affected by the conditional jump
                    # must wait for the choice to be resolved
                    
                    # Find related operations that might be in the jump path
                    for other_trans_name in self.translator.net.transitions.keys():
                        if (other_trans_name != trans_name and 
                            not other_trans_name.startswith("goto_") and
                            not other_trans_name.startswith("if_goto_")):
                            
                            # Check if this operation might be affected by the jump
                            # Conservative: assume all subsequent operations depend on choice
                            if self._is_potentially_affected_by_control_flow(trans_name, other_trans_name):
                                control_flow_deps[other_trans_name].append(trans_name)
        
        # Add inter-control-flow dependencies
        # Multiple control flow operations in sequence create dependencies
        control_flow_transitions = [name for name in self.translator.net.transitions.keys() 
                                  if name.startswith(('goto_', 'if_goto_'))]
        
        for i, cf_trans1 in enumerate(control_flow_transitions):
            for cf_trans2 in control_flow_transitions[i+1:]:
                # Later control flow operations depend on earlier ones
                # This ensures proper sequencing of control flow decisions
                control_flow_deps[cf_trans2].append(cf_trans1)
        
        # Log control flow dependencies for debugging
        cf_deps_found = {k: v for k, v in control_flow_deps.items() if v}
        if cf_deps_found:
            print(f"\nControl Flow Dependencies Found:")
            for trans_name, deps in list(cf_deps_found.items())[:3]:  # Show first 3
                print(f"  {trans_name} depends on: {deps[:3]}{'...' if len(deps) > 3 else ''}")
            if len(cf_deps_found) > 3:
                print(f"  ... and {len(cf_deps_found) - 3} more")
        
        return control_flow_deps
        
    def _is_potentially_affected_by_control_flow(self, cf_transition, other_transition):
        """
        Determine if a transition might be affected by a control flow operation
        More refined conservative approach: focus on operations that could be in control flow paths
        """
        # Skip other control flow operations (they have their own dependencies)
        if other_transition.startswith(('goto_', 'if_goto_')):
            return False
            
        # Skip operations that are clearly independent (constants, sources)
        if other_transition.startswith(('const_', 'source_')):
            return False
            
        # Operations that are likely to be in the execution path and could be affected
        # by control flow decisions should depend on control flow operations
        
        # Local variable operations could be in loops
        if other_transition.startswith(('dup_local_', 'pop_local_')):
            return True
            
        # Arithmetic operations could be in loops  
        if any(other_transition.startswith(op) for op in ['add_', 'sub_', 'mul_', 'div_', 'neg_']):
            return True
            
        # Comparison operations could be in conditional paths
        if any(other_transition.startswith(op) for op in ['eq_', 'lt_', 'gt_', 'and_', 'or_', 'not_']):
            return True
            
        # Function call operations could be affected by control flow
        if other_transition.startswith(('call_', 'return_')):
            return True
            
        # Most other operations are potentially affected by control flow
        return True
        
    def assign_operations_to_cores(self, execution_plan, num_cores):
        """
        Assign operations to cores based on dependencies and load balancing
        Enhanced to handle control flow operations with distributed coordination
        """
        core_assignments = {i: [] for i in range(num_cores)}
        
        for level_idx, level in enumerate(execution_plan['execution_levels']):
            print(f"Level {level_idx}: {len(level)} parallel operations: {level}")
            
            # Check if this level contains control flow operations
            control_flow_ops = [op for op in level 
                              if op.startswith(('goto_', 'if_goto_', 'label_'))]
            
            if control_flow_ops:
                print(f"  Control flow operations in level {level_idx}: {control_flow_ops}")
                # All cores must participate in control flow synchronization
                # Even if they don't execute the specific control flow operation
                
            # Assign operations in this level to cores (round-robin)
            for i, operation in enumerate(level):
                core_id = i % num_cores
                
                # Mark control flow operations for special handling
                is_control_flow = operation.startswith(('goto_', 'if_goto_', 'label_'))
                
                core_assignments[core_id].append({
                    'operation': operation,
                    'level': level_idx,
                    'transition': self.translator.net.transitions.get(operation),
                    'is_control_flow': is_control_flow,
                    'requires_barrier': is_control_flow or len(control_flow_ops) > 0
                })
                
        # Ensure all cores have barrier synchronization at control flow levels
        self._ensure_control_flow_barriers(core_assignments, execution_plan)
                
        return core_assignments
    
    def _ensure_control_flow_barriers(self, core_assignments, execution_plan):
        """
        Ensure all cores participate in barriers at levels containing control flow
        This maintains distributed coordination even when cores don't execute control flow ops
        """
        # Find levels that contain control flow operations
        control_flow_levels = set()
        for level_idx, level in enumerate(execution_plan['execution_levels']):
            if any(op.startswith(('goto_', 'if_goto_', 'label_')) for op in level):
                control_flow_levels.add(level_idx)
        
        if control_flow_levels:
            print(f"Control flow barrier levels: {sorted(control_flow_levels)}")
            
            # Ensure all cores have operations marked for barriers at these levels
            for core_id, operations in core_assignments.items():
                for op_info in operations:
                    if op_info['level'] in control_flow_levels:
                        op_info['requires_barrier'] = True
                        
                # If a core has no operations at a control flow level,
                # add a barrier placeholder
                core_levels = {op['level'] for op in operations}
                for cf_level in control_flow_levels:
                    if cf_level not in core_levels:
                        # Add barrier placeholder for this core
                        core_assignments[core_id].append({
                            'operation': f'barrier_placeholder_level_{cf_level}',
                            'level': cf_level,
                            'transition': None,
                            'is_control_flow': False,
                            'requires_barrier': True,
                            'is_placeholder': True
                        })
        
        # Sort operations by level for each core
        for core_id in core_assignments:
            core_assignments[core_id].sort(key=lambda x: x['level'])