# Broken Telephone Translation Chain

This project implements a Level 4 autonomous translation agent system based on Dr. Yoram Segal's Lesson 5 principles.

## Structure
- **Agent_Folder/**: Contains project governance (PRD, PLAN, TODO).
- **.claude/skills/**: Contains the specialized expert personas.## How to Run
To execute the autonomous translation chain, ensure you have Node.js installed and run:
`node orchestrator.js`

## Level 4 Achievement: Autonomous Orchestration
This project reaches **Level 4** by implementing an **Orchestrator** that acts as the system's **"Brain" (CPU)** [2, 3]. 
- **Autonomous Adaptation:** When the system detected a failure in the Python environment (Microsoft Store dummy link), the agent autonomously pivoted the entire infrastructure to **Node.js** to ensure mission success.
- **Skill Management:** The Orchestrator automatically calls specialized **Skills** (found in `/.claude/skills/`) which act as expert personas for each language [3, 4].

## Success Metrics: Vector Distance
The goal of this "Broken Telephone" system is to maintain semantic meaning across the chain [5, 6].
- **Metric:** We measure the **Vector Distance** (Semantic Drift) between the original and final English sentences [6, 7].
- **Goal:** Aiming for a **Vector Distance of 0**, representing perfect semantic alignment [6].

## Management Advantage (Prompt Engineering)
As the project manager, I utilized advanced techniques to oversee quality [8]:
- **Experts Committee:** To define the logic for each translation step [9].
- **Specific Instructions:** To balance creativity and accuracy [10].
- **Handling the U-Phenomenon:** Ensuring the orchestrator maintains focus on the goal despite the complexity of the chain [11, 12].
