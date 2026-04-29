# DT-Reflection-Tree-Project
Deterministic Reflection Tree Agent built for the DT Fellowship Role Simulation. Uses Python and JSON to engineer knowledge-driven reflection paths based on Locus of Control and Altrocentrism.

*A Fellowship Assignment for DT-CultureTech*

## Overview
This is a deterministic reflection tool designed to help employees process their day through three psychological axes:
1. **Locus of Control** (Victim vs Victor)
2. **Orientation** (Contribution vs Entitlement)
3. **Radius of Concern** (Self vs Altrocentric)

## Project Structure
- `/tree`: Contains the deterministic logic in JSON format.
- `/agent`: A Python-based runner to walk through the tree (No LLM runtime).
- `write-up.md`: Detailed rationale and psychological grounding.

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Run the agent using:
   ```bash
   python agent/main.py
