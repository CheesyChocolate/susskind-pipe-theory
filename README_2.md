A revised version of the original proposal. The decision to change the proposal
to this one is not final.

---

# susskind-pipe-theory

Leveraging graph theory and reinforcement learning to find the input for a
desired output in a pipe maze.

## Problem Statement

A maze of water pipes with multiple inputs and outputs. The goal is to connect
the input to the output. The maze is a grid of pipes, where each pipe has a
direction and a connector. Connectors link to other pipes. The maze is randomly
generated, with inputs and outputs randomly placed on its border. The aim is to
release water only from specified outputs by determining which input to open to
achieve this. Extensions include considering water flow dynamics such as
gravity and pressure, and the behavior at multi-way junctions.

### Problem Description

The maze consists of multiple input water sources and output water sinks.
Hidden layers of junction nodes connect inputs and outputs via pipes. Each sink
has a maximum water capacity, and overflow should be avoided at the last sink.
Water flow divides at junctions based on downstream pipe capacity. Pipes vary
in capacity and behavior, with some susceptible to blockage or breaking,
affecting water distribution. The goal is to find input sources that achieve
the desired water output.

The simulation should include real-time visualization, accounting for pressure,
gravity, and flow rates.

### Approach

Graph Theory:
- Represent the maze as a graph with nodes (junctions and sinks) and edges
(pipes).
- Use algorithms like BFS, DFS, or Dijkstra's to identify possible paths.

Reinforcement Learning:
- Model the problem as an RL task, with input sources as actions and water
amounts at outputs as rewards.
- Train the agent using Q-learning or Monte Carlo methods to optimize the
policy for desired outputs.

Challenges:
- Unknown maze depth can prolong algorithm runtime.
- Finding an optimal policy in complex mazes is NP-hard.

### Input and Output

Input:
- List of node IDs, their relationships, and pipe details, similar to TSP
problem input.
- Desired water amounts at output sinks, which can be generated or provided via
file/command line.

Output:
- Optimal input sources and corresponding pressures/timings to achieve desired
water outputs.
- Results displayed in the console or saved to a file.

### Evaluation

- Time to find the optimal policy.
- Accuracy of the policy in achieving desired water distribution.

### Extensions

- Customizable nodes in hidden layers to adjust water pressure.
- Time limits or priorities for output sinks.
- Output sinks consuming water at a rate over time.

### Relatable Problems

- Design of computer networks and web connections.
- Internal structure of circuits or chips.
- Understanding brain connectivity and developing computer models mimicking the
brain.

### Other Notes

### Project Name

Named after Leonard Susskind, a theoretical physicist who developed the
holographic principle, which suggests that a volume of space can be encoded on
a lower-dimensional boundary. The reason for this name choice remains a
mystery.
