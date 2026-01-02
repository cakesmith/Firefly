"""
Integration between PetriEmitter and Memory Sharing Analysis

This module bridges the existing PetriEmitter implementation with the
memory sharing and mesh placement system.
"""

from typing import Dict, Set, List, Tuple, Optional
from memory_sharing import (
    Transition as MemTransition, Place as MemPlace, MeshCore, ConcurrencyInfo, 
    PlaceType, analyze_and_place, TransitionPlacement, MemoryPlacement
)
from PetriEmitter import PetriEmitter


class PetriMemoryIntegrator:
    """Integrates PetriEmitter with memory sharing analysis"""
    
    def __init__(self, petri_emitter: PetriEmitter):
        self.petri_emitter = petri_emitter
        self.net = petri_emitter.net
    
    def extract_memory_transitions(self) -> List[MemTransition]:
        """
        Extract transitions from PetriEmitter's net and convert to memory analysis format.
        
        Returns:
            List of MemTransition objects for memory analysis
        """
        mem_transitions = []
        
        for trans_id, transition in self.net.transitions.items():
            # Extract reads and writes from the transition's connections
            reads = set()
            writes = set()
            
            # Input places are read by this transition
            for in_place in transition.in_places:
                reads.add(in_place.name)
            
            # Output places are written by this transition
            for out_place in transition.out_places:
                writes.add(out_place.name)
            
            mem_transition = MemTransition(
                id=trans_id,
                reads=reads,
                writes=writes
            )
            mem_transitions.append(mem_transition)
        
        return mem_transitions
    
    def extract_memory_places(self) -> List[MemPlace]:
        """
        Extract places from PetriEmitter's net and classify as ROM or RAM.
        
        Returns:
            List of MemPlace objects for memory analysis
        """
        mem_places = []
        
        for place_id, place in self.net.places.items():
            # Classify place type based on usage patterns
            place_type = self._classify_place_type(place_id, place)
            
            mem_place = MemPlace(
                id=place_id,
                type=place_type
            )
            mem_places.append(mem_place)
        
        return mem_places
    
    def _classify_place_type(self, place_id: str, place) -> PlaceType:
        """
        Classify a place as ROM or RAM based on its characteristics.
        
        Heuristics:
        - Constants and labels are ROM
        - Stack locations and variables are RAM
        - Init/end control places are ROM
        """
        # Check for constant places (ROM)
        if place_id.startswith("const_") or "constant" in place_id.lower():
            return PlaceType.ROM
        
        # Check for label places (ROM - shared instruction space)
        if hasattr(place, 'is_label') and place.is_label:
            return PlaceType.ROM
        if place_id.startswith("label_"):
            return PlaceType.ROM
        
        # Control flow places (ROM)
        if place_id in ["init", "end"]:
            return PlaceType.ROM
        
        # Dup output places (typically control flow - ROM)
        if place_id.startswith("dup_out"):
            return PlaceType.ROM
        
        # Everything else is RAM (stack locations, results, variables)
        return PlaceType.RAM
    
    def infer_concurrency(self) -> ConcurrencyInfo:
        """
        Infer concurrency relationships from the Petri net structure.
        
        For now, this is a simple heuristic. In a real implementation,
        this could be more sophisticated based on:
        - Control flow analysis
        - Loop detection
        - Function call patterns
        
        Returns:
            ConcurrencyInfo with concurrent transition pairs
        """
        concurrent_pairs = set()
        
        # Simple heuristic: transitions that don't share input/output places
        # and are not in a direct sequence might be concurrent
        transitions = list(self.net.transitions.items())
        
        for i, (trans1_id, trans1) in enumerate(transitions):
            for j, (trans2_id, trans2) in enumerate(transitions[i+1:], i+1):
                if self._might_be_concurrent(trans1, trans2):
                    concurrent_pairs.add((trans1_id, trans2_id))
        
        return ConcurrencyInfo(concurrent_pairs)
    
    def _might_be_concurrent(self, trans1, trans2) -> bool:
        """
        Heuristic to determine if two transitions might be concurrent.
        
        Simple rule: if they don't share input places and neither's output
        is the other's input, they might be concurrent.
        """
        # Get place names for comparison
        trans1_inputs = {p.name for p in trans1.in_places}
        trans1_outputs = {p.name for p in trans1.out_places}
        trans2_inputs = {p.name for p in trans2.in_places}
        trans2_outputs = {p.name for p in trans2.out_places}
        
        # If they share input places, they're likely sequential
        if trans1_inputs & trans2_inputs:
            return False
        
        # If one's output is the other's input, they're sequential
        if trans1_outputs & trans2_inputs or trans2_outputs & trans1_inputs:
            return False
        
        # Special case: operations on the same stack level are likely sequential
        if self._are_stack_sequential(trans1, trans2):
            return False
        
        # Otherwise, they might be concurrent
        return True
    
    def _are_stack_sequential(self, trans1, trans2) -> bool:
        """Check if two transitions are sequential stack operations"""
        # This is a simple heuristic - in practice, you'd want more sophisticated analysis
        trans1_name = getattr(trans1, 'name', '')
        trans2_name = getattr(trans2, 'name', '')
        
        # Operations that modify the same stack locations are sequential
        stack_ops = ['add', 'sub', 'neg', 'lt', 'eq', 'gt', 'and', 'or', 'not']
        
        trans1_is_stack = any(op in trans1_name for op in stack_ops)
        trans2_is_stack = any(op in trans2_name for op in stack_ops)
        
        return trans1_is_stack and trans2_is_stack
    
    def create_default_mesh(self, num_cores: int = 4) -> List[MeshCore]:
        """
        Create a default mesh topology for the given number of cores.
        
        Args:
            num_cores: Number of cores to create (default 4 for 2x2 mesh)
            
        Returns:
            List of MeshCore objects representing the mesh
        """
        if num_cores == 4:
            # 2x2 mesh
            return [
                MeshCore("core_0_0", ["core_0_1", "core_1_0"]),
                MeshCore("core_0_1", ["core_0_0", "core_1_1"]),
                MeshCore("core_1_0", ["core_0_0", "core_1_1"]),
                MeshCore("core_1_1", ["core_0_1", "core_1_0"]),
            ]
        elif num_cores == 9:
            # 3x3 mesh
            return [
                MeshCore("core_0_0", ["core_0_1", "core_1_0"]),
                MeshCore("core_0_1", ["core_0_0", "core_0_2", "core_1_1"]),
                MeshCore("core_0_2", ["core_0_1", "core_1_2"]),
                MeshCore("core_1_0", ["core_0_0", "core_1_1", "core_2_0"]),
                MeshCore("core_1_1", ["core_0_1", "core_1_0", "core_1_2", "core_2_1"]),
                MeshCore("core_1_2", ["core_0_2", "core_1_1", "core_2_2"]),
                MeshCore("core_2_0", ["core_1_0", "core_2_1"]),
                MeshCore("core_2_1", ["core_1_1", "core_2_0", "core_2_2"]),
                MeshCore("core_2_2", ["core_1_2", "core_2_1"]),
            ]
        else:
            # Linear topology for other sizes
            cores = []
            for i in range(num_cores):
                neighbors = []
                if i > 0:
                    neighbors.append(f"core_{i-1}")
                if i < num_cores - 1:
                    neighbors.append(f"core_{i+1}")
                cores.append(MeshCore(f"core_{i}", neighbors))
            return cores
    
    def analyze_and_place_memory(self, num_cores: int = 4) -> Tuple[TransitionPlacement, MemoryPlacement]:
        """
        Perform complete memory sharing analysis and mesh placement on the PetriEmitter's net.
        
        Args:
            num_cores: Number of cores in the mesh (default 4)
            
        Returns:
            Tuple of (TransitionPlacement, MemoryPlacement)
        """
        # Extract data from PetriEmitter
        mem_transitions = self.extract_memory_transitions()
        mem_places = self.extract_memory_places()
        mesh_cores = self.create_default_mesh(num_cores)
        concurrency_info = self.infer_concurrency()
        
        # Perform analysis
        return analyze_and_place(mem_transitions, mem_places, mesh_cores, concurrency_info)
    
    # High memory base for place storage (below screen at 16384)
    PLACE_MEMORY_BASE = 15000
    
    def apply_memory_addresses(self, memory_placement: MemoryPlacement):
        """
        Apply memory addresses to places in the PetriEmitter based on placement decisions.
        
        This assigns actual memory addresses to places based on their sharing kind
        and core assignments. Addresses start at PLACE_MEMORY_BASE to avoid conflicts
        with stack/heap.
        """
        address_counter = self.PLACE_MEMORY_BASE
        
        for place_id, place in self.net.places.items():
            if place_id in memory_placement.place_to_cores:
                # Assign memory address if not already assigned
                if not hasattr(place, 'memory_address') or place.memory_address is None:
                    place.memory_address = address_counter
                    address_counter += 1
                
                # Store placement information
                place.memory_kind = memory_placement.memory_kinds[place_id]
                place.assigned_cores = memory_placement.place_to_cores[place_id]
        
        # Warn if we're getting close to screen memory
        if address_counter >= 16384:
            print(f"WARNING: Place memory ({address_counter}) overlaps with screen memory!")
    
    def generate_placement_report(self, transition_placement: TransitionPlacement, 
                                memory_placement: MemoryPlacement) -> str:
        """
        Generate a human-readable report of the placement decisions.
        
        Returns:
            String containing the placement report
        """
        report = []
        report.append("=== PETRI NET MEMORY SHARING & PLACEMENT REPORT ===\n")
        
        # Summary
        report.append("SUMMARY:")
        report.append(f"  Transitions: {len(self.net.transitions)}")
        report.append(f"  Places: {len(self.net.places)}")
        report.append(f"  Memory sharing decisions: {len(memory_placement.memory_kinds)}")
        report.append("")
        
        # Transition placement
        report.append("TRANSITION PLACEMENT:")
        core_assignments = {}
        for trans_id, core_id in transition_placement.mapping.items():
            if core_id not in core_assignments:
                core_assignments[core_id] = []
            core_assignments[core_id].append(trans_id)
        
        for core_id in sorted(core_assignments.keys()):
            transitions_on_core = core_assignments[core_id]
            report.append(f"  {core_id}: {', '.join(transitions_on_core)}")
        report.append("")
        
        # Memory placement
        report.append("MEMORY PLACEMENT:")
        for place_id, kind in memory_placement.memory_kinds.items():
            cores = memory_placement.place_to_cores[place_id]
            place_type = "ROM" if place_id in self.net.places else "UNKNOWN"
            
            # Try to get place type from our classification
            if place_id in self.net.places:
                place = self.net.places[place_id]
                place_type = self._classify_place_type(place_id, place).value
            
            report.append(f"  {place_id} ({place_type}):")
            report.append(f"    Kind: {kind.value}")
            report.append(f"    Cores: {cores if cores else 'None'}")
        
        return "\n".join(report)


def integrate_petri_memory_sharing(petri_emitter: PetriEmitter, num_cores: int = 4) -> str:
    """
    Convenience function to perform complete integration of PetriEmitter with memory sharing.
    
    Args:
        petri_emitter: The PetriEmitter instance to analyze
        num_cores: Number of cores in the target mesh
        
    Returns:
        String report of the analysis results
    """
    integrator = PetriMemoryIntegrator(petri_emitter)
    
    # Perform analysis
    transition_placement, memory_placement = integrator.analyze_and_place_memory(num_cores)
    
    # Apply results back to the PetriEmitter
    integrator.apply_memory_addresses(memory_placement)
    
    # Generate report
    return integrator.generate_placement_report(transition_placement, memory_placement)