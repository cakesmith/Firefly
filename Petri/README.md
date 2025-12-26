# Petri-Net–Native Virtual Machine

A **Petri-net–native virtual machine and compiler framework** where Petri nets are the
**semantic core** of execution, control flow, concurrency, memory, and correctness.

This project is not about visualizing Petri nets.
The Petri net **is** the program.

---

## Motivation

Traditional VMs hide control flow behind:
- a program counter
- implicit stacks
- sequential execution assumptions

This project replaces those with a **structural execution model**:

- Control flow is token flow
- Concurrency is native
- Correctness is structural
- Analysis and execution share the same semantics

The same Petri net can be:
- executed
- simulated
- refined
- analyzed
- compiled to other targets

---

## Core Principles

- **No hidden program counter**
- **No implicit control state**
- **No implicit duplication or discard**
- **Concurrency by construction**
- **Correctness by structure**

The Petri net is the *semantic truth*.  
All other targets (assembly, JVM, Jenkins, etc.) are optional and erasable.

---

## Architecture Overview

The system consists of three tightly coupled layers:

1. **UIR (Universal Intermediate Representation)**  
   Language-independent IR

2. **Petri Net Semantic Model**  
   Formal execution, control, memory, and correctness

3. **VM / Simulator / Code Generator**  
   Executes or lowers Petri nets to other systems

---

## Token Semantics

Each **token represents an independent thread of execution**.

A token carries:
- a value payload (stack, registers, structured data)
- optional metadata (core ID, region, etc.)

Multiple tokens may exist simultaneously:
- 2 tokens = 2 logical cores
- oversubscription is allowed
- invariants must still hold

---

## Places

Places represent:
- control locations
- memory regions
- stack frames
- synchronization points
- abstract resources

### Compile-Time Place Classification

Places are classified to construct memory hierarchy:

**A. Private Places**
- single producer
- single consumer
- eligible for CPU-local memory

**B. Read-Mostly Places**
- single producer
- multiple consumers
- explicit replication via copy transitions

**C. Shared Mutable Places**
- multiple producers
- shared and arbitrated

This classification enables **compile-time locality optimization**.

---

## Transitions

Transitions:
- consume tokens from *all* input places
- produce exactly one token per output place (except `dup`)
- are atomic
- encode computation and control movement

There is no firing without satisfying all inputs.

---

## The Six Petri-Native Primitives

These primitives are **both minimal and maximal**.
Do not add more.

1. **source**  
   Injects a new token  
   Used for entrypoints and initialization

2. **choice**  
   Selects *exactly one* output place  
   Used for branching (`if-goto`) and nondeterminism

3. **dup**  
   Explicitly duplicates a token  
   Required for independent reuse and parallel consumers

4. **drop**  
   Consumes a token and produces nothing  
   Required to discard values explicitly

5. **join**  
   Synchronizes multiple input tokens into one  
   Required for parallel joins and barriers

6. **loop**  
   Feeds an output token back to an earlier place  
   Required for iteration and recursion

### Affine Discipline

- Tokens are affine by default:
  - consumed exactly once
- `dup` is the *only* way to copy
- `drop` is the *only* way to discard

This prevents hidden aliasing and enforces structural correctness.

---

## Control Flow Model

### No Program Counter

There is no implicit PC.

- Control is represented by token location
- Instruction sequencing is place → transition → place

### Branching

- `if-goto` is modeled as a `choice`
- Exactly one output receives the token
- Invariants hold under concurrency

### Functions, Call, and Return

Functions are modeled as **Petri subnets**:

- Call: token enters function entry place
- Return: token exits via function output place
- Recursion: achieved via `loop` and token flow

No external call stack exists.

---

## Stack Model

- Each token carries its own logical stack
- Stack effects are transitions over token payloads
- No separate mutable stack pointer exists

A “virtual stack” without Petri structure is not allowed:
stack correctness and control correctness are inseparable.

---

## Concurrency Model

- Each token is a logical processor
- Multi-core execution is natural
- Single RAM is modeled via shared places and arbiter transitions
- Oversubscription is permitted

Correctness emerges from structure, not locks.

---

## Self-Stabilization

Self-stabilization is a **core correctness principle**.

The system must:
- define legitimacy predicates over markings
- explicitly model illegitimate states
- include repair transitions that fire only in illegitimate states
- use a well-founded measure that strictly decreases
- converge from *any* marking under weakly fair scheduling

Self-stabilization must be preserved under refinement.

---

## Refinement & Hierarchy

Uses **hierarchical Petri-net refinement**.

Any abstract transition `t` may be refined into a subnet `R(t)`.

Each refinement must define:
- input interface places
- output interface places

### Soundness Obligations

1. Interface well-formedness
2. Guaranteed termination to outputs
3. No internal token leaks
4. Behavioral equivalence to the abstract transition

Refinement order is explicit and preserved.

---

## Compiler Pipeline

### Frontend
- Parse source language (VM, Groovy AST, Jenkinsfile, etc.)
- Lower into UIR

### Lowering
- UIR → Petri net
- Emit places, transitions, and arcs
- No execution occurs here

### Backends (Optional)
- Petri-net interpreter
- Hack assembly
- JVM bytecode
- Jenkins pipeline simulation

The Petri net remains authoritative.

---

## Current Status

- Petri net core classes are being implemented inside the VM codebase
- Parsing exists; code generation is being removed
- The compiler now emits Petri nets instead of instructions

Next steps:
- finalize Petri net runtime semantics
- encode VM instructions as net fragments
- ensure invariants hold under concurrency

---

## Absolute Constraints

- No hidden state
- No program counter
- No weakening affine discipline
- No extra primitives
- Petri nets execute — they are not diagrams

---

## Project Direction

This framework is intended to scale toward:
- distributed execution
- performance modeling
- formal verification
- Jenkins / JVM simulation
- hardware-aware compilation

Petri nets are the unifying abstraction.

---

## License

TBD
