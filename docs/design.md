# Quezo System Design

## 1. Purpose

Quezo simulates CPU job scheduling and lets users assign jobs to one or more
workers.

## 2. Inputs

Users provide processes with the following attributes:

1. Process ID
2. Arrival time
3. Burst time
4. Priority
5. Dependencies

## 3. Processing

The simulator accepts processes as input and creates a workload. Users select
an algorithm: FCFS, SJF, or Priority Scheduling. Quezo then visualizes how the
selected algorithm schedules processes on the CPU.

## 4. Outputs

Simulation results should include a Gantt chart, the scheduled jobs, and
performance metrics. A Python and Rust benchmark can be shown after both
engines are implemented.

## 5. Core Concepts

- **Process:** A job that is assigned to the CPU.
- **Scheduling policy:** Rules that determine which eligible process runs
  next.
- **Simulation configuration:** A file containing the processes and
  algorithms for a simulation.
- **Execution interval:** The time during which a process runs on a worker.
- **Simulation result:** A summary of the simulation, including metrics and
  benchmarks.

## 6. Constraints

Process scheduling values must not be negative. Input validation will enforce
this rule and validate process IDs and dependency references according to the
data model.

Additional invariants will be defined as the simulation behavior is
implemented.

## 7. Out of Scope for the MVP

The desktop UI and Rust engine are outside the scope of the MVP.
