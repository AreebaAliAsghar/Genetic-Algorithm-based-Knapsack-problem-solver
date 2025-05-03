# 🧬 Genetic Algorithm for 0/1 Knapsack Problem

This project solves the classic **0/1 Knapsack Problem** using a **Genetic Algorithm (GA)**. The algorithm evolves a population of possible solutions using biologically inspired operations like **selection**, **crossover**, and **mutation**.

---

## 📦 Problem Description

Given:
- A list of items, each with a value and weight.
- A maximum weight capacity of the knapsack.

Goal:
- Select a subset of items such that the **total value is maximized** without exceeding the weight limit.

---

## 🧠 How It Works

- **Chromosome Representation**: Each chromosome is a binary list where `1` indicates an item is selected.
- **Fitness Function**: Calculates total value if weight is within limit, else returns 0.
- **Selection**: Top 50% of the population (elitism).
- **Crossover**: Single-point crossover.
- **Mutation**: Random bit flipping with a defined mutation rate.
- **Evolution**: Repeats for 50 generations to improve solution quality.

---

