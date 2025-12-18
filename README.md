# Q-Learning for Move Operator Selection in Genetic Algorithms

## Project Overview

This project investigates the use of **Q-Learning** as a reinforcement learning mechanism for **dynamic selection of genetic operators** within a **Genetic Algorithm (GA)**.  
The main goal is to replace **static operator scheduling** with a Q-learning agent that dynamically chooses crossover and mutation operators during the evolutionary process.

The work compares a **standard Genetic Algorithm with fixed operators** against a **GA enhanced with a Q-learning agent**, focusing on solution quality, stability, and sensitivity to hyperparameter configuration.

---

## Motivation

In classical Genetic Algorithms, crossover and mutation operators are typically chosen **statically** before the algorithm starts. However, different operators may be more effective at different stages of the evolutionary process.

This project explores whether **reinforcement learning**, specifically Q-learning, can be used to adaptively select genetic operators and reduce the dependence on carefully tuned static configurations.

---

## Methodology

### Genetic Algorithm

- Metaheuristic: **Genetic Algorithm**
- Standard evolutionary cycle:
  - Selection
  - Crossover
  - Mutation
  - Replacement

Two approaches are evaluated:
- **Static GA**: crossover and mutation operators are fixed throughout the run
- **Q-learning GA**: operator selection is controlled by a Q-learning agent

---

### Q-Learning Component

- **Agent role**: Select crossover and mutation operators
- **Action space**: Set of available genetic operators
- **State space**: Characteristics of the current evolutionary process (e.g. generation progress, fitness improvement)
- **Reward function**: Change in fitness after applying a selected operator

The agent updates its policy online using the standard Q-learning update rule.

---

### Hyperparameter Tuning

Hyperparameters for both the Genetic Algorithm and the Q-learning component (e.g. learning rate, discount factor, exploration rate) were determined through **systematic hyperparameter tuning in R**, rather than being manually fixed.

This tuning process allowed an objective comparison between static and adaptive approaches and reduced bias introduced by arbitrary parameter choices.

---

## Experimental Results

The experimental evaluation revealed a trade-off between **solution quality** and **stability**:

- The **static Genetic Algorithm**:
  - Achieved better best-case solutions
  - Was highly sensitive to hyperparameter configuration
  - Exhibited a large performance variance across different configurations

- The **Q-learning-based Genetic Algorithm**:
  - Produced worse average and best solutions
  - Demonstrated significantly higher stability
  - Was less sensitive to hyperparameter choices, with a narrower performance range

---

## Discussion

While the Q-learning-based approach didn't outperform the static GA in terms of raw optimization performance, it showed an important advantage in terms of robustness.  
The static GA can yield excellent results when well-tuned, but small changes in configuration can lead to drastically different outcomes.

In contrast, the Q-learning-enhanced GA adapts its operator selection dynamically, resulting in more consistent, though generally weaker, solutions.

---

## Conclusion

This study demonstrates that:
- Static operator selection can achieve superior results when carefully tuned
- Q-learning-based operator selection provides increased robustness and reduced sensitivity to configuration
- There exists a clear trade-off between peak performance and stability

Although Q-learning did not outperform the static approach in this work, it represents a promising direction for problems where manual tuning is difficult or where consistent performance is preferred over optimal but unstable solutions.


