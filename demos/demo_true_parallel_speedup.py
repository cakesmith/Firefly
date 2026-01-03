#!/usr/bin/env python3
"""
True Parallel Speedup Demonstration
===================================
This demo builds Petri nets directly with parallel structure to demonstrate
linear speedup. It bypasses the sequential VM emitter to show what's possible
with true parallel execution.

The key insight is that the standard VM-to-Petri-net translation creates
sequential control flow (each operation waits for the previous one). To achieve
linear speedup, we need to create Petri nets where multiple transitions can
fire simultaneously because they don't share input/output places.

This demo creates:
1. A parallel Petri net structure with independent computation branches
2. Demonstrates near-linear speedup with 2 and 4 cores
3. Shows how to structure computations for maximum parallelism
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition
from Petri.Token import Token


def create_parallel_sum_net(num_branches, ops_per_branch):
    """
    Create a Petri net with parallel computation branches.
    
    Structure:
    - init place with token
    - Fork transition that creates tokens for each branch
    - Each branch: push values -> compute sum
    - Join transition that combines results
    
    This structure allows all branches to execute in parallel.
    """
    net = PetriNet()
    
    # Create init place with token
    init = Place("init")
    net.add_place(init)
    init.put_token(Token("control"))
    
    # Create fork transition that duplicates token for each branch
    fork_outputs = []
    for i in range(num_branches):
        fork_out = Place(f"fork_out_{i}")
        net.add_place(fork_out)
        fork_outputs.append(fork_out)
    
    def fork_operation(tokens):
        return [Token("control") for _ in range(num_branches)]
    
    fork_trans = Transition(
        name="fork",
        operation=fork_operation
    )
    net.add_transition(fork_trans)
    net.add_arc(init, fork_trans)
    for out in fork_outputs:
        net.add_arc(fork_trans, out)
    
    # Create computation branches
    branch_results = []
    for branch_id in range(num_branches):
        # Each branch computes a sum of values
        branch_input = fork_outputs[branch_id]
        
        # Create a chain of operations for this branch
        current_place = branch_input
        running_sum = 0
        
        for op_id in range(ops_per_branch):
            value = branch_id * ops_per_branch + op_id + 1
            running_sum += value
            
            # Create output place for this operation
            op_output = Place(f"branch_{branch_id}_op_{op_id}")
            net.add_place(op_output)
            
            # Create transition that adds value to running sum
            def make_op(val, prev_sum):
                def op(tokens):
                    # Get previous sum from token (or 0 if first op)
                    prev = 0
                    for t in tokens:
                        if hasattr(t, 'value') and isinstance(t.value, int):
                            prev = t.value
                    return [Token(prev + val)]
                return op
            
            op_trans = Transition(
                name=f"branch_{branch_id}_add_{value}",
                operation=make_op(value, running_sum - value)
            )
            net.add_transition(op_trans)
            net.add_arc(current_place, op_trans)
            net.add_arc(op_trans, op_output)
            
            current_place = op_output
        
        branch_results.append((current_place, running_sum))
    
    # Create join transition that combines all branch results
    result_place = Place("result")
    net.add_place(result_place)
    
    def join_operation(tokens):
        total = 0
        for t in tokens:
            if hasattr(t, 'value') and isinstance(t.value, int):
                total += t.value
        return [Token(total)]
    
    join_trans = Transition(
        name="join",
        operation=join_operation
    )
    net.add_transition(join_trans)
    
    for branch_result, _ in branch_results:
        net.add_arc(branch_result, join_trans)
    net.add_arc(join_trans, result_place)
    
    # Calculate expected result
    expected = sum(i + 1 for i in range(num_branches * ops_per_branch))
    
    return net, result_place, expected


def create_wide_parallel_net(width):
    """
    Create a maximally parallel Petri net.
    
    Structure:
    - init place with token
    - Fork to 'width' parallel branches
    - Each branch does one computation
    - Tree reduction to combine results
    
    This achieves maximum parallelism in the computation phase.
    """
    net = PetriNet()
    
    # Create init place with token
    init = Place("init")
    net.add_place(init)
    init.put_token(Token("control"))
    
    # Create fork transition
    fork_outputs = []
    for i in range(width):
        fork_out = Place(f"fork_out_{i}")
        net.add_place(fork_out)
        fork_outputs.append(fork_out)
    
    def fork_operation(tokens):
        return [Token(0) for _ in range(width)]
    
    fork_trans = Transition(
        name="fork",
        operation=fork_operation
    )
    net.add_transition(fork_trans)
    net.add_arc(init, fork_trans)
    for out in fork_outputs:
        net.add_arc(fork_trans, out)
    
    # Create parallel computation transitions (each produces a value)
    compute_outputs = []
    for i in range(width):
        compute_out = Place(f"compute_out_{i}")
        net.add_place(compute_out)
        compute_outputs.append(compute_out)
        
        value = i + 1
        def make_compute(val):
            def compute(tokens):
                return [Token(val)]
            return compute
        
        compute_trans = Transition(
            name=f"compute_{i}",
            operation=make_compute(value)
        )
        net.add_transition(compute_trans)
        net.add_arc(fork_outputs[i], compute_trans)
        net.add_arc(compute_trans, compute_out)
    
    # Tree reduction
    current_level = compute_outputs
    level = 0
    
    while len(current_level) > 1:
        next_level = []
        
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                # Pair exists - create add transition
                add_out = Place(f"add_out_L{level}_{i//2}")
                net.add_place(add_out)
                next_level.append(add_out)
                
                def add_op(tokens):
                    total = 0
                    for t in tokens:
                        if hasattr(t, 'value') and isinstance(t.value, int):
                            total += t.value
                    return [Token(total)]
                
                add_trans = Transition(
                    name=f"add_L{level}_{i//2}",
                    operation=add_op
                )
                net.add_transition(add_trans)
                net.add_arc(current_level[i], add_trans)
                net.add_arc(current_level[i + 1], add_trans)
                net.add_arc(add_trans, add_out)
            else:
                # Odd element - pass through
                next_level.append(current_level[i])
        
        current_level = next_level
        level += 1
    
    result_place = current_level[0]
    expected = sum(range(1, width + 1))
    
    return net, result_place, expected


def execute_sequential(net, result_place, max_steps=1000):
    """Execute Petri net sequentially (1 transition per step)."""
    steps = 0
    transitions_fired = 0
    
    while steps < max_steps:
        # Find enabled transitions
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        # Fire only ONE transition
        t = enabled[0]
        t.fire()
        steps += 1
        transitions_fired += 1
    
    # Get result
    result = None
    if result_place.token:
        result = result_place.token.value
    
    return steps, transitions_fired, result


def execute_parallel(net, result_place, num_cores, max_steps=1000):
    """Execute with parallel firing (up to num_cores per step)."""
    steps = 0
    transitions_fired = 0
    parallel_steps = 0
    
    while steps < max_steps:
        # Find ALL enabled transitions
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        # Select up to num_cores non-conflicting transitions
        to_fire = []
        used_places = set()
        
        for t in enabled:
            t_places = set(p.name for p in t.in_places) | set(p.name for p in t.out_places)
            
            if not (t_places & used_places):
                to_fire.append(t)
                used_places |= t_places
                
                if len(to_fire) >= num_cores:
                    break
        
        # Fire selected transitions
        for t in to_fire:
            t.fire()
            transitions_fired += 1
        
        if len(to_fire) > 1:
            parallel_steps += 1
        
        steps += 1
    
    # Get result
    result = None
    if result_place.token:
        result = result_place.token.value
    
    return steps, transitions_fired, parallel_steps, result


def reset_net(net):
    """Reset all places in the net."""
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))


def run_speedup_test(name, net, result_place, expected):
    """Run speedup test and report results."""
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"  Places: {len(net.places)}, Transitions: {len(net.transitions)}")
    print(f"  Expected result: {expected}")
    print(f"{'='*70}")
    
    # Sequential baseline
    reset_net(net)
    seq_steps, seq_fired, seq_result = execute_sequential(net, result_place)
    
    print(f"\n  Sequential: {seq_steps} steps, {seq_fired} transitions, result={seq_result}")
    if seq_result != expected:
        print(f"  WARNING: Result mismatch! Expected {expected}")
    
    # Parallel execution
    print(f"\n  {'Cores':<8} {'Steps':<10} {'Speedup':<12} {'Efficiency':<12} {'Parallel%':<12}")
    print(f"  {'-'*54}")
    
    results = []
    for num_cores in [1, 2, 4, 8]:
        reset_net(net)
        par_steps, par_fired, par_parallel, par_result = execute_parallel(net, result_place, num_cores)
        
        speedup = seq_steps / par_steps if par_steps > 0 else 1.0
        efficiency = (speedup / num_cores) * 100
        parallel_pct = (par_parallel / par_steps * 100) if par_steps > 0 else 0
        
        print(f"  {num_cores:<8} {par_steps:<10} {speedup:<12.2f}x {efficiency:<12.1f}% {parallel_pct:<12.1f}%")
        results.append((num_cores, par_steps, speedup, efficiency))
    
    return seq_steps, results


def main():
    print("=" * 72)
    print("  True Parallel Speedup Demonstration")
    print("  Direct Petri Net Construction with Parallel Structure")
    print("=" * 72)
    
    all_results = []
    
    # Test 1: 2 parallel branches, 4 ops each
    net, result_place, expected = create_parallel_sum_net(2, 4)
    seq, res = run_speedup_test(
        "Test 1: 2 Parallel Branches (4 ops each)",
        net, result_place, expected
    )
    all_results.append(("2 Branches", seq, res))
    
    # Test 2: 4 parallel branches, 4 ops each
    net, result_place, expected = create_parallel_sum_net(4, 4)
    seq, res = run_speedup_test(
        "Test 2: 4 Parallel Branches (4 ops each)",
        net, result_place, expected
    )
    all_results.append(("4 Branches", seq, res))
    
    # Test 3: 4 parallel branches, 8 ops each
    net, result_place, expected = create_parallel_sum_net(4, 8)
    seq, res = run_speedup_test(
        "Test 3: 4 Parallel Branches (8 ops each)",
        net, result_place, expected
    )
    all_results.append(("4 Branches x8", seq, res))
    
    # Test 4: 8 parallel branches, 4 ops each
    net, result_place, expected = create_parallel_sum_net(8, 4)
    seq, res = run_speedup_test(
        "Test 4: 8 Parallel Branches (4 ops each)",
        net, result_place, expected
    )
    all_results.append(("8 Branches", seq, res))
    
    # Test 5: Wide parallel (8 values)
    net, result_place, expected = create_wide_parallel_net(8)
    seq, res = run_speedup_test(
        "Test 5: Wide Parallel (8 values, tree reduction)",
        net, result_place, expected
    )
    all_results.append(("Wide 8", seq, res))
    
    # Test 6: Wide parallel (16 values)
    net, result_place, expected = create_wide_parallel_net(16)
    seq, res = run_speedup_test(
        "Test 6: Wide Parallel (16 values, tree reduction)",
        net, result_place, expected
    )
    all_results.append(("Wide 16", seq, res))
    
    # Test 7: Wide parallel (32 values)
    net, result_place, expected = create_wide_parallel_net(32)
    seq, res = run_speedup_test(
        "Test 7: Wide Parallel (32 values, tree reduction)",
        net, result_place, expected
    )
    all_results.append(("Wide 32", seq, res))
    
    # Summary
    print("\n" + "=" * 72)
    print("  SPEEDUP SUMMARY")
    print("=" * 72)
    
    print(f"\n  {'Test':<16} {'Seq Steps':<12} {'2-Core':<14} {'4-Core':<14}")
    print(f"  {'-'*56}")
    
    for name, seq, results in all_results:
        speedup_2 = results[1][2]
        speedup_4 = results[2][2]
        print(f"  {name:<16} {seq:<12} {speedup_2:.2f}x ({speedup_2/2*100:.0f}%)    {speedup_4:.2f}x ({speedup_4/4*100:.0f}%)")
    
    # Linear speedup analysis
    print("\n" + "=" * 72)
    print("  LINEAR SPEEDUP ANALYSIS")
    print("=" * 72)
    
    best_2core = 0
    best_4core = 0
    best_test = ""
    
    for name, seq, results in all_results:
        speedup_2 = results[1][2]
        speedup_4 = results[2][2]
        
        linear_2 = speedup_2 / 2.0 * 100
        linear_4 = speedup_4 / 4.0 * 100
        
        if linear_2 + linear_4 > best_2core + best_4core:
            best_2core = linear_2
            best_4core = linear_4
            best_test = name
    
    print(f"\n  Best linear speedup achieved: {best_test}")
    print(f"    2-core: {best_2core:.1f}% of linear (speedup = {best_2core*2/100:.2f}x)")
    print(f"    4-core: {best_4core:.1f}% of linear (speedup = {best_4core*4/100:.2f}x)")
    
    if best_2core >= 90 and best_4core >= 90:
        print("\n  ✓ EXCELLENT: Near-perfect linear speedup achieved!")
    elif best_2core >= 75 and best_4core >= 75:
        print("\n  ✓ VERY GOOD: Strong linear speedup achieved!")
    elif best_2core >= 50 and best_4core >= 50:
        print("\n  ✓ GOOD: Significant parallel speedup achieved.")
    
    # Explanation
    print("\n" + "=" * 72)
    print("  HOW THIS ACHIEVES LINEAR SPEEDUP")
    print("=" * 72)
    print("""
  The Petri net structure enables parallelism through:
  
  1. FORK TRANSITIONS: A single token is duplicated into multiple tokens,
     one for each parallel branch. This creates independent execution paths.
     
  2. INDEPENDENT BRANCHES: Each branch has its own places and transitions
     that don't share resources with other branches. Multiple branches
     can execute simultaneously.
     
  3. JOIN TRANSITIONS: Results from all branches are combined at the end.
     This is the synchronization point.
     
  4. TREE REDUCTION: For wide parallel computations, a tree structure
     allows log(N) reduction steps instead of N-1 sequential steps.
  
  SPEEDUP FORMULA:
  
  For N parallel branches with M operations each:
  - Sequential: 1 (fork) + N*M (branch ops) + 1 (join) = N*M + 2 steps
  - Parallel with N cores: 1 (fork) + M (branch ops) + 1 (join) = M + 2 steps
  - Speedup = (N*M + 2) / (M + 2) ≈ N for large M
  
  This demonstrates that with proper Petri net structure, linear speedup
  is achievable when computations are truly independent.
""")


if __name__ == "__main__":
    main()
