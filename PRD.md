# PRD: 'Broken Telephone' AI Translation Chain (Level 4)

## 1. Executive Summary
**Project Name:** Broken Telephone Semantic Guard
**Objective:** Execute a multi-lingual translation chain (EN -> FR -> HE -> EN) while maintaining near-zero semantic drift.
**Architectural Level:** Level 4 (Autonomous Orchestrator with Specialized Skills).

## 2. The Experts Committee
The system is designed based on the consensus of:
1. **Andrej Karpathy:** Tokenization & Transformer optimization.
2. **Andrew Ng:** Quality assurance and system iteration.
3. **Harrison Chase:** Chain orchestration logic.
4. **Jerry Liu:** Data structure and vector indexing.
5. **Ilya Sutskever:** Deep semantic robustness.
6. **Sam Altman:** User experience and scaling.
7. **Demis Hassabis:** Multi-step strategic reasoning.
8. **Noam Brown:** Self-correction and search-based refinement.
9. **Fei-Fei Li:** Contextual and cultural world-modeling.
10. **Yann LeCun:** Objective-driven AI architecture.

## 3. System Architecture
Following the "Agent Infrastructure" (L05), the system is composed of:

### 3.1. Autonomous Orchestrator (The Conductor)
*   **Role:** Manages the session (`Context Window`).
*   **Logic:** Instead of a linear script, the Orchestrator evaluates each translation step before proceeding. If a translation is deemed "semantically unstable," it requests a retry from the skill.

### 3.2. Specialized Skills (`.claude/skills/`)
Each node in the chain is a discrete **Skill** with its own `Skill.md` (System Prompt) and `Tools`:
1.  **Skill: En_Fr_Linguist:** Focuses on idiomatic preservation.
2.  **Skill: Fr_He_Scholar:** Focuses on grammatical and cultural mapping.
3.  **Skill: He_En_Editor:** Focuses on reconstructing the original intent.

### 3.3. Memory & Context
*   **Short-term (RAM):** The `Context Window` stores the trace of all translations.
*   **RAG (The Library):** A reference tool containing common idioms in all three languages to prevent literal translation errors.

## 4. Requirements & Success Metrics
*   **Chain Path:** English ➔ French ➔ Hebrew ➔ English.
*   **Primary Metric:** Semantic Similarity.
*   **Technical Success Metric:** Vector Distance $d \approx 0$ between $S_{original}$ and $S_{final}$.
*   **Evaluation Tool:** A Python script utilizing `sentence-transformers` or LLM-based semantic evaluation to measure the cosine similarity between the first and last sentences.

## 5. Execution Protocol (The "Act As" Strategy)
1.  **Phase 1 (Ingestion):** Orchestrator receives the English sentence.
2.  **Phase 2 (Specialized Translation):**
    *   Call `En_Fr_Linguist` using the "Committee of Experts" prompt.
    *   Call `Fr_He_Scholar` to bridge the Romance and Semitic linguistic gap.
    *   Call `He_En_Editor` to finalize the loop.
3.  **Phase 3 (Evaluation):** The Orchestrator calls the `Evaluation Tool`.
4.  **Phase 4 (Reporting):** Display the original sentence, the chain journey, the final sentence, and the Vector Distance score.

## 6. Risk Mitigation (Lesson 5 Insights)
*   **Lost in the Middle:** Key instructions are placed at the *start* and *end* of the prompt.
*   **Hallucinations:** Skills are instructed to provide "Zero-Shot" translations first, followed by a "Self-Correction" pass.
*   **Forest of Paths:** The Orchestrator is biased toward "semantic constancy" rather than "lexical accuracy."
