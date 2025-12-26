# Distributed Synchronization Protocol

## Level-Based Execution (NO COORDINATOR)
1. Each core signals ready for current level by setting its bit
2. Each core waits for ALL cores to be ready at current level
3. When all cores ready, ALL cores proceed simultaneously
4. Repeat for next level
5. **Final level completion = Program completion**

## Core Status Protocol (DEBUGGING ONLY)
- **0**: Core idle/waiting (debugging visibility)
- **1**: Core working on operations (debugging visibility)
- **2**: Core completed all operations (debugging visibility)
- **NOTE**: Status flags are NOT used for coordination - only for debugging

## Distributed Termination
- **No coordinator** monitors core status
- **Final level barrier** serves as completion detection
- Each core **self-terminates** when final level barrier is satisfied
- **No single point of failure** or coordination bottleneck

## Execution Flow
1. Run `shared_init.asm` to initialize shared memory
2. Start all core ROMs simultaneously
3. Cores self-coordinate using level barriers
4. **No coordinator needed** - cores terminate when final level completes
5. Final results available in optimized memory locations

## Key Innovation: Elimination of Coordinator

### Traditional Multi-Core:
- Centralized coordinator monitors all cores
- Single point of failure
- Coordinator overhead

### Our Distributed Approach:
- **Level synchronization IS completion detection**
- **Each core knows when program is complete**
- **No coordinator overhead**
- **Pure Petri net semantics**

## Files Generated
- `core0.asm` to `core{num_cores-1}.asm`: Individual core ROMs (self-coordinating)
- `shared_init.asm`: Shared memory initialization
- `coordination.md`: This documentation file

## Technical Details

### Level Barrier Algorithm:
```assembly
// Each core at each level:
1. Set ready bit: sync_area |= (1 << core_id)
2. Wait for all: while (sync_area != all_cores_mask)
3. Proceed when barrier satisfied
```

### Distributed Termination:
```assembly
// Each core after final level:
1. Wait for final level barrier completion
2. Self-terminate when barrier satisfied
3. No coordinator involvement
```

This approach eliminates the centralized coordinator while maintaining
correctness through formal Petri net level analysis.