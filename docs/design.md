
# Quezo — System Design

## 1. Purpose
This is a simulation of CPU job scheduling in which you can assinge jobs to multiple workers.

## 2. Inputs
- User provides a process with
1. process id  
2. arrival time  
3. burst time  
4. priority  
5. dependencies  

## 3. Processing
So basically what we do is we give take processes as an input from user, and create a workload,
then we give the user the freedom of selecting a algorithm. FCFS, SJF or Priority Scheduling. 
We then simulate visually how these algorithms work in the CPU.

## 4. Outputs
What should the user see after a simulation?
After the simulation user should see a gannt chart, scheduled job and a benchmark between python and rust.


## 5. Core concepts
- Process:
 A simple process that will be assinged to CPU. 
- Scheduling policy:
    In this we will have to write policies about scheduling.(I don't understand much about this.)
- Simulation configuration:  
    A simulation config, which will have process and the algorithms,
    basically a file which contains the assests to execute a simulation.
- Execution interval:
    Depends entirely on processes and jobs.
- Simulation result:
    A visual and statical result and benchamarks.

## 6. Constraints

A process which contains any of the variable in negative considers invalid.  
We are using validation of that as well.   

What behavior must always be correct?(I'll figure this out.)

## 7. Out of scope for the MVP
What features will not be implemented yet?
The desktop UI, and rust engine.
