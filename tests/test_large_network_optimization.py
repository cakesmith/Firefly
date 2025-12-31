#!/usr/bin/env python3
"""
Large Network Memory Optimization Showcase
Tests memory reduction capabilities on randomly generated large-scale Petri nets
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition

def print_optimization_results(net, test_name):
    """Print detailed memory optimization results"""
    total_places = len(net.places)
    total_slots = net.allocate_memory()
    efficiency = (total_places - total_slots) / total_places * 100 if total_places > 0 else 0
    
    print(f"\n{'='*60}")
    print(f"🎯 {test_name}")
    print(f"{'='*60}")
    print(f"Total Places: {total_places}")
    print(f"Memory Slots Used: {total_slots}")
    print(f"Memory Reduction: {efficiency:.1f}%")
    print(f"Space Saved: {total_places - total_slots} slots")
    
    # Show sample allocations (first 10 places)
    print(f"\nSample Memory Allocations:")
    sample_count = 0
    for place_name, place in net.places.items():
        if sample_count < 10:
            print(f"  {place_name} -> R{place.memory_address}")
            sample_count += 1
        else:
            break
    
    if len(net.places) > 10:
        print(f"  ... and {len(net.places) - 10} more places")
    
    return total_slots, efficiency

def test_massive_linear_pipeline():
    """Test: Massive linear pipeline (1000 places) - should use only 2 slots"""
    print("\n🚀 MASSIVE LINEAR PIPELINE TEST")
    
    net = PetriNet()
    
    # Create 1000 places in sequence
    for i in range(1000):
        net.add_place(Place(f"Stage_{i:04d}"))
    
    # Create 999 transitions connecting them
    for i in range(999):
        transition_name = f"Process_{i:04d}"
        net.add_transition(Transition(transition_name))
        
        # Connect: Stage_i -> Process_i -> Stage_(i+1)
        net.add_arc(net.places[f"Stage_{i:04d}"], net.transitions[transition_name])
        net.add_arc(net.transitions[transition_name], net.places[f"Stage_{i+1:04d}"])
    
    slots, efficiency = print_optimization_results(net, "Massive Linear Pipeline (1000 places)")
    
    assert slots <= 2, f"Linear pipeline should use ≤2 slots, used {slots}"
    assert efficiency > 99, f"Should achieve >99% efficiency, got {efficiency:.1f}%"
    
    return efficiency

def test_random_tree_forest():
    """Test: Random forest of trees - multiple independent processing chains"""
    print("\n🌲 RANDOM TREE FOREST TEST")
    
    net = PetriNet()
    
    # Create 5 independent trees, each with 100 nodes
    for tree_id in range(5):
        # Root of each tree
        root_name = f"Tree{tree_id}_Root"
        net.add_place(Place(root_name))
        tree_nodes = [root_name]
        
        # Generate random tree structure
        for node_id in range(1, 100):
            node_name = f"Tree{tree_id}_Node_{node_id:03d}"
            net.add_place(Place(node_name))
            tree_nodes.append(node_name)
            
            # Connect to random parent in same tree
            parent = random.choice(tree_nodes[:-1])
            transition_name = f"Tree{tree_id}_T_{parent.split('_')[-1]}_to_{node_id:03d}"
            net.add_transition(Transition(transition_name))
            
            net.add_arc(net.places[parent], net.transitions[transition_name])
            net.add_arc(net.transitions[transition_name], net.places[node_name])
    
    slots, efficiency = print_optimization_results(net, "Random Tree Forest (500 places, 5 trees)")
    
    assert slots <= 10, f"Forest should use ≤10 slots (2 per tree), used {slots}"
    assert efficiency > 95, f"Should achieve >95% efficiency, got {efficiency:.1f}%"
    
    return efficiency

def test_layered_dag_network():
    """Test: Large layered DAG with controlled fan-out"""
    print("\n🔀 LAYERED DAG NETWORK TEST")
    
    net = PetriNet()
    
    # Create 20 layers with 25 nodes each (500 total places)
    layers = []
    for layer_idx in range(20):
        layer_nodes = []
        for node_idx in range(25):
            node_name = f"L{layer_idx:02d}_N{node_idx:02d}"
            net.add_place(Place(node_name))
            layer_nodes.append(node_name)
        layers.append(layer_nodes)
    
    # Connect layers with controlled fan-out (each node connects to 2-4 nodes in next layer)
    for layer_idx in range(19):
        current_layer = layers[layer_idx]
        next_layer = layers[layer_idx + 1]
        
        for source_idx, source_node in enumerate(current_layer):
            # Each source connects to 2-4 targets
            fan_out = random.randint(2, 4)
            targets = random.sample(next_layer, min(fan_out, len(next_layer)))
            
            for target_idx, target_node in enumerate(targets):
                transition_name = f"L{layer_idx:02d}_T{source_idx:02d}_{target_idx}"
                net.add_transition(Transition(transition_name))
                
                net.add_arc(net.places[source_node], net.transitions[transition_name])
                net.add_arc(net.transitions[transition_name], net.places[target_node])
    
    slots, efficiency = print_optimization_results(net, "Layered DAG Network (500 places, 20 layers)")
    
    assert slots <= 50, f"Layered DAG used {slots} slots"
    assert efficiency > 85, f"Should achieve >85% efficiency, got {efficiency:.1f}%"
    
    return efficiency

def test_complex_workflow_network():
    """Test: Complex workflow with branches, merges, and loops"""
    print("\n⚙️ COMPLEX WORKFLOW NETWORK TEST")
    
    net = PetriNet()
    
    # Main workflow backbone (100 stages)
    backbone = []
    for i in range(100):
        stage_name = f"MainFlow_S{i:03d}"
        net.add_place(Place(stage_name))
        backbone.append(stage_name)
        
        if i > 0:
            # Connect sequential stages
            transition_name = f"MainFlow_T{i-1:03d}"
            net.add_transition(Transition(transition_name))
            net.add_arc(net.places[backbone[i-1]], net.transitions[transition_name])
            net.add_arc(net.transitions[transition_name], net.places[stage_name])
    
    # Add parallel processing branches
    branch_id = 0
    for i in range(10, 90, 15):  # Branch every 15 stages
        backbone_source = backbone[i]
        
        # Create parallel branch (5-10 stages)
        branch_length = random.randint(5, 10)
        branch_nodes = []
        
        for j in range(branch_length):
            branch_node = f"Branch{branch_id}_S{j:02d}"
            net.add_place(Place(branch_node))
            branch_nodes.append(branch_node)
            
            if j == 0:
                # Fork from backbone
                fork_transition = f"Fork_B{branch_id}"
                net.add_transition(Transition(fork_transition))
                net.add_arc(net.places[backbone_source], net.transitions[fork_transition])
                net.add_arc(net.transitions[fork_transition], net.places[branch_node])
            else:
                # Connect within branch
                branch_transition = f"Branch{branch_id}_T{j-1:02d}"
                net.add_transition(Transition(branch_transition))
                net.add_arc(net.places[branch_nodes[j-1]], net.transitions[branch_transition])
                net.add_arc(net.transitions[branch_transition], net.places[branch_node])
        
        # Merge back to backbone (with some probability)
        if random.random() > 0.2:  # 80% chance to merge back
            merge_target_idx = min(i + random.randint(10, 25), 99)
            merge_target = backbone[merge_target_idx]
            
            merge_transition = f"Merge_B{branch_id}"
            net.add_transition(Transition(merge_transition))
            net.add_arc(net.places[branch_nodes[-1]], net.transitions[merge_transition])
            net.add_arc(net.transitions[merge_transition], net.places[merge_target])
        
        branch_id += 1
    
    # Add some cross-connections between branches for complexity
    all_places = list(net.places.keys())
    for _ in range(20):  # Add 20 random cross-connections
        source = random.choice(all_places)
        target = random.choice(all_places)
        
        if source != target:
            cross_transition = f"Cross_{len(net.transitions)}"
            net.add_transition(Transition(cross_transition))
            net.add_arc(net.places[source], net.transitions[cross_transition])
            net.add_arc(net.transitions[cross_transition], net.places[target])
    
    slots, efficiency = print_optimization_results(net, f"Complex Workflow Network ({len(net.places)} places)")
    
    assert efficiency > 70, f"Should achieve >70% efficiency, got {efficiency:.1f}%"
    
    return efficiency

def test_mega_scale_network():
    """Test: Mega-scale network (2000+ places) to stress test the optimizer"""
    print("\n🏗️ MEGA-SCALE NETWORK TEST")
    
    net = PetriNet()
    
    # Create a hybrid structure: multiple large pipelines with interconnections
    pipelines = []
    
    # Create 10 parallel pipelines of 150 stages each
    for pipeline_id in range(10):
        pipeline_stages = []
        
        for stage_id in range(150):
            stage_name = f"P{pipeline_id:02d}_S{stage_id:03d}"
            net.add_place(Place(stage_name))
            pipeline_stages.append(stage_name)
            
            if stage_id > 0:
                # Connect sequential stages within pipeline
                transition_name = f"P{pipeline_id:02d}_T{stage_id-1:03d}"
                net.add_transition(Transition(transition_name))
                net.add_arc(net.places[pipeline_stages[stage_id-1]], net.transitions[transition_name])
                net.add_arc(net.transitions[transition_name], net.places[stage_name])
        
        pipelines.append(pipeline_stages)
    
    # Add inter-pipeline connections for data sharing
    for i in range(len(pipelines)):
        for j in range(len(pipelines)):
            if i != j:
                # Connect every 30th stage between pipelines
                for stage_idx in range(0, 150, 30):
                    source_stage = pipelines[i][stage_idx]
                    target_stage = pipelines[j][min(stage_idx + 5, 149)]
                    
                    inter_transition = f"Inter_P{i:02d}_to_P{j:02d}_S{stage_idx:03d}"
                    net.add_transition(Transition(inter_transition))
                    net.add_arc(net.places[source_stage], net.transitions[inter_transition])
                    net.add_arc(net.transitions[inter_transition], net.places[target_stage])
    
    # Add aggregation layer (50 aggregator nodes)
    aggregators = []
    for agg_id in range(50):
        agg_name = f"Aggregator_{agg_id:02d}"
        net.add_place(Place(agg_name))
        aggregators.append(agg_name)
        
        # Each aggregator collects from multiple pipelines
        source_pipelines = random.sample(pipelines, random.randint(2, 5))
        for source_pipeline in source_pipelines:
            source_stage = random.choice(source_pipeline[100:])  # From later stages
            
            agg_transition = f"Collect_A{agg_id:02d}_{len(net.transitions)}"
            net.add_transition(Transition(agg_transition))
            net.add_arc(net.places[source_stage], net.transitions[agg_transition])
            net.add_arc(net.transitions[agg_transition], net.places[agg_name])
    
    slots, efficiency = print_optimization_results(net, f"Mega-Scale Network ({len(net.places)} places)")
    
    assert efficiency > 60, f"Should achieve >60% efficiency even at mega-scale, got {efficiency:.1f}%"
    
    return efficiency

def run_optimization_showcase():
    """Run all large network optimization tests"""
    print("🎯 PETRI NET MEMORY OPTIMIZATION SHOWCASE")
    print("Testing memory reduction on large, randomly generated networks")
    print("="*80)
    
    results = {}
    
    # Run all tests
    results['Linear Pipeline'] = test_massive_linear_pipeline()
    results['Tree Forest'] = test_random_tree_forest()
    results['Layered DAG'] = test_layered_dag_network()
    results['Complex Workflow'] = test_complex_workflow_network()
    results['Mega-Scale'] = test_mega_scale_network()
    
    # Summary report
    print(f"\n{'='*80}")
    print("🏆 OPTIMIZATION SHOWCASE SUMMARY")
    print(f"{'='*80}")
    
    for test_name, efficiency in results.items():
        print(f"{test_name:20}: {efficiency:6.1f}% memory reduction")
    
    avg_efficiency = sum(results.values()) / len(results)
    print(f"{'Average Efficiency':20}: {avg_efficiency:6.1f}% memory reduction")
    
    print(f"\n✅ All tests passed! The memory optimizer successfully reduces")
    print(f"   memory usage across diverse network topologies and scales.")
    print(f"   Average reduction: {avg_efficiency:.1f}%")

if __name__ == "__main__":
    # Set random seed for reproducible results
    random.seed(42)
    
    run_optimization_showcase()