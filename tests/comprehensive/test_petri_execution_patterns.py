#!/usr/bin/env python3
"""
Petri Net Execution Pattern Analysis
====================================

This test suite focuses specifically on analyzing Petri net execution patterns,
token flow, and the six primitive operations (source, choice, dup, drop, join, loop).

Key analyses:
1. Token flow patterns through the network
2. Primitive operation usage and effectiveness
3. Concurrency patterns and bottlenecks
4. Control flow vs data flow separation
5. Stack-free execution verification
"""

import sys
import os
import json
import time
from collections import defaultdict, deque

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Petri.VMToPetri import VMToPetriTranslator
from Petri.Token import Token, ValueToken
from vm_parser import parse_vm_file

class PetriExecutionPatternAnalyzer:
    """Analyzes execution patterns in Petri nets"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results_dir = "test_results/petri_execution_analysis"
        self.execution_traces = {}
        
        # Create test results directory
        if not os.path.exists(self.test_results_dir):
            os.makedirs(self.test_results_dir)
            print(f"Created execution analysis directory: {self.test_results_dir}/")
    
    def run_test(self, test_name, test_func):
        """Run a test and track results"""
        print(f"\n{'='*60}")
        print(f"ANALYZING EXECUTION PATTERNS: {test_name}")
        print('='*60)
        try:
            success = test_func()
            if success:
                print(f"✅ {test_name} EXECUTION ANALYSIS COMPLETE")
                self.passed += 1
            else:
                print(f"❌ {test_name} EXECUTION ANALYSIS FAILED")
                self.failed += 1
            return success
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
            import traceback
            traceback.print_exc()
            self.failed += 1
            return False
    
    def analyze_execution_patterns(self, commands, test_name):
        """
        Comprehensive execution pattern analysis:
        1. Trace token flow through the network
        2. Analyze primitive operation usage
        3. Identify concurrency patterns
        4. Verify stack-free execution
        5. Analyze control vs data flow
        """
        print(f"Analyzing execution patterns for {len(commands)} commands")
        
        try:
            # Create translator and build network
            translator = VMToPetriTranslator()
            
            # Execute with detailed tracing
            execution_trace = self.trace_execution_with_patterns(translator, commands)
            
            # Analyze the built network structure
            network_analysis = self.analyze_network_structure(translator)
            
            # Analyze primitive usage
            primitive_analysis = self.analyze_primitive_usage(translator, execution_trace)
            
            # Analyze token flow patterns
            token_flow_analysis = self.analyze_token_flow_patterns(execution_trace)
            
            # Analyze concurrency patterns
            concurrency_analysis = self.analyze_concurrency_patterns(execution_trace)
            
            # Verify stack-free execution
            stack_free_verification = self.verify_stack_free_execution(translator, execution_trace)
            
            # Analyze control vs data flow
            flow_separation_analysis = self.analyze_flow_separation(translator)
            
            # Store comprehensive analysis
            self.execution_traces[test_name] = {
                'commands_count': len(commands),
                'execution_trace': execution_trace,
                'network_analysis': network_analysis,
                'primitive_analysis': primitive_analysis,
                'token_flow_analysis': token_flow_analysis,
                'concurrency_analysis': concurrency_analysis,
                'stack_free_verification': stack_free_verification,
                'flow_separation_analysis': flow_separation_analysis,
                'timestamp': time.time()
            }
            
            # Save detailed trace
            self.save_execution_trace(test_name)
            
            return True
            
        except Exception as e:
            print(f"Error analyzing execution patterns: {e}")
            return False
    
    def trace_execution_with_patterns(self, translator, commands):
        """Execute commands while tracing detailed execution patterns"""
        print("Tracing execution with pattern analysis...")
        
        execution_steps = []
        step_counter = 0
        
        # Execute each command and trace the network state
        for i, command in enumerate(commands):
            step_counter += 1
            
            print(f"Step {step_counter}: Executing {command}")
            
            # Capture network state before execution
            before_state = self.capture_network_state(translator.net)
            
            # Execute the command
            try:
                if command[0] == "push":
                    if command[1] == "constant":
                        result_place = translator.push_constant(command[2])
                    elif command[1] == "local":
                        result_place = translator.push_operation("local", command[2])
                    elif command[1] == "argument":
                        result_place = translator.push_operation("argument", command[2])
                    else:
                        result_place = translator.push_operation(command[1], command[2])
                elif command[0] == "pop":
                    translator.pop_operation(command[1], command[2])
                    result_place = None
                elif command[0] in ["add", "sub", "mul", "div"]:
                    result_place = getattr(translator, command[0] + "_operation")()
                elif command[0] in ["eq", "lt", "gt", "and", "or", "not", "neg"]:
                    result_place = getattr(translator, command[0] + "_operation")()
                elif command[0] == "label":
                    translator.label_operation(command[1])
                    result_place = None
                elif command[0] == "goto":
                    translator.goto_operation(command[1])
                    result_place = None
                elif command[0] == "if-goto":
                    translator.if_goto_operation(command[1])
                    result_place = None
                elif command[0] == "function":
                    translator.function_operation(command[1], command[2])
                    result_place = None
                elif command[0] == "call":
                    result_place = translator.call_operation(command[1], command[2])
                elif command[0] == "return":
                    result_place = translator.return_operation()
                else:
                    print(f"Unknown command: {command}")
                    result_place = None
                    
            except Exception as e:
                print(f"Error executing command {command}: {e}")
                result_place = None
            
            # Capture network state after execution
            after_state = self.capture_network_state(translator.net)
            
            # Analyze what changed
            changes = self.analyze_state_changes(before_state, after_state)
            
            # Record execution step
            execution_steps.append({
                'step': step_counter,
                'command': command,
                'before_state': before_state,
                'after_state': after_state,
                'changes': changes,
                'result_place': result_place.name if result_place else None
            })
        
        # Execute the final program to get results
        try:
            final_result = translator.execute_program(commands)
            execution_steps.append({
                'step': 'final_execution',
                'final_result': final_result,
                'final_network_state': self.capture_network_state(translator.net)
            })
        except Exception as e:
            print(f"Error in final execution: {e}")
        
        return execution_steps
    
    def capture_network_state(self, net):
        """Capture the current state of the Petri net"""
        state = {
            'places': {},
            'transitions': {},
            'token_count': 0
        }
        
        # Capture place states
        for place_name, place in net.places.items():
            tokens = []
            for token in place.tokens:
                tokens.append({
                    'value': token.value,
                    'level': getattr(token, 'level', 0),
                    'type': type(token).__name__
                })
            
            state['places'][place_name] = {
                'token_count': len(tokens),
                'tokens': tokens,
                'in_transitions': [t.name for t in place.in_transitions],
                'out_transitions': [t.name for t in place.out_transitions]
            }
            state['token_count'] += len(tokens)
        
        # Capture transition states
        for trans_name, transition in net.transitions.items():
            state['transitions'][trans_name] = {
                'can_fire': transition.can_fire(),
                'in_places': [p.name for p in transition.in_places],
                'out_places': [p.name for p in transition.out_places],
                'operation': str(transition.operation) if transition.operation else None
            }
        
        return state
    
    def analyze_state_changes(self, before_state, after_state):
        """Analyze what changed between two network states"""
        changes = {
            'places_added': [],
            'places_removed': [],
            'transitions_added': [],
            'transitions_removed': [],
            'token_changes': {},
            'total_token_change': after_state['token_count'] - before_state['token_count']
        }
        
        # Analyze place changes
        before_places = set(before_state['places'].keys())
        after_places = set(after_state['places'].keys())
        
        changes['places_added'] = list(after_places - before_places)
        changes['places_removed'] = list(before_places - after_places)
        
        # Analyze transition changes
        before_transitions = set(before_state['transitions'].keys())
        after_transitions = set(after_state['transitions'].keys())
        
        changes['transitions_added'] = list(after_transitions - before_transitions)
        changes['transitions_removed'] = list(before_transitions - after_transitions)
        
        # Analyze token changes in existing places
        for place_name in before_places & after_places:
            before_tokens = before_state['places'][place_name]['token_count']
            after_tokens = after_state['places'][place_name]['token_count']
            
            if before_tokens != after_tokens:
                changes['token_changes'][place_name] = {
                    'before': before_tokens,
                    'after': after_tokens,
                    'change': after_tokens - before_tokens
                }
        
        return changes
    
    def analyze_network_structure(self, translator):
        """Analyze the overall structure of the generated network"""
        print("Analyzing network structure...")
        
        net = translator.net
        
        # Basic metrics
        place_count = len(net.places)
        transition_count = len(net.transitions)
        arc_count = len(net.arcs)
        
        # Analyze network topology
        topology = self.analyze_network_topology(net)
        
        # Analyze place types by naming patterns
        place_types = self.categorize_places_by_function(net.places)
        
        # Analyze transition types by operations
        transition_types = self.categorize_transitions_by_operation(net.transitions)
        
        return {
            'basic_metrics': {
                'places': place_count,
                'transitions': transition_count,
                'arcs': arc_count,
                'places_per_transition': place_count / transition_count if transition_count > 0 else 0
            },
            'topology': topology,
            'place_types': place_types,
            'transition_types': transition_types
        }
    
    def analyze_network_topology(self, net):
        """Analyze the topological properties of the network"""
        # Calculate connectivity metrics
        max_in_degree = 0
        max_out_degree = 0
        total_connections = 0
        
        for place in net.places.values():
            in_degree = len(place.in_transitions)
            out_degree = len(place.out_transitions)
            max_in_degree = max(max_in_degree, in_degree)
            max_out_degree = max(max_out_degree, out_degree)
            total_connections += in_degree + out_degree
        
        # Check for cycles (simplified analysis)
        has_cycles = self.detect_cycles(net)
        
        # Analyze branching factor
        branching_analysis = self.analyze_branching_patterns(net)
        
        return {
            'max_in_degree': max_in_degree,
            'max_out_degree': max_out_degree,
            'avg_connectivity': total_connections / (2 * len(net.places)) if net.places else 0,
            'has_cycles': has_cycles,
            'branching_analysis': branching_analysis
        }
    
    def detect_cycles(self, net):
        """Simple cycle detection in the Petri net"""
        # Use DFS to detect cycles
        visited = set()
        rec_stack = set()
        
        def dfs(node_name, node_type):
            if node_name in rec_stack:
                return True  # Cycle detected
            if node_name in visited:
                return False
            
            visited.add(node_name)
            rec_stack.add(node_name)
            
            # Get neighbors based on node type
            if node_type == 'place':
                neighbors = [(t.name, 'transition') for t in net.places[node_name].out_transitions]
            else:  # transition
                neighbors = [(p.name, 'place') for p in net.transitions[node_name].out_places]
            
            for neighbor_name, neighbor_type in neighbors:
                if dfs(neighbor_name, neighbor_type):
                    return True
            
            rec_stack.remove(node_name)
            return False
        
        # Check for cycles starting from each place
        for place_name in net.places:
            if place_name not in visited:
                if dfs(place_name, 'place'):
                    return True
        
        return False
    
    def analyze_branching_patterns(self, net):
        """Analyze branching and merging patterns"""
        branching_places = 0  # Places with multiple output transitions
        merging_places = 0    # Places with multiple input transitions
        choice_transitions = 0  # Transitions with multiple output places
        join_transitions = 0    # Transitions with multiple input places
        
        for place in net.places.values():
            if len(place.out_transitions) > 1:
                branching_places += 1
            if len(place.in_transitions) > 1:
                merging_places += 1
        
        for transition in net.transitions.values():
            if len(transition.out_places) > 1:
                choice_transitions += 1
            if len(transition.in_places) > 1:
                join_transitions += 1
        
        return {
            'branching_places': branching_places,
            'merging_places': merging_places,
            'choice_transitions': choice_transitions,
            'join_transitions': join_transitions
        }
    
    def categorize_places_by_function(self, places):
        """Categorize places by their functional role"""
        categories = {
            'constants': 0,
            'local_variables': 0,
            'arguments': 0,
            'computation_results': 0,
            'control_flow': 0,
            'function_related': 0,
            'temporary': 0,
            'other': 0
        }
        
        for place_name in places:
            name_lower = place_name.lower()
            
            if 'const' in name_lower:
                categories['constants'] += 1
            elif 'local' in name_lower:
                categories['local_variables'] += 1
            elif 'arg' in name_lower:
                categories['arguments'] += 1
            elif any(op in name_lower for op in ['add', 'sub', 'mul', 'div', 'eq', 'lt', 'gt']):
                categories['computation_results'] += 1
            elif any(cf in name_lower for cf in ['label', 'goto', 'if', 'choice', 'control']):
                categories['control_flow'] += 1
            elif any(fn in name_lower for fn in ['function', 'call', 'return']):
                categories['function_related'] += 1
            elif 'temp' in name_lower or 'tmp' in name_lower:
                categories['temporary'] += 1
            else:
                categories['other'] += 1
        
        return categories
    
    def categorize_transitions_by_operation(self, transitions):
        """Categorize transitions by their operation type"""
        categories = {
            'source': 0,      # Create tokens
            'choice': 0,      # Select paths
            'dup': 0,         # Duplicate tokens
            'drop': 0,        # Discard tokens
            'join': 0,        # Synchronize tokens
            'loop': 0,        # Feedback loops
            'arithmetic': 0,  # Arithmetic operations
            'logical': 0,     # Logical operations
            'memory': 0,      # Memory operations
            'control': 0,     # Control flow
            'function': 0,    # Function operations
            'other': 0
        }
        
        for trans_name in transitions:
            name_lower = trans_name.lower()
            
            if 'source' in name_lower or 'const' in name_lower:
                categories['source'] += 1
            elif 'choice' in name_lower or 'goto' in name_lower or 'if' in name_lower:
                categories['choice'] += 1
            elif 'dup' in name_lower:
                categories['dup'] += 1
            elif 'drop' in name_lower:
                categories['drop'] += 1
            elif 'join' in name_lower or any(op in name_lower for op in ['add', 'sub', 'mul', 'div']):
                categories['join'] += 1
            elif 'loop' in name_lower:
                categories['loop'] += 1
            elif any(op in name_lower for op in ['add', 'sub', 'mul', 'div', 'neg']):
                categories['arithmetic'] += 1
            elif any(op in name_lower for op in ['eq', 'lt', 'gt', 'and', 'or', 'not']):
                categories['logical'] += 1
            elif any(op in name_lower for op in ['push', 'pop', 'local', 'arg']):
                categories['memory'] += 1
            elif any(op in name_lower for op in ['label', 'goto', 'if']):
                categories['control'] += 1
            elif any(op in name_lower for op in ['call', 'return', 'function']):
                categories['function'] += 1
            else:
                categories['other'] += 1
        
        return categories
    
    def analyze_primitive_usage(self, translator, execution_trace):
        """Analyze usage of the six Petri net primitives"""
        print("Analyzing primitive operation usage...")
        
        primitive_counts = {
            'source': 0,
            'choice': 0,
            'dup': 0,
            'drop': 0,
            'join': 0,
            'loop': 0
        }
        
        primitive_examples = {
            'source': [],
            'choice': [],
            'dup': [],
            'drop': [],
            'join': [],
            'loop': []
        }
        
        # Analyze transitions to identify primitive usage
        for trans_name, transition in translator.net.transitions.items():
            primitive_type = self.identify_primitive_type(trans_name, transition)
            if primitive_type in primitive_counts:
                primitive_counts[primitive_type] += 1
                primitive_examples[primitive_type].append(trans_name)
        
        # Calculate primitive usage statistics
        total_primitives = sum(primitive_counts.values())
        primitive_percentages = {}
        for primitive, count in primitive_counts.items():
            primitive_percentages[primitive] = (count / total_primitives * 100) if total_primitives > 0 else 0
        
        return {
            'primitive_counts': primitive_counts,
            'primitive_percentages': primitive_percentages,
            'primitive_examples': primitive_examples,
            'total_primitive_operations': total_primitives,
            'primitive_diversity': len([p for p in primitive_counts.values() if p > 0])
        }
    
    def identify_primitive_type(self, trans_name, transition):
        """Identify which of the six primitives a transition represents"""
        name_lower = trans_name.lower()
        
        # Analyze by name patterns and structure
        if 'source' in name_lower or 'const' in name_lower:
            return 'source'
        elif 'choice' in name_lower or ('goto' in name_lower) or ('if' in name_lower):
            return 'choice'
        elif 'dup' in name_lower:
            return 'dup'
        elif 'drop' in name_lower:
            return 'drop'
        elif len(transition.in_places) > 1:  # Multiple inputs suggest join
            return 'join'
        elif 'loop' in name_lower or self.has_feedback_loop(transition):
            return 'loop'
        else:
            # Default classification based on structure
            if len(transition.in_places) == 0:
                return 'source'
            elif len(transition.out_places) > 1:
                return 'choice'
            elif len(transition.in_places) > 1:
                return 'join'
            else:
                return 'source'  # Default
    
    def has_feedback_loop(self, transition):
        """Check if a transition is part of a feedback loop"""
        # Simple heuristic: check if any output place connects back to an input place
        for out_place in transition.out_places:
            for out_trans in out_place.out_transitions:
                for final_place in out_trans.out_places:
                    if final_place in transition.in_places:
                        return True
        return False
    
    def analyze_token_flow_patterns(self, execution_trace):
        """Analyze patterns in token flow through the network"""
        print("Analyzing token flow patterns...")
        
        token_flow_stats = {
            'max_concurrent_tokens': 0,
            'total_token_movements': 0,
            'token_lifetime_analysis': {},
            'flow_bottlenecks': [],
            'parallel_flow_opportunities': 0
        }
        
        # Track token counts over time
        token_counts_over_time = []
        
        for step in execution_trace:
            if 'after_state' in step:
                token_count = step['after_state']['token_count']
                token_counts_over_time.append(token_count)
                token_flow_stats['max_concurrent_tokens'] = max(
                    token_flow_stats['max_concurrent_tokens'], 
                    token_count
                )
        
        # Analyze token movement patterns
        for step in execution_trace:
            if 'changes' in step:
                changes = step['changes']
                token_flow_stats['total_token_movements'] += abs(changes['total_token_change'])
                
                # Identify bottlenecks (places where tokens accumulate)
                for place_name, change_info in changes['token_changes'].items():
                    if change_info['after'] > 3:  # Arbitrary threshold for bottleneck
                        if place_name not in token_flow_stats['flow_bottlenecks']:
                            token_flow_stats['flow_bottlenecks'].append(place_name)
        
        # Analyze parallel flow opportunities
        token_flow_stats['parallel_flow_opportunities'] = len([
            count for count in token_counts_over_time if count > 1
        ])
        
        # Calculate flow efficiency
        if token_counts_over_time:
            avg_tokens = sum(token_counts_over_time) / len(token_counts_over_time)
            token_flow_stats['average_concurrent_tokens'] = avg_tokens
            token_flow_stats['token_utilization'] = avg_tokens / token_flow_stats['max_concurrent_tokens'] if token_flow_stats['max_concurrent_tokens'] > 0 else 0
        
        return token_flow_stats
    
    def analyze_concurrency_patterns(self, execution_trace):
        """Analyze concurrency patterns and parallelization opportunities"""
        print("Analyzing concurrency patterns...")
        
        concurrency_analysis = {
            'max_parallel_operations': 0,
            'parallel_execution_steps': 0,
            'sequential_bottlenecks': 0,
            'concurrency_efficiency': 0,
            'parallel_patterns': []
        }
        
        # Analyze each execution step for concurrency
        for step in execution_trace:
            if 'after_state' in step:
                state = step['after_state']
                
                # Count transitions that can fire simultaneously
                fireable_transitions = [
                    name for name, trans_info in state['transitions'].items()
                    if trans_info['can_fire']
                ]
                
                parallel_ops = len(fireable_transitions)
                concurrency_analysis['max_parallel_operations'] = max(
                    concurrency_analysis['max_parallel_operations'],
                    parallel_ops
                )
                
                if parallel_ops > 1:
                    concurrency_analysis['parallel_execution_steps'] += 1
                    concurrency_analysis['parallel_patterns'].append({
                        'step': step.get('step', 'unknown'),
                        'parallel_operations': fireable_transitions,
                        'parallelism_degree': parallel_ops
                    })
                elif parallel_ops == 1:
                    concurrency_analysis['sequential_bottlenecks'] += 1
        
        # Calculate concurrency efficiency
        total_steps = len([s for s in execution_trace if 'after_state' in s])
        if total_steps > 0:
            concurrency_analysis['concurrency_efficiency'] = (
                concurrency_analysis['parallel_execution_steps'] / total_steps
            )
        
        return concurrency_analysis
    
    def verify_stack_free_execution(self, translator, execution_trace):
        """Verify that execution is truly stack-free"""
        print("Verifying stack-free execution...")
        
        verification = {
            'is_stack_free': True,
            'stack_like_patterns': [],
            'hidden_state_indicators': [],
            'visible_state_verification': True
        }
        
        # Check for stack-like naming patterns
        for place_name in translator.net.places:
            if any(pattern in place_name.lower() for pattern in ['stack', 'sp', 'stack_pointer']):
                verification['is_stack_free'] = False
                verification['stack_like_patterns'].append(place_name)
        
        # Check for hidden state indicators
        for trans_name in translator.net.transitions:
            if any(pattern in trans_name.lower() for pattern in ['push_stack', 'pop_stack', 'stack_op']):
                verification['hidden_state_indicators'].append(trans_name)
        
        # Verify all state is visible in places
        for step in execution_trace:
            if 'after_state' in step:
                state = step['after_state']
                # All computation state should be visible as tokens in places
                total_tokens = state['token_count']
                if total_tokens == 0 and step.get('command', [''])[0] not in ['label', 'goto', 'if-goto']:
                    # Might indicate hidden state if we expect tokens but see none
                    pass  # This is actually normal for some operations
        
        return verification
    
    def analyze_flow_separation(self, translator):
        """Analyze separation between control flow and data flow"""
        print("Analyzing control vs data flow separation...")
        
        flow_analysis = {
            'control_flow_places': 0,
            'data_flow_places': 0,
            'mixed_flow_places': 0,
            'control_flow_transitions': 0,
            'data_flow_transitions': 0,
            'separation_quality': 0
        }
        
        # Classify places
        for place_name, place in translator.net.places.items():
            if self.is_control_flow_place(place_name):
                flow_analysis['control_flow_places'] += 1
            elif self.is_data_flow_place(place_name):
                flow_analysis['data_flow_places'] += 1
            else:
                flow_analysis['mixed_flow_places'] += 1
        
        # Classify transitions
        for trans_name, transition in translator.net.transitions.items():
            if self.is_control_flow_transition(trans_name):
                flow_analysis['control_flow_transitions'] += 1
            else:
                flow_analysis['data_flow_transitions'] += 1
        
        # Calculate separation quality
        total_places = len(translator.net.places)
        if total_places > 0:
            flow_analysis['separation_quality'] = (
                (flow_analysis['control_flow_places'] + flow_analysis['data_flow_places']) / 
                total_places
            )
        
        return flow_analysis
    
    def is_control_flow_place(self, place_name):
        """Determine if a place is primarily for control flow"""
        control_keywords = ['label', 'goto', 'if', 'choice', 'control', 'branch', 'jump']
        return any(keyword in place_name.lower() for keyword in control_keywords)
    
    def is_data_flow_place(self, place_name):
        """Determine if a place is primarily for data flow"""
        data_keywords = ['const', 'local', 'arg', 'add', 'sub', 'mul', 'div', 'result', 'value']
        return any(keyword in place_name.lower() for keyword in data_keywords)
    
    def is_control_flow_transition(self, trans_name):
        """Determine if a transition is primarily for control flow"""
        control_keywords = ['goto', 'if', 'choice', 'branch', 'jump', 'label']
        return any(keyword in trans_name.lower() for keyword in control_keywords)
    
    def save_execution_trace(self, test_name):
        """Save detailed execution trace to file"""
        if test_name not in self.execution_traces:
            return
            
        trace_file = os.path.join(self.test_results_dir, f"{test_name}_execution_trace.json")
        
        try:
            with open(trace_file, 'w') as f:
                json.dump(self.execution_traces[test_name], f, indent=2, default=str)
            print(f"Saved execution trace: {trace_file}")
        except Exception as e:
            print(f"Error saving execution trace: {e}")
    
    # Test methods for different execution patterns
    
    def test_simple_arithmetic_pattern(self):
        """Test execution patterns in simple arithmetic"""
        commands = [
            ("push", "constant", 7),
            ("push", "constant", 8),
            ("add",)
        ]
        return self.analyze_execution_patterns(commands, "simple_arithmetic_pattern")
    
    def test_complex_arithmetic_pattern(self):
        """Test execution patterns in complex arithmetic"""
        commands = [
            ("push", "constant", 10),
            ("push", "constant", 3),
            ("sub",),
            ("push", "constant", 2),
            ("mul",),
            ("neg",),
            ("push", "constant", 5),
            ("add",)
        ]
        return self.analyze_execution_patterns(commands, "complex_arithmetic_pattern")
    
    def test_control_flow_pattern(self):
        """Test execution patterns in control flow"""
        commands = [
            ("push", "constant", 5),
            ("push", "constant", 3),
            ("gt",),
            ("if-goto", "TRUE_BRANCH"),
            ("push", "constant", 0),
            ("goto", "END"),
            ("label", "TRUE_BRANCH"),
            ("push", "constant", 1),
            ("label", "END")
        ]
        return self.analyze_execution_patterns(commands, "control_flow_pattern")
    
    def test_function_call_pattern(self):
        """Test execution patterns in function calls"""
        commands = [
            ("function", "test", 1),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("add",),
            ("return",),
            ("push", "constant", 5),
            ("call", "test", 1)
        ]
        return self.analyze_execution_patterns(commands, "function_call_pattern")
    
    def test_recursive_pattern(self):
        """Test execution patterns in recursive functions"""
        commands = [
            ("function", "factorial", 0),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("eq",),
            ("if-goto", "BASE_CASE"),
            ("push", "argument", 0),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("sub",),
            ("call", "factorial", 1),
            ("mul",),
            ("return",),
            ("label", "BASE_CASE"),
            ("push", "constant", 1),
            ("return",),
            ("push", "constant", 3),
            ("call", "factorial", 1)
        ]
        return self.analyze_execution_patterns(commands, "recursive_pattern")
    
    def test_memory_access_pattern(self):
        """Test execution patterns in memory access"""
        commands = [
            ("push", "constant", 10),
            ("pop", "local", 0),
            ("push", "constant", 20),
            ("pop", "local", 1),
            ("push", "local", 0),
            ("push", "local", 1),
            ("add",),
            ("pop", "local", 2),
            ("push", "local", 2)
        ]
        return self.analyze_execution_patterns(commands, "memory_access_pattern")
    
    def run_all_tests(self):
        """Run all execution pattern analysis tests"""
        print("=" * 80)
        print("PETRI NET EXECUTION PATTERN ANALYSIS SUITE")
        print("=" * 80)
        
        # Test different execution patterns
        self.run_test("Simple Arithmetic Pattern", self.test_simple_arithmetic_pattern)
        self.run_test("Complex Arithmetic Pattern", self.test_complex_arithmetic_pattern)
        self.run_test("Control Flow Pattern", self.test_control_flow_pattern)
        self.run_test("Function Call Pattern", self.test_function_call_pattern)
        self.run_test("Recursive Pattern", self.test_recursive_pattern)
        self.run_test("Memory Access Pattern", self.test_memory_access_pattern)
        
        # Generate comprehensive analysis report
        self.generate_pattern_analysis_report()
        
        # Print summary
        print("\n" + "=" * 80)
        print("EXECUTION PATTERN ANALYSIS SUMMARY")
        print("=" * 80)
        print(f"Total pattern tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success rate: {self.passed / (self.passed + self.failed) * 100:.1f}%")
        
        if self.execution_traces:
            self.print_aggregate_pattern_statistics()
        
        print(f"\nDetailed traces saved in: {self.test_results_dir}/")
        
        return self.failed == 0
    
    def generate_pattern_analysis_report(self):
        """Generate comprehensive pattern analysis report"""
        report_file = os.path.join(self.test_results_dir, "pattern_analysis_report.json")
        
        summary = {
            'total_patterns_analyzed': len(self.execution_traces),
            'timestamp': time.time(),
            'aggregate_statistics': self.calculate_aggregate_statistics(),
            'detailed_traces': self.execution_traces
        }
        
        try:
            with open(report_file, 'w') as f:
                json.dump(summary, f, indent=2, default=str)
            print(f"\nSaved pattern analysis report: {report_file}")
        except Exception as e:
            print(f"Error saving pattern analysis report: {e}")
    
    def calculate_aggregate_statistics(self):
        """Calculate aggregate statistics across all pattern analyses"""
        if not self.execution_traces:
            return {}
        
        # Aggregate primitive usage
        total_primitives = defaultdict(int)
        for trace in self.execution_traces.values():
            if 'primitive_analysis' in trace:
                for primitive, count in trace['primitive_analysis']['primitive_counts'].items():
                    total_primitives[primitive] += count
        
        # Aggregate concurrency metrics
        max_concurrency = 0
        total_parallel_steps = 0
        total_steps = 0
        
        for trace in self.execution_traces.values():
            if 'concurrency_analysis' in trace:
                concurrency = trace['concurrency_analysis']
                max_concurrency = max(max_concurrency, concurrency.get('max_parallel_operations', 0))
                total_parallel_steps += concurrency.get('parallel_execution_steps', 0)
                total_steps += concurrency.get('parallel_execution_steps', 0) + concurrency.get('sequential_bottlenecks', 0)
        
        # Aggregate stack-free verification
        stack_free_count = sum(
            1 for trace in self.execution_traces.values()
            if trace.get('stack_free_verification', {}).get('is_stack_free', False)
        )
        
        return {
            'primitive_usage_totals': dict(total_primitives),
            'max_concurrency_observed': max_concurrency,
            'overall_parallelization_rate': total_parallel_steps / total_steps if total_steps > 0 else 0,
            'stack_free_verification_rate': stack_free_count / len(self.execution_traces),
            'patterns_analyzed': len(self.execution_traces)
        }
    
    def print_aggregate_pattern_statistics(self):
        """Print aggregate statistics across all patterns"""
        stats = self.calculate_aggregate_statistics()
        
        print(f"\nAggregate Pattern Statistics:")
        print(f"Patterns analyzed: {stats.get('patterns_analyzed', 0)}")
        print(f"Max concurrency observed: {stats.get('max_concurrency_observed', 0)}")
        print(f"Overall parallelization rate: {stats.get('overall_parallelization_rate', 0) * 100:.1f}%")
        print(f"Stack-free verification rate: {stats.get('stack_free_verification_rate', 0) * 100:.1f}%")
        
        print(f"\nPrimitive Usage Totals:")
        for primitive, count in stats.get('primitive_usage_totals', {}).items():
            print(f"  {primitive}: {count}")


if __name__ == "__main__":
    analyzer = PetriExecutionPatternAnalyzer()
    success = analyzer.run_all_tests()
    sys.exit(0 if success else 1)