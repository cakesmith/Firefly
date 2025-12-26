"""
Advanced Memory Optimization for Petri Net VM
Implements sophisticated memory allocation algorithms with control flow awareness
"""

class MemoryOptimizer:
    """
    Advanced memory optimization with control flow support
    Places can share memory if they can never have tokens simultaneously
    """
    
    def __init__(self, translator):
        self.translator = translator
        
    def optimize_memory_allocation(self):
        """
        Enhanced memory optimization with control flow support
        Places can share memory if they can never have tokens simultaneously
        Includes specialized handling for control flow constructs
        """
        print("\n--- Enhanced Memory Optimization with Control Flow ---")
        
        # Analyze place lifetimes including control flow dependencies
        lifetime_analysis = self._analyze_place_lifetimes_with_control_flow()
        
        # Use interval graph coloring for optimal memory allocation
        memory_allocation = self._allocate_memory_with_control_flow_awareness(lifetime_analysis)
        
        print(f"Original places: {len(self.translator.net.places)}")
        print(f"Memory locations needed: {memory_allocation['total_locations']}")
        print(f"Memory savings: {len(self.translator.net.places) - memory_allocation['total_locations']} locations")
        
        # Show control flow specific optimizations
        self._show_control_flow_memory_details(memory_allocation, lifetime_analysis)
        
        return memory_allocation
        
    def _analyze_place_lifetimes_with_control_flow(self):
        """
        Enhanced place lifetime analysis that handles control flow constructs
        Accounts for labels, goto, and if-goto operations in lifetime calculations
        """
        print("Analyzing place lifetimes with control flow awareness...")
        
        # Get execution plan with control flow dependencies
        execution_plan = self.translator._analyze_execution_dependencies()
        
        # Classify places by type for specialized lifetime analysis
        place_types = self._classify_places_by_type()
        
        # Calculate lifetimes for each place type
        lifetimes = {}
        
        # 1. Control flow places (labels, goto sources, choice results)
        for place_name in place_types['control_flow']:
            lifetimes[place_name] = self._analyze_control_flow_place_lifetime(place_name, execution_plan)
        
        # 2. Regular computation places (arithmetic results, local variables)
        for place_name in place_types['computation']:
            lifetimes[place_name] = self._analyze_computation_place_lifetime(place_name, execution_plan)
        
        # 3. Constant places (live from start)
        for place_name in place_types['constants']:
            lifetimes[place_name] = self._analyze_constant_place_lifetime(place_name, execution_plan)
        
        # 4. Result places (live until end)
        for place_name in place_types['results']:
            lifetimes[place_name] = self._analyze_result_place_lifetime(place_name, execution_plan)
        
        return {
            'lifetimes': lifetimes,
            'execution_plan': execution_plan,
            'place_types': place_types
        }
    
    def _classify_places_by_type(self):
        """
        Classify places by their role in the computation for specialized lifetime analysis
        """
        place_types = {
            'control_flow': [],
            'computation': [],
            'constants': [],
            'results': []
        }
        
        for place_name, place in self.translator.net.places.items():
            if self.translator._is_control_flow_place(place_name):
                place_types['control_flow'].append(place_name)
            elif place_name.startswith('const_'):
                place_types['constants'].append(place_name)
            elif place in self.translator.result_places:
                place_types['results'].append(place_name)
            else:
                place_types['computation'].append(place_name)
        
        print(f"Place classification: {len(place_types['control_flow'])} control flow, "
              f"{len(place_types['computation'])} computation, "
              f"{len(place_types['constants'])} constants, "
              f"{len(place_types['results'])} results")
        
        return place_types
    
    def _analyze_control_flow_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of control flow places with enhanced control flow dependency handling
        These often have very short lifetimes and high reuse potential
        """
        place = self.translator.net.places[place_name]
        
        # Control flow places typically have short, specific lifetimes
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # Enhanced handling for different control flow place types
        if place_name.startswith('label_'):
            # Label places: analyze control flow dependencies to determine actual lifetime
            death_level = self._analyze_label_place_dependencies(place_name, execution_plan)
        
        elif place_name.startswith('goto_source_'):
            # Goto source places have very short lifetimes (just for the jump)
            death_level = birth_level + 1  # Die immediately after use
        
        elif place_name.startswith('if_goto_continue_'):
            # Continue places for if-goto: analyze choice resolution dependencies
            death_level = self._analyze_choice_place_dependencies(place_name, execution_plan)
        
        elif place_name.startswith('control_'):
            # General control places: analyze their specific usage pattern
            death_level = self._analyze_general_control_place_dependencies(place_name, execution_plan)
        
        # Apply control flow dependency constraints
        death_level = self._apply_control_flow_constraints(place_name, birth_level, death_level, execution_plan)
        
        return {
            'birth': birth_level,
            'death': death_level,
            'type': 'control_flow',
            'reuse_priority': 'high',  # Control flow places are good candidates for reuse
            'control_flow_deps': self._get_control_flow_dependencies(place_name, execution_plan)
        }
    
    def _analyze_computation_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of regular computation places (arithmetic, local variables)
        """
        place = self.translator.net.places[place_name]
        
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # Handle control flow dependencies for computation places
        # If a place might be accessed in a loop, extend its lifetime
        if self._place_potentially_in_loop(place_name, execution_plan):
            # Conservative: extend lifetime to account for potential loop iterations
            death_level = max(death_level, birth_level + 3)
        
        return {
            'birth': birth_level,
            'death': death_level,
            'type': 'computation',
            'reuse_priority': 'medium'
        }
    
    def _analyze_constant_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of constant places
        """
        return {
            'birth': -1,  # Constants are born before execution starts
            'death': float('inf'),  # May be needed throughout execution
            'type': 'constant',
            'reuse_priority': 'low'  # Constants should not be reused aggressively
        }
    
    def _analyze_result_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of result places
        """
        place = self.translator.net.places[place_name]
        birth_level = self._find_place_birth_level(place, execution_plan)
        
        return {
            'birth': birth_level,
            'death': float('inf'),  # Results live until program end
            'type': 'result',
            'reuse_priority': 'none'  # Results should never be reused
        }
    
    def _find_place_birth_level(self, place, execution_plan):
        """
        Find the execution level where a place is born (produced)
        """
        if not place.in_transitions:
            return -1  # Source places (constants) are born before execution
        
        # Find the earliest level where any producer transition executes
        min_birth_level = float('inf')
        for producer in place.in_transitions:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if producer.name in level_transitions:
                    min_birth_level = min(min_birth_level, level_idx)
                    break
        
        return min_birth_level if min_birth_level != float('inf') else 0
    
    def _find_place_death_level(self, place, execution_plan):
        """
        Find the execution level where a place dies (consumed)
        """
        if not place.out_transitions:
            return float('inf')  # Sink places (results) never die
        
        # Find the latest level where any consumer transition executes
        max_death_level = -1
        for consumer in place.out_transitions:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if consumer.name in level_transitions:
                    max_death_level = max(max_death_level, level_idx)
                    break
        
        return max_death_level if max_death_level != -1 else 0
    
    def _analyze_label_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for label places to determine accurate lifetime
        """
        # Find all goto/if-goto operations that target this label
        label_name = place_name.replace('label_', '').split('_')[0]  # Extract label name
        
        # Look for jumps to this label
        targeting_jumps = []
        for trans_name in self.translator.net.transitions.keys():
            if (trans_name.startswith('goto_') and label_name in trans_name) or \
               (trans_name.startswith('if_goto_') and label_name in trans_name):
                targeting_jumps.append(trans_name)
        
        if not targeting_jumps:
            # No jumps target this label, it can die early
            birth_level = self._find_place_birth_level(self.translator.net.places[place_name], execution_plan)
            return birth_level + 1
        
        # Find the latest level where any targeting jump might execute
        max_jump_level = -1
        for jump_trans in targeting_jumps:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if jump_trans in level_transitions:
                    max_jump_level = max(max_jump_level, level_idx)
        
        # Label must live until after the latest possible jump
        return max_jump_level + 1 if max_jump_level >= 0 else len(execution_plan['execution_levels'])
    
    def _analyze_choice_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for if-goto continue places
        """
        # Continue places die after the choice is resolved and execution continues
        birth_level = self._find_place_birth_level(self.translator.net.places[place_name], execution_plan)
        
        # Look for the if-goto transition that creates this continue place
        if_goto_trans = None
        for trans_name in self.translator.net.transitions.keys():
            if trans_name.startswith('if_goto_') and place_name.replace('if_goto_continue_', '') in trans_name:
                if_goto_trans = trans_name
                break
        
        if if_goto_trans:
            # Find when the if-goto executes
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if if_goto_trans in level_transitions:
                    # Continue place dies shortly after the choice is made
                    return level_idx + 2
        
        # Default: short lifetime
        return birth_level + 2
    
    def _analyze_general_control_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for general control places
        """
        place = self.translator.net.places[place_name]
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # General control places typically have short lifetimes
        # but may need to live longer if they're part of complex control flow
        if self._is_part_of_complex_control_flow(place_name, execution_plan):
            # Extend lifetime for complex control flow patterns
            return max(death_level, birth_level + 3)
        
        return death_level
    
    def _apply_control_flow_constraints(self, place_name, birth_level, death_level, execution_plan):
        """
        Apply control flow dependency constraints to place lifetime
        """
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        
        # If this place is involved in control flow dependencies, extend its lifetime
        for trans_name, deps in control_flow_deps.items():
            # Check if any transition that uses this place has control flow dependencies
            place = self.translator.net.places[place_name]
            for consumer in place.out_transitions:
                if consumer.name in control_flow_deps and control_flow_deps[consumer.name]:
                    # This place is consumed by a transition with control flow dependencies
                    # Extend its lifetime to account for potential control flow delays
                    death_level = max(death_level, birth_level + 2)
                    break
        
        return death_level
    
    def _get_control_flow_dependencies(self, place_name, execution_plan):
        """
        Get control flow dependencies for a place
        """
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        place = self.translator.net.places[place_name]
        
        deps = []
        # Check dependencies of transitions that consume this place
        for consumer in place.out_transitions:
            if consumer.name in control_flow_deps:
                deps.extend(control_flow_deps[consumer.name])
        
        return list(set(deps))  # Remove duplicates
    
    def _place_potentially_in_loop(self, place_name, execution_plan):
        """
        Determine if a place might be accessed within a loop construct
        Enhanced with better control flow dependency analysis
        """
        # Check if there are any control flow operations that might create loops
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        
        # Look for patterns that suggest loops (goto/if-goto operations)
        for trans_name, deps in control_flow_deps.items():
            if any(dep.startswith(('goto_', 'if_goto_')) for dep in deps):
                # There are control flow operations that might create loops
                # Be conservative and assume computation places might be in loops
                if not place_name.startswith(('const_', 'label_')):
                    return True
        
        # Enhanced analysis: check for backward jumps that indicate loops
        if self._has_backward_control_flow_jumps(execution_plan):
            # If there are backward jumps, computation places might be in loops
            if not self.translator._is_control_flow_place(place_name) and not place_name.startswith('const_'):
                return True
        
        return False
    
    def _has_backward_control_flow_jumps(self, execution_plan):
        """
        Check if there are any backward jumps that might indicate loops
        """
        # Look for goto/if-goto operations that might jump backward
        # This is a heuristic based on transition names and execution levels
        
        control_flow_transitions = []
        for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
            for trans_name in level_transitions:
                if trans_name.startswith(('goto_', 'if_goto_')):
                    control_flow_transitions.append((trans_name, level_idx))
        
        # Check if any control flow operation might jump to an earlier level
        # This is conservative - we assume any control flow might create loops
        return len(control_flow_transitions) > 0
    
    def _is_part_of_complex_control_flow(self, place_name, execution_plan):
        """
        Determine if a place is part of complex control flow patterns
        """
        # Check if there are multiple control flow operations that might affect this place
        control_flow_count = 0
        for level_transitions in execution_plan['execution_levels']:
            for trans_name in level_transitions:
                if trans_name.startswith(('goto_', 'if_goto_', 'label_')):
                    control_flow_count += 1
        
        # If there are multiple control flow operations, consider it complex
        return control_flow_count > 2
    
    def _allocate_memory_with_control_flow_awareness(self, lifetime_analysis):
        """
        Allocate memory locations with control flow awareness
        Uses enhanced interval graph coloring with control flow optimizations
        """
        lifetimes = lifetime_analysis['lifetimes']
        place_types = lifetime_analysis['place_types']
        
        print("Allocating memory with control flow optimizations...")
        
        # Separate places by reuse priority for optimized allocation
        high_priority_reuse = []  # Control flow places
        medium_priority_reuse = []  # Computation places
        low_priority_reuse = []   # Constants
        no_reuse = []            # Results
        
        for place_name, lifetime_info in lifetimes.items():
            priority = lifetime_info.get('reuse_priority', 'medium')
            if priority == 'high':
                high_priority_reuse.append((place_name, lifetime_info))
            elif priority == 'medium':
                medium_priority_reuse.append((place_name, lifetime_info))
            elif priority == 'low':
                low_priority_reuse.append((place_name, lifetime_info))
            else:  # 'none'
                no_reuse.append((place_name, lifetime_info))
        
        # Sort each group by birth time for interval graph coloring
        high_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        medium_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        low_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        no_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        
        # Allocate memory using enhanced interval coloring
        location_map = {}
        location_to_places = {}
        next_location = 256
        
        # Track active intervals for each priority group
        active_intervals = []  # [(end_time, location_id, priority)]
        
        # Process all places in order of reuse priority
        all_places = high_priority_reuse + medium_priority_reuse + low_priority_reuse + no_reuse
        
        for place_name, lifetime_info in all_places:
            birth = lifetime_info['birth']
            death = lifetime_info['death']
            priority = lifetime_info.get('reuse_priority', 'medium')
            
            # Clean up expired intervals
            active_intervals = [(end_time, loc_id, prio) for end_time, loc_id, prio in active_intervals 
                              if end_time > birth]
            
            # Try to find a reusable location based on priority
            reused_location = None
            
            if priority == 'high':
                # Control flow places: aggressive reuse with other control flow places
                reused_location = self._find_reusable_location_for_control_flow(
                    active_intervals, birth, place_name)
            elif priority == 'medium':
                # Computation places: moderate reuse
                reused_location = self._find_reusable_location_for_computation(
                    active_intervals, birth, place_name)
            elif priority == 'low':
                # Constants: conservative reuse
                reused_location = self._find_reusable_location_for_constants(
                    active_intervals, birth, place_name)
            # priority == 'none': no reuse for results
            
            if reused_location is not None:
                # Reuse existing location
                location_map[place_name] = reused_location
                location_to_places[reused_location].append(place_name)
            else:
                # Allocate new location
                location_map[place_name] = next_location
                location_to_places[next_location] = [place_name]
                next_location += 1
            
            # Add this interval to active set (if it has a finite death time)
            if death != float('inf'):
                active_intervals.append((death, location_map[place_name], priority))
        
        # Calculate optimization statistics
        total_locations = next_location - 256
        control_flow_savings = self._calculate_control_flow_savings(
            place_types['control_flow'], location_to_places)
        
        print(f"Control flow places: {len(place_types['control_flow'])}")
        print(f"Control flow memory savings: {control_flow_savings} locations")
        
        return {
            'location_map': location_map,
            'location_to_places': location_to_places,
            'total_locations': total_locations,
            'control_flow_savings': control_flow_savings
        }
    
    def _find_reusable_location_for_control_flow(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for control flow places with enhanced dependency handling
        Control flow places can aggressively reuse memory from each other
        """
        # Enhanced reuse strategy for control flow places
        
        # Priority 1: Reuse from other control flow places that are clearly expired
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority == 'high':
                # Check if this location is safe to reuse for control flow
                if self._is_safe_control_flow_reuse(location_id, place_name, birth_time):
                    return location_id
        
        # Priority 2: Reuse from computation places if they're expired and safe
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority == 'medium':
                if self._is_safe_control_flow_reuse(location_id, place_name, birth_time):
                    return location_id
        
        # Priority 3: Aggressive reuse for very short-lived control flow places
        if self._is_very_short_lived_control_flow_place(place_name):
            # Very short-lived places can reuse locations more aggressively
            for end_time, location_id, priority in active_intervals:
                if end_time <= birth_time + 1:  # Allow slight overlap for very short places
                    return location_id
        
        return None
    
    def _is_safe_control_flow_reuse(self, location_id, place_name, birth_time):
        """
        Check if it's safe to reuse a memory location for a control flow place
        """
        # Control flow places can generally reuse memory safely due to their short lifetimes
        # Additional safety checks for specific patterns
        
        # Check if the place is involved in complex control flow dependencies
        if place_name.startswith('label_') and self._has_multiple_jump_targets(place_name):
            # Labels with multiple jump sources need more careful handling
            return True  # Still safe, but noted for future enhancement
        
        # Goto source places are very safe to reuse
        if place_name.startswith('goto_source_'):
            return True
        
        # Continue places are generally safe
        if place_name.startswith('if_goto_continue_'):
            return True
        
        return True  # Default: control flow places are safe to reuse
    
    def _is_very_short_lived_control_flow_place(self, place_name):
        """
        Determine if a control flow place has a very short lifetime
        """
        # Goto source places are very short-lived
        if place_name.startswith('goto_source_'):
            return True
        
        # Some continue places are very short-lived
        if place_name.startswith('if_goto_continue_'):
            return True
        
        return False
    
    def _has_multiple_jump_targets(self, label_place_name):
        """
        Check if a label place is targeted by multiple jump operations
        """
        if not label_place_name.startswith('label_'):
            return False
        
        label_name = label_place_name.replace('label_', '').split('_')[0]
        
        # Count transitions that target this label
        targeting_count = 0
        for trans_name in self.translator.net.transitions.keys():
            if (trans_name.startswith('goto_') and label_name in trans_name) or \
               (trans_name.startswith('if_goto_') and label_name in trans_name):
                targeting_count += 1
        
        return targeting_count > 1
    
    def _find_reusable_location_for_computation(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for computation places
        More conservative than control flow places
        """
        # Only reuse from other computation places or expired control flow places
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority in ['high', 'medium']:
                return location_id
        
        return None
    
    def _find_reusable_location_for_constants(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for constants
        Very conservative reuse policy
        """
        # Constants only reuse from clearly expired locations
        for end_time, location_id, priority in active_intervals:
            if end_time < birth_time - 1:  # Extra safety margin
                return location_id
        
        return None
    
    def _calculate_control_flow_savings(self, control_flow_places, location_to_places):
        """
        Calculate memory savings specifically from control flow optimizations
        """
        control_flow_locations = set()
        
        for place_name in control_flow_places:
            for location, places in location_to_places.items():
                if place_name in places:
                    control_flow_locations.add(location)
                    break
        
        # Savings = original control flow places - actual locations used
        return len(control_flow_places) - len(control_flow_locations)
    
    def _show_control_flow_memory_details(self, memory_allocation, lifetime_analysis):
        """
        Show detailed memory allocation information for control flow constructs
        """
        print(f"\nControl Flow Memory Optimization Details:")
        
        place_types = lifetime_analysis['place_types']
        location_to_places = memory_allocation['location_to_places']
        
        # Show control flow specific allocations
        control_flow_locations = {}
        
        for place_name in place_types['control_flow']:
            for location, places in location_to_places.items():
                if place_name in places:
                    if location not in control_flow_locations:
                        control_flow_locations[location] = []
                    control_flow_locations[location].append(place_name)
        
        print(f"  Control flow places using {len(control_flow_locations)} memory locations:")
        for location, places in sorted(control_flow_locations.items()):
            if len(places) > 1:
                print(f"    @{location}: SHARED by {len(places)} places: {places}")
            else:
                print(f"    @{location}: {places[0]}")
        
        # Memory efficiency metrics
        total_cf_places = len(place_types['control_flow'])
        cf_locations_used = len(control_flow_locations)
        cf_efficiency = (total_cf_places - cf_locations_used) / total_cf_places * 100 if total_cf_places > 0 else 0
        
        print(f"\n  Control Flow Memory Efficiency:")
        print(f"    Original control flow places: {total_cf_places}")
        print(f"    Memory locations used: {cf_locations_used}")
        print(f"    Control flow memory efficiency: {cf_efficiency:.1f}%")