# Quezo

### A visual playground for scheduling algorithms, workload simulation, and performance analysis.

Quezo is an open-source scheduling simulator designed to explore how scheduling policies behave under different workloads. It combines Python's flexibility, Rust's performance, and interactive visualization to make scheduling decisions observable, measurable, and comparable.

The goal is to build a tool where users can define workloads, simulate their execution, inspect process timelines, compare scheduling policies, and understand the trade-offs behind each algorithm.

> **Project status:** Early development. Features listed in the roadmap are planned unless explicitly marked as implemented.

---

## Table of Contents

- [Overview](#overview)
- [Why Quezo?](#why-quezo)
- [Core Features](#core-features)
- [How It Works](#how-it-works)
- [Scheduling Algorithms](#scheduling-algorithms)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Testing and Quality](#testing-and-quality)
- [Performance Benchmarking](#performance-benchmarking)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [Design Principles](#design-principles)
- [License](#license)

---

## Overview

Scheduling is the process of deciding which task should execute, when it should execute, and how available resources should be allocated.

Different scheduling policies produce different outcomes. One may minimize average waiting time, another may prioritize urgent work, while another may favor tasks that arrived earlier.

Quezo aims to make these differences visible through reproducible simulations and measurable results.

With Quezo, the intended workflow is:

1. Define a workload containing processes, arrival times, burst durations, and priorities.
2. Select a scheduling policy.
3. Run a simulation.
4. Inspect the execution timeline and process states.
5. Analyze performance metrics.
6. Repeat the experiment with another policy.
7. Compare the results using the same workload.

The initial focus is CPU-style process scheduling. The architecture may later support broader scheduling experiments, subject to the requirements and limitations of each model.

## Why Quezo?

Scheduling algorithms are often taught through static tables and manually calculated examples. These methods explain the basics, but they make it difficult to explore larger workloads or understand how changing input parameters affects the result.

Quezo aims to bridge that gap.

- **Experiment instead of guessing:** Run different policies against identical workloads.
- **Visualize execution:** Inspect when processes start, run, and finish.
- **Measure trade-offs:** Compare waiting time, turnaround time, throughput, and utilization.
- **Learn through implementation:** Explore object-oriented design, simulation architecture, and algorithm behavior.
- **Investigate performance:** Compare a Python reference implementation with a Rust implementation using reproducible benchmarks.

Quezo is intended as both an educational tool and a practical software engineering project.

---

## Core Features

The following capabilities define the planned initial release.

### 1. Workload Modeling

Create workloads containing processes with configurable attributes.

| Attribute | Description |
|---|---|
| Process ID | Unique identifier for a process |
| Arrival time | Time at which a process becomes available |
| Burst duration | CPU time required for completion |
| Priority | Scheduling priority assigned to the process |
| Dependencies | Optional relationships that constrain execution order |

Input validation will prevent invalid configurations from entering the simulation engine.

### 2. Scheduling Policies

The initial implementation is planned to include:

- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling

The first version will focus on non-preemptive policies. Preemptive algorithms and additional scheduling strategies can be introduced after the core simulation engine is validated.

### 3. Simulation Engine

The simulation engine will manage:

- Simulated time
- Process arrival and completion
- Ready queues
- Worker availability
- Process state transitions
- Execution intervals
- Simulation results

The engine will use simulated time rather than real-time delays, allowing experiments to run quickly and reproducibly.

### 4. Interactive Visualization

The planned desktop interface will provide:

- A workload editor
- Scheduling policy selection
- A Gantt-style execution timeline
- Current simulation time and process states
- Step, pause, reset, and replay controls
- Metric summaries and policy comparisons

### 5. Performance Metrics

Quezo will calculate and present metrics such as:

- Waiting time
- Turnaround time
- Completion time
- Response time, where applicable
- Throughput
- CPU utilization

Metrics will be calculated from the execution trace, keeping the measurement logic separate from the scheduling policies.

### 6. Experiment Comparison

Users will be able to execute multiple policies against the same workload and compare their outcomes.

This will make it possible to investigate questions such as:

- Which policy produces the lowest average waiting time for a particular workload?
- How do long-running tasks affect shorter tasks?
- What happens when process priorities change?
- How does idle time affect utilization?
- Does the Rust implementation improve execution time for larger workloads?

The results will be based on measured data rather than assumptions about which algorithm is universally best.

### 7. Persistence

SQLite integration is planned to support saving and loading workloads and experiment results, making it easier to reproduce and revisit experiments.

---

## How It Works

Quezo separates workload definition, scheduling decisions, execution, and analysis.

```text
        Workload Configuration
                  |
                  v
          Input Validation
                  |
                  v
         Simulation Engine
                  |
           +------+------+
           |             |
           v             v
    Python Engine    Rust Engine
           |             |
           +------+------+
                  |
                  v
          Execution Trace
                  |
           +------+------+
           |             |
           v             v
      Metrics       Timeline Data
           |             |
           +------+------+
                  |
                  v
          Visualization UI
```

The Python engine will act as the reference implementation. The Rust engine will implement the same supported behavior through a defined interface.

Both engines should produce equivalent results for identical workloads and scheduling configurations.

The interface will consume structured results rather than depending on the internal implementation of either engine.

---

## Scheduling Algorithms

### First-Come, First-Served (FCFS)

Processes are selected in arrival order.

**Strengths**
- Simple to understand and implement.
- Predictable execution order.
- Low scheduling complexity.

**Limitations**
- A long-running process can delay shorter processes.
- Average waiting time can be high for some workloads.

### Shortest Job First (SJF)

Among currently available processes, the process with the shortest burst duration is selected.

**Strengths**
- Can reduce average waiting time for suitable workloads.
- Demonstrates the impact of workload characteristics on scheduling decisions.

**Limitations**
- Requires knowledge or estimates of burst durations.
- Long tasks may experience extended delays when short tasks repeatedly arrive.

### Priority Scheduling

The scheduler selects the available process with the highest configured priority.

**Strengths**
- Models workloads with different levels of importance.
- Makes priority-based trade-offs observable.

**Limitations**
- Low-priority processes may wait for a long time.
- Priority inversion and starvation require additional mechanisms to address in more advanced implementations.

The initial version will define a consistent priority convention and deterministic tie-breaking rules so that experiments remain reproducible.

---

## Architecture

Quezo will use a modular architecture with explicit responsibilities.

### Domain Layer

Defines the core data structures, configuration, and validation rules.

### Scheduling Layer

Implements interchangeable scheduling policies through a common interface. Policies decide which eligible process should run next without owning the entire simulation lifecycle.

### Simulation Layer

Coordinates simulated time, process state transitions, worker availability, and execution events.

### Metrics Layer

Calculates statistics from completed simulations without coupling metric calculations to individual scheduling algorithms.

### Application Layer

Coordinates workloads, simulations, experiments, persistence, and communication with the user interface.

### Rust Execution Layer

Provides an optimized implementation of selected computational operations through Python–Rust interoperability.

### Presentation Layer

Displays configuration controls, execution timelines, process states, and analytical results.

This separation is intended to make the system easier to test, extend, and maintain.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Domain models, application logic, reference simulation |
| Rust | Performance-oriented simulation implementation |
| PyO3 | Exposing Rust functionality to Python |
| Maturin | Building and packaging the Rust extension |
| PySide6 | Desktop user interface |
| SQLite | Workload and experiment persistence |
| uv | Python dependency and environment management |
| Ruff | Python linting and formatting |
| pytest | Automated testing |
| mypy | Optional static type checking |
| Cargo | Rust dependency management, builds, and tests |
| Git and GitHub | Version control and collaboration |

The stack is intentionally split by responsibility. Rust will be introduced after the Python behavior is sufficiently well-defined to provide a reliable correctness baseline.

---

## Project Structure

The planned repository layout is:

```text
Quezo/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── quezo/
│       ├── __init__.py
│       ├── models.py
│       ├── policies.py
│       ├── validator.py
│       ├── engine.py
│       ├── metrics.py
│       ├── experiments.py
│       ├── repository.py
│       └── ui/
│           ├── main_window.py
│           ├── timeline.py
│           └── workload_editor.py
├── rust_engine/
│   ├── Cargo.toml
│   └── src/
│       └── lib.rs
├── tests/
│   ├── test_models.py
│   ├── test_policies.py
│   ├── test_engine.py
│   └── test_metrics.py
└── docs/
    └── design.md
```

This structure is a design target, not a claim that every module already exists.

---

## Getting Started

### Prerequisites

Install the following tools:

- Python 3
- uv
- Rust toolchain through rustup
- Git

The desktop interface and Rust bindings will be introduced as their corresponding development phases begin.

### 1. Clone the repository

Replace the placeholder with the actual repository URL.

```bash
git clone <YOUR_REPOSITORY_URL>
cd Quezo
```

### 2. Create the Python environment

If the repository already contains a `pyproject.toml`:

```bash
uv sync --dev
```

If you are creating the project from scratch:

```bash
uv init
uv add --dev pytest ruff maturin mypy pytest-cov
```

Use the existing project configuration rather than reinitializing an already configured repository.

### 3. Verify the development tools

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

These commands are intended to run once the initial source and test structure exists. An empty or incomplete project may not yet pass all checks.

### 4. Verify Rust

Install Rust through the official rustup installation instructions if it is not already installed.

Then run:

```bash
rustc --version
cargo --version
```

### 5. Build and run

The exact application launch command will be documented once the initial executable entry point is implemented.

Until then, development should begin with the domain models, scheduling policies, and automated tests.

---

## Development Workflow

Quezo is being developed incrementally. Each phase should produce a working, testable result.

### Phase 1 — Foundation and Domain Modeling

- Establish the package structure.
- Define process and simulation models.
- Implement input validation.
- Add unit tests for valid and invalid configurations.

**Completion criterion:** Workloads can be represented and validated independently of the interface.

### Phase 2 — Scheduling Policies

- Define a common policy interface.
- Implement FCFS, SJF, and Priority Scheduling.
- Define deterministic tie-breaking behavior.
- Test policies against hand-calculated examples.

**Completion criterion:** Policies can be swapped without rewriting the simulation engine.

### Phase 3 — Simulation and Metrics

- Implement the simulation loop.
- Track process arrivals, execution, and completion.
- Record execution intervals.
- Calculate performance metrics.
- Test edge cases and reproducibility.

**Completion criterion:** Known workloads produce correct execution traces and metrics.

### Phase 4 — Rust Integration

- Implement the Rust crate.
- Define the Python–Rust interface.
- Expose the required functions using PyO3.
- Build the extension with Maturin.
- Compare Python and Rust results using shared test fixtures.

**Completion criterion:** Both implementations agree on the supported scheduling semantics.

### Phase 5 — Desktop Interface

- Build the main application window.
- Add workload editing and policy selection.
- Display execution timelines.
- Add simulation controls.
- Present metrics and policy comparisons.

**Completion criterion:** Users can run and inspect experiments without modifying source code.

### Phase 6 — Persistence and Release

- Add SQLite persistence.
- Expand regression tests.
- Benchmark both implementations.
- Document installation and usage.
- Prepare screenshots and a release.

**Completion criterion:** The project can be installed, tested, demonstrated, and evaluated by another developer.

---

## Testing and Quality

Correctness takes priority over optimization.

The test suite will cover:

- Invalid process configurations
- Duplicate process identifiers
- Processes with different arrival times
- Equal burst durations and priorities
- Idle periods
- Empty and single-process workloads
- Process completion and state transitions
- Metric calculations
- Dependency validation, when dependencies are supported
- Consistency between Python and Rust implementations

Tests should use small workloads with manually verifiable expected results.

For example, a test can define three processes, calculate their expected execution order and completion times by hand, and verify that the simulation produces those results.

Cross-engine tests should use the same input fixtures and compare normalized results. Floating-point metrics should use an appropriate tolerance where necessary.

---

## Performance Benchmarking

Performance is a measurable engineering objective, not an assumption.

The planned benchmark process will:

1. Generate reproducible workloads at several sizes.
2. Run identical workloads through the Python and Rust engines.
3. Verify that the results are equivalent.
4. Measure execution time over repeated runs.
5. Report workload size, runtime, and environmental conditions.
6. Calculate speedup where the measurements support a meaningful comparison.

Speedup is calculated as:

\[
\text{Speedup} =
\frac{\text{Python execution time}}
{\text{Rust execution time}}
\]

A speedup greater than 1 indicates that Rust completed the measured operation faster in that experiment.

Benchmarks should distinguish the simulation kernel from end-to-end application overhead. Python–Rust conversion costs, workload generation, and visualization should not be silently mixed into kernel-only measurements.

No performance improvement is claimed until it has been measured.

---

## Development Roadmap

| Milestone | Primary outcome |
|---|---|
| M1 | Domain models and validation |
| M2 | Working scheduling policies |
| M3 | Deterministic simulation engine |
| M4 | Metrics and execution traces |
| M5 | Rust implementation and bindings |
| M6 | Interactive visualization |
| M7 | Persistence and experiment comparison |
| M8 | Benchmarks, documentation, and release |

The milestones describe the intended sequence. Actual completion should be reflected in repository issues, release notes, and this README.

---

## Contributing

Contributions are welcome once the repository's contribution guidelines and initial implementation are established.

### Areas for contribution

- Scheduling algorithms
- Simulation correctness and edge cases
- Performance benchmarking
- Python–Rust interoperability
- Timeline visualization
- Testing and documentation
- Usability improvements

### Suggested workflow

1. Open an issue describing the proposed change.
2. Discuss the intended behavior and relevant design decisions.
3. Create a focused branch.
4. Implement the change with appropriate tests.
5. Run the available quality checks.
6. Open# Quezo

### A visual playground for scheduling algorithms, workload simulation, and performance analysis.

Quezo is an open-source scheduling simulator designed to explore how scheduling policies behave under different workloads. It combines Python's flexibility, Rust's performance, and interactive visualization to make scheduling decisions observable, measurable, and comparable.

The goal is to build a tool where users can define workloads, simulate their execution, inspect process timelines, compare scheduling policies, and understand the trade-offs behind each algorithm.

> **Project status:** Early development. Features listed in the roadmap are planned unless explicitly marked as implemented.

---

## Table of Contents

- [Overview](#overview)
- [Why Quezo?](#why-quezo)
- [Core Features](#core-features)
- [How It Works](#how-it-works)
- [Scheduling Algorithms](#scheduling-algorithms)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Testing and Quality](#testing-and-quality)
- [Performance Benchmarking](#performance-benchmarking)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [Design Principles](#design-principles)
- [License](#license)

---

## Overview

Scheduling is the process of deciding which task should execute, when it should execute, and how available resources should be allocated.

Different scheduling policies produce different outcomes. One may minimize average waiting time, another may prioritize urgent work, while another may favor tasks that arrived earlier.

Quezo aims to make these differences visible through reproducible simulations and measurable results.

With Quezo, the intended workflow is:

1. Define a workload containing processes, arrival times, burst durations, and priorities.
2. Select a scheduling policy.
3. Run a simulation.
4. Inspect the execution timeline and process states.
5. Analyze performance metrics.
6. Repeat the experiment with another policy.
7. Compare the results using the same workload.

The initial focus is CPU-style process scheduling. The architecture may later support broader scheduling experiments, subject to the requirements and limitations of each model.

## Why Quezo?

Scheduling algorithms are often taught through static tables and manually calculated examples. These methods explain the basics, but they make it difficult to explore larger workloads or understand how changing input parameters affects the result.

Quezo aims to bridge that gap.

- **Experiment instead of guessing:** Run different policies against identical workloads.
- **Visualize execution:** Inspect when processes start, run, and finish.
- **Measure trade-offs:** Compare waiting time, turnaround time, throughput, and utilization.
- **Learn through implementation:** Explore object-oriented design, simulation architecture, and algorithm behavior.
- **Investigate performance:** Compare a Python reference implementation with a Rust implementation using reproducible benchmarks.

Quezo is intended as both an educational tool and a practical software engineering project.

---

## Core Features

The following capabilities define the planned initial release.

### 1. Workload Modeling

Create workloads containing processes with configurable attributes.

| Attribute | Description |
|---|---|
| Process ID | Unique identifier for a process |
| Arrival time | Time at which a process becomes available |
| Burst duration | CPU time required for completion |
| Priority | Scheduling priority assigned to the process |
| Dependencies | Optional relationships that constrain execution order |

Input validation will prevent invalid configurations from entering the simulation engine.

### 2. Scheduling Policies

The initial implementation is planned to include:

- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling

The first version will focus on non-preemptive policies. Preemptive algorithms and additional scheduling strategies can be introduced after the core simulation engine is validated.

### 3. Simulation Engine

The simulation engine will manage:

- Simulated time
- Process arrival and completion
- Ready queues
- Worker availability
- Process state transitions
- Execution intervals
- Simulation results

The engine will use simulated time rather than real-time delays, allowing experiments to run quickly and reproducibly.

### 4. Interactive Visualization

The planned desktop interface will provide:

- A workload editor
- Scheduling policy selection
- A Gantt-style execution timeline
- Current simulation time and process states
- Step, pause, reset, and replay controls
- Metric summaries and policy comparisons

### 5. Performance Metrics

Quezo will calculate and present metrics such as:

- Waiting time
- Turnaround time
- Completion time
- Response time, where applicable
- Throughput
- CPU utilization

Metrics will be calculated from the execution trace, keeping the measurement logic separate from the scheduling policies.

### 6. Experiment Comparison

Users will be able to execute multiple policies against the same workload and compare their outcomes.

This will make it possible to investigate questions such as:

- Which policy produces the lowest average waiting time for a particular workload?
- How do long-running tasks affect shorter tasks?
- What happens when process priorities change?
- How does idle time affect utilization?
- Does the Rust implementation improve execution time for larger workloads?

The results will be based on measured data rather than assumptions about which algorithm is universally best.

### 7. Persistence

SQLite integration is planned to support saving and loading workloads and experiment results, making it easier to reproduce and revisit experiments.

---

## How It Works

Quezo separates workload definition, scheduling decisions, execution, and analysis.

```text
        Workload Configuration
                  |
                  v
          Input Validation
                  |
                  v
         Simulation Engine
                  |
           +------+------+
           |             |
           v             v
    Python Engine    Rust Engine
           |             |
           +------+------+
                  |
                  v
          Execution Trace
                  |
           +------+------+
           |             |
           v             v
      Metrics       Timeline Data
           |             |
           +------+------+
                  |
                  v
          Visualization UI
```

The Python engine will act as the reference implementation. The Rust engine will implement the same supported behavior through a defined interface.

Both engines should produce equivalent results for identical workloads and scheduling configurations.

The interface will consume structured results rather than depending on the internal implementation of either engine.

---

## Scheduling Algorithms

### First-Come, First-Served (FCFS)

Processes are selected in arrival order.

**Strengths**
- Simple to understand and implement.
- Predictable execution order.
- Low scheduling complexity.

**Limitations**
- A long-running process can delay shorter processes.
- Average waiting time can be high for some workloads.

### Shortest Job First (SJF)

Among currently available processes, the process with the shortest burst duration is selected.

**Strengths**
- Can reduce average waiting time for suitable workloads.
- Demonstrates the impact of workload characteristics on scheduling decisions.

**Limitations**
- Requires knowledge or estimates of burst durations.
- Long tasks may experience extended delays when short tasks repeatedly arrive.

### Priority Scheduling

The scheduler selects the available process with the highest configured priority.

**Strengths**
- Models workloads with different levels of importance.
- Makes priority-based trade-offs observable.

**Limitations**
- Low-priority processes may wait for a long time.
- Priority inversion and starvation require additional mechanisms to address in more advanced implementations.

The initial version will define a consistent priority convention and deterministic tie-breaking rules so that experiments remain reproducible.

---

## Architecture

Quezo will use a modular architecture with explicit responsibilities.

### Domain Layer

Defines the core data structures, configuration, and validation rules.

### Scheduling Layer

Implements interchangeable scheduling policies through a common interface. Policies decide which eligible process should run next without owning the entire simulation lifecycle.

### Simulation Layer

Coordinates simulated time, process state transitions, worker availability, and execution events.

### Metrics Layer

Calculates statistics from completed simulations without coupling metric calculations to individual scheduling algorithms.

### Application Layer

Coordinates workloads, simulations, experiments, persistence, and communication with the user interface.

### Rust Execution Layer

Provides an optimized implementation of selected computational operations through Python–Rust interoperability.

### Presentation Layer

Displays configuration controls, execution timelines, process states, and analytical results.

This separation is intended to make the system easier to test, extend, and maintain.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Domain models, application logic, reference simulation |
| Rust | Performance-oriented simulation implementation |
| PyO3 | Exposing Rust functionality to Python |
| Maturin | Building and packaging the Rust extension |
| PySide6 | Desktop user interface |
| SQLite | Workload and experiment persistence |
| uv | Python dependency and environment management |
| Ruff | Python linting and formatting |
| pytest | Automated testing |
| mypy | Optional static type checking |
| Cargo | Rust dependency management, builds, and tests |
| Git and GitHub | Version control and collaboration |

The stack is intentionally split by responsibility. Rust will be introduced after the Python behavior is sufficiently well-defined to provide a reliable correctness baseline.

---

## Project Structure

The planned repository layout is:

```text
Quezo/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── quezo/
│       ├── __init__.py
│       ├── models.py
│       ├── policies.py
│       ├── validator.py
│       ├── engine.py
│       ├── metrics.py
│       ├── experiments.py
│       ├── repository.py
│       └── ui/
│           ├── main_window.py
│           ├── timeline.py
│           └── workload_editor.py
├── rust_engine/
│   ├── Cargo.toml
│   └── src/
│       └── lib.rs
├── tests/
│   ├── test_models.py
│   ├── test_policies.py
│   ├── test_engine.py
│   └── test_metrics.py
└── docs/
    └── design.md
```

This structure is a design target, not a claim that every module already exists.

---

## Getting Started

### Prerequisites

Install the following tools:

- Python 3
- uv
- Rust toolchain through rustup
- Git

The desktop interface and Rust bindings will be introduced as their corresponding development phases begin.

### 1. Clone the repository

Replace the placeholder with the actual repository URL.

```bash
git clone <YOUR_REPOSITORY_URL>
cd Quezo
```

### 2. Create the Python environment

If the repository already contains a `pyproject.toml`:

```bash
uv sync --dev
```

If you are creating the project from scratch:

```bash
uv init
uv add --dev pytest ruff maturin mypy pytest-cov
```

Use the existing project configuration rather than reinitializing an already configured repository.

### 3. Verify the development tools

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

These commands are intended to run once the initial source and test structure exists. An empty or incomplete project may not yet pass all checks.

### 4. Verify Rust

Install Rust through the official rustup installation instructions if it is not already installed.

Then run:

```bash
rustc --version
cargo --version
```

### 5. Build and run

The exact application launch command will be documented once the initial executable entry point is implemented.

Until then, development should begin with the domain models, scheduling policies, and automated tests.

---

## Development Workflow

Quezo is being developed incrementally. Each phase should produce a working, testable result.

### Phase 1 — Foundation and Domain Modeling

- Establish the package structure.
- Define process and simulation models.
- Implement input validation.
- Add unit tests for valid and invalid configurations.

**Completion criterion:** Workloads can be represented and validated independently of the interface.

### Phase 2 — Scheduling Policies

- Define a common policy interface.
- Implement FCFS, SJF, and Priority Scheduling.
- Define deterministic tie-breaking behavior.
- Test policies against hand-calculated examples.

**Completion criterion:** Policies can be swapped without rewriting the simulation engine.

### Phase 3 — Simulation and Metrics

- Implement the simulation loop.
- Track process arrivals, execution, and completion.
- Record execution intervals.
- Calculate performance metrics.
- Test edge cases and reproducibility.

**Completion criterion:** Known workloads produce correct execution traces and metrics.

### Phase 4 — Rust Integration

- Implement the Rust crate.
- Define the Python–Rust interface.
- Expose the required functions using PyO3.
- Build the extension with Maturin.
- Compare Python and Rust results using shared test fixtures.

**Completion criterion:** Both implementations agree on the supported scheduling semantics.

### Phase 5 — Desktop Interface

- Build the main application window.
- Add workload editing and policy selection.
- Display execution timelines.
- Add simulation controls.
- Present metrics and policy comparisons.

**Completion criterion:** Users can run and inspect experiments without modifying source code.

### Phase 6 — Persistence and Release

- Add SQLite persistence.
- Expand regression tests.
- Benchmark both implementations.
- Document installation and usage.
- Prepare screenshots and a release.

**Completion criterion:** The project can be installed, tested, demonstrated, and evaluated by another developer.

---

## Testing and Quality

Correctness takes priority over optimization.

The test suite will cover:

- Invalid process configurations
- Duplicate process identifiers
- Processes with different arrival times
- Equal burst durations and priorities
- Idle periods
- Empty and single-process workloads
- Process completion and state transitions
- Metric calculations
- Dependency validation, when dependencies are supported
- Consistency between Python and Rust implementations

Tests should use small workloads with manually verifiable expected results.

For example, a test can define three processes, calculate their expected execution order and completion times by hand, and verify that the simulation produces those results.

Cross-engine tests should use the same input fixtures and compare normalized results. Floating-point metrics should use an appropriate tolerance where necessary.

---

## Performance Benchmarking

Performance is a measurable engineering objective, not an assumption.

The planned benchmark process will:

1. Generate reproducible workloads at several sizes.
2. Run identical workloads through the Python and Rust engines.
3. Verify that the results are equivalent.
4. Measure execution time over repeated runs.
5. Report workload size, runtime, and environmental conditions.
6. Calculate speedup where the measurements support a meaningful comparison.

Speedup is calculated as:

\[
\text{Speedup} =
\frac{\text{Python execution time}}
{\text{Rust execution time}}
\]

A speedup greater than 1 indicates that Rust completed the measured operation faster in that experiment.

Benchmarks should distinguish the simulation kernel from end-to-end application overhead. Python–Rust conversion costs, workload generation, and visualization should not be silently mixed into kernel-only measurements.

No performance improvement is claimed until it has been measured.

---

## Development Roadmap

| Milestone | Primary outcome |
|---|---|
| M1 | Domain models and validation |
| M2 | Working scheduling policies |
| M3 | Deterministic simulation engine |
| M4 | Metrics and execution traces |
| M5 | Rust implementation and bindings |
| M6 | Interactive visualization |
| M7 | Persistence and experiment comparison |
| M8 | Benchmarks, documentation, and release |

The milestones describe the intended sequence. Actual completion should be reflected in repository issues, release notes, and this README.

---

## Contributing

Contributions are welcome once the repository's contribution guidelines and initial implementation are established.

### Areas for contribution

- Scheduling algorithms
- Simulation correctness and edge cases
- Performance benchmarking
- Python–Rust interoperability
- Timeline visualization
- Testing and documentation
- Usability improvements

### Suggested workflow

1. Open an issue describing the proposed change.
2. Discuss the intended behavior and relevant design decisions.
3. Create a focused branch.
4. Implement the change with appropriate tests.
5. Run the available quality checks.
6. Open