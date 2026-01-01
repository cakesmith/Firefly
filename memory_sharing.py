"""
Minimal Petri-Net Memory Sharing & Mesh Placement

This module implements memory sharing decisions and mesh core placement
for transitions in a Petri net, based on memory access patterns and concurrency.
"""

from typing import Dict, Set, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass


class PlaceType(Enum):
    ROM = "ROM"
    RAM = "RAM"


class MemoryKind(Enum):
    PRIVATE = "PRIVATE"      # Only one transition/core uses it
    SHARED = "SHARED"        # Multiple transitions on same core (non-concurrent)
    REPLICATED = "REPLICATED"  # Multiple copies across cores (concurrent allowed)
    ARBITRATED = "ARBITRATED"  # Multiple cores share RAM with conflict management


@dataclass
class Transition:
    """Represents a VM instruction as a transition in the Petri net"""
    id: str
    reads: Set[str]  # Set of PlaceIds this transition reads from
    writes: Set[str]  # Set of PlaceIds this transition writes to


@dataclass
class Place:
    """Represents a memory location as a place in the Petri net"""
    id: str
    type: PlaceType  # ROM or RAM


@dataclass
class MeshCore:
    """Represents a core in the 2D mesh"""
    id: str
    neighbors: List[str] = None  # List of neighboring core IDs
    
    def __post_init__(self):
        if self.neighbors is None:
            self.neighbors = []


@dataclass
class ConcurrencyInfo:
    """Information about which transitions may be concurrent"""
    concurrent: Set[Tuple[str, str]]  # Set of (TransitionId, TransitionId) pairs
    
    def are_concurrent(self, t1_id: str, t2_id: str) -> bool:
        """Check if two transitions may be concurrent"""
        return (t1_id, t2_id) in self.concurrent or (t2_id, t1_id) in self.concurrent


@dataclass
class TransitionPlacement:
    """Result of transition placement on mesh cores"""
    mapping: Dict[str, str]  # TransitionId -> CoreId


@dataclass
class MemoryPlacement:
    """Result of memory placement decisions"""
    place_to_cores: Dict[str, List[str]]  # PlaceId -> list of CoreIds that have a copy
    memory_kinds: Dict[str, MemoryKind]   # PlaceId -> memory sharing kind


class MemorySharingAnalyzer:
    """Analyzes memory sharing patterns and makes placement decisions"""
    
    def __init__(self, transitions: List[Transition], places: List[Place], 
                 cores: List[MeshCore], concurrency: ConcurrencyInfo):
        self.transitions = {t.id: t for t in transitions}
        self.places = {p.id: p for p in places}
        self.cores = {c.id: c for c in cores}
        self.concurrency = concurrency
        
        # Build reverse mappings for analysis
        self.place_readers = self._build_place_readers()
        self.place_writers = self._build_place_writers()
        self.place_accessors = self._build_place_accessors()
    
    def _build_place_readers(self) -> Dict[str, Set[str]]:
        """Build mapping from PlaceId to set of TransitionIds that read from it"""
        readers = {}
        for place_id in self.places:
            readers[place_id] = set()
        
        for trans_id, trans in self.transitions.items():
            for place_id in trans.reads:
                if place_id in readers:
                    readers[place_id].add(trans_id)
        
        return readers
    
    def _build_place_writers(self) -> Dict[str, Set[str]]:
        """Build mapping from PlaceId to set of TransitionIds that write to it"""
        writers = {}
        for place_id in self.places:
            writers[place_id] = set()
        
        for trans_id, trans in self.transitions.items():
            for place_id in trans.writes:
                if place_id in writers:
                    writers[place_id].add(trans_id)
        
        return writers
    
    def _build_place_accessors(self) -> Dict[str, Set[str]]:
        """Build mapping from PlaceId to set of TransitionIds that access it (read or write)"""
        accessors = {}
        for place_id in self.places:
            accessors[place_id] = self.place_readers[place_id] | self.place_writers[place_id]
        
        return accessors
    
    def analyze_memory_sharing(self) -> MemoryPlacement:
        """
        Analyze memory sharing patterns and determine memory placement strategy.
        
        Returns:
            MemoryPlacement with decisions for each place
        """
        place_to_cores = {}
        memory_kinds = {}
        
        for place_id, place in self.places.items():
            accessors = self.place_accessors[place_id]
            
            if len(accessors) == 0:
                # No transitions access this place - mark as private (unused)
                place_to_cores[place_id] = []
                memory_kinds[place_id] = MemoryKind.PRIVATE
                continue
            
            if len(accessors) == 1:
                # Only one transition accesses this place - private memory
                place_to_cores[place_id] = []  # Will be assigned during placement
                memory_kinds[place_id] = MemoryKind.PRIVATE
                continue
            
            # Multiple transitions access this place - check concurrency
            concurrent_pairs = self._find_concurrent_accessors(accessors)
            
            if place.type == PlaceType.ROM:
                if len(concurrent_pairs) == 0:
                    # ROM with no concurrent access - can share freely
                    memory_kinds[place_id] = MemoryKind.SHARED
                else:
                    # ROM with concurrent access - replicate for performance
                    memory_kinds[place_id] = MemoryKind.REPLICATED
            else:  # RAM
                if len(concurrent_pairs) == 0:
                    # RAM with no concurrent access - can share
                    memory_kinds[place_id] = MemoryKind.SHARED
                else:
                    # RAM with concurrent access - need arbitration or replication
                    # For simplicity, use arbitration (single shared copy with conflict management)
                    memory_kinds[place_id] = MemoryKind.ARBITRATED
            
            # Cores will be determined during placement phase
            place_to_cores[place_id] = []
        
        return MemoryPlacement(place_to_cores, memory_kinds)
    
    def _find_concurrent_accessors(self, accessors: Set[str]) -> List[Tuple[str, str]]:
        """Find pairs of transitions that are concurrent and both access the same place"""
        concurrent_pairs = []
        accessor_list = list(accessors)
        
        for i in range(len(accessor_list)):
            for j in range(i + 1, len(accessor_list)):
                t1, t2 = accessor_list[i], accessor_list[j]
                if self.concurrency.are_concurrent(t1, t2):
                    concurrent_pairs.append((t1, t2))
        
        return concurrent_pairs
    
    def place_transitions_on_mesh(self, memory_placement: MemoryPlacement) -> TransitionPlacement:
        """
        Place transitions on mesh cores based on memory sharing patterns.
        
        Uses a greedy approach:
        1. Group transitions that share memory
        2. Place groups on same core if possible
        3. Otherwise place on neighboring cores
        
        Args:
            memory_placement: Result from analyze_memory_sharing()
            
        Returns:
            TransitionPlacement mapping transitions to cores
        """
        mapping = {}
        core_list = list(self.cores.keys())
        core_index = 0
        
        # Build sharing groups - transitions that share memory should be close
        sharing_groups = self._build_sharing_groups(memory_placement)
        
        # Place each sharing group
        for group in sharing_groups:
            if len(group) == 1:
                # Single transition - place on next available core
                trans_id = list(group)[0]
                core_id = core_list[core_index % len(core_list)]
                mapping[trans_id] = core_id
                core_index += 1
            else:
                # Multiple transitions sharing memory - try to place on same core
                # For simplicity, place all on same core (could be optimized)
                core_id = core_list[core_index % len(core_list)]
                for trans_id in group:
                    mapping[trans_id] = core_id
                core_index += 1
        
        # Update memory placement with actual core assignments
        self._update_memory_core_assignments(memory_placement, mapping)
        
        return TransitionPlacement(mapping)
    
    def _build_sharing_groups(self, memory_placement: MemoryPlacement) -> List[Set[str]]:
        """
        Build groups of transitions that share memory and should be placed together.
        
        Returns:
            List of sets, where each set contains TransitionIds that should be grouped
        """
        # Start with each transition in its own group
        groups = [{trans_id} for trans_id in self.transitions.keys()]
        
        # Merge groups that share memory (for SHARED and ARBITRATED memory)
        for place_id, kind in memory_placement.memory_kinds.items():
            if kind in [MemoryKind.SHARED, MemoryKind.ARBITRATED]:
                accessors = self.place_accessors[place_id]
                if len(accessors) > 1:
                    # Find groups containing these transitions and merge them
                    groups_to_merge = []
                    for i, group in enumerate(groups):
                        if group & accessors:  # If group intersects with accessors
                            groups_to_merge.append(i)
                    
                    if len(groups_to_merge) > 1:
                        # Merge all groups that contain accessors
                        merged_group = set()
                        for i in sorted(groups_to_merge, reverse=True):
                            merged_group |= groups.pop(i)
                        groups.append(merged_group)
        
        return groups
    
    def _update_memory_core_assignments(self, memory_placement: MemoryPlacement, 
                                      transition_mapping: Dict[str, str]):
        """Update memory placement with actual core assignments based on transition placement"""
        for place_id, kind in memory_placement.memory_kinds.items():
            accessors = self.place_accessors[place_id]
            
            if kind == MemoryKind.PRIVATE:
                # Private memory goes to the core of the single accessor
                if len(accessors) == 1:
                    trans_id = list(accessors)[0]
                    core_id = transition_mapping[trans_id]
                    memory_placement.place_to_cores[place_id] = [core_id]
                else:
                    memory_placement.place_to_cores[place_id] = []
            
            elif kind == MemoryKind.SHARED:
                # Shared memory goes to cores where accessors are placed
                cores = set()
                for trans_id in accessors:
                    if trans_id in transition_mapping:
                        cores.add(transition_mapping[trans_id])
                memory_placement.place_to_cores[place_id] = list(cores)
            
            elif kind == MemoryKind.REPLICATED:
                # Replicated memory goes to all cores where accessors are placed
                cores = set()
                for trans_id in accessors:
                    if trans_id in transition_mapping:
                        cores.add(transition_mapping[trans_id])
                memory_placement.place_to_cores[place_id] = list(cores)
            
            elif kind == MemoryKind.ARBITRATED:
                # Arbitrated memory - single copy, but note which cores need access
                cores = set()
                for trans_id in accessors:
                    if trans_id in transition_mapping:
                        cores.add(transition_mapping[trans_id])
                # For arbitrated, we could place on one core or use a central location
                # For simplicity, place on the first core that needs it
                if cores:
                    memory_placement.place_to_cores[place_id] = [list(cores)[0]]
                else:
                    memory_placement.place_to_cores[place_id] = []


def analyze_and_place(transitions: List[Transition], places: List[Place], 
                     cores: List[MeshCore], concurrency: ConcurrencyInfo) -> Tuple[TransitionPlacement, MemoryPlacement]:
    """
    Main entry point for memory sharing analysis and mesh placement.
    
    Args:
        transitions: List of transitions (VM instructions)
        places: List of places (memory locations)
        cores: List of available mesh cores
        concurrency: Information about concurrent transitions
        
    Returns:
        Tuple of (TransitionPlacement, MemoryPlacement)
    """
    analyzer = MemorySharingAnalyzer(transitions, places, cores, concurrency)
    
    # Step 1: Analyze memory sharing patterns
    memory_placement = analyzer.analyze_memory_sharing()
    
    # Step 2: Place transitions on mesh cores
    transition_placement = analyzer.place_transitions_on_mesh(memory_placement)
    
    return transition_placement, memory_placement