# Technical Implementation Plan: 'Broken Telephone' Level 4 System

## 1. System Architecture (The Four Pillars)

### 1.1. The Brain (LLM)
*   **Engine:** Gemini/Claude acting as the core reasoning unit.
*   **Strategy:** Utilize "System 2 Reasoning" (Chain of Thought) for each translation step.
*   **Prompting:** Every call will include an "Act As" persona and a "Committee of 10 Experts" validation block to ensure high-fidelity output.

### 1.2. Memory (Context Window Management)
*   **Session Management:** The Orchestrator will maintain a `session_log.json` to track the state of the conversation.
*   **Prompt Caching:** To minimize latency and tokens, the core "Committee of Experts" instructions will be cached at the start of the context window.
*   **Structure:** $ContextWindow_n = S + Skills + (P_1 + RAG_1) + A_1 ... + (P_n + RAG_n) + A_n$.

### 1.3. Tools (Python Evaluation)
*   **Tool Name:** `eval_drift.py`
*   **Function:** Measures the semantic distance between the input English sentence ($S_{start}$) and the final output ($S_{end}$).
*   **Method:** 
    *   *Primary:* LLM-as-a-Judge (Semantic Similarity Score 1-10).
    *   *Secondary:* Cosine Similarity via embedding vectors (if environment permits).

### 1.4. RAG (The Knowledge Base)
*   **Source:** `L05-Agent-infrasr.pdf` and a curated `idioms_vault.json`.
*   **Usage:** Before translation, the Skill queries the RAG to check if the input contains known "Semantic Traps" (idioms that fail literal translation).

---

## 2. Development Phases

### Phase 1: Environment Setup (PowerShell)
1.  **Directory Initialization:** 
    *   Set up `.claude/skills/` hierarchy.
    *   Create `logs/` directory for session persistence.
2.  **Dependency Management:** 
    *   Initialize a Python virtual environment.
    *   Install necessary libraries: `numpy`, `scikit-learn` (for vector math), or utilize API calls for embeddings.

### Phase 2: Skill Engineering (The Personas)
1.  **EN_FR_Expert:** 
    *   *Goal:* Preserve the "Baguette" (French cultural nuance).
    *   *Implementation:* Write `Skill.md` with instructions to prioritize idiomatic equivalence over literal words.
2.  **FR_HE_Scholar:** 
    *   *Goal:* Navigate the transition from Indo-European to Semitic logic.
    *   *Implementation:* Skill focus on Hebrew "Rua'h HaSafah".
3.  **HE_EN_Editor:** 
    *   *Goal:* The Final Guard.
    *   *Implementation:* Instructed to perform "Back-Translation Analysis" to guess the original intent.

### Phase 3: Evaluation & Orchestration
1.  **The Orchestrator Logic:** 
    *   Implement a "Retry Loop": If `eval_drift.py` returns a score $< 0.85$, the Orchestrator instructs the chain to re-translate the offending segment.
2.  **Final Validation:** 
    *   Run a batch of 10 test cases (Idioms, Technical Specs, Emotional Prose).
    *   Calculate the Average Vector Distance across the batch.

---

## 3. Risk Management
*   **Lost in the Middle:** All critical constraints (Success Metrics) will be repeated in the `A_n` (final output) instructions of each skill.
*   **Hallucinations:** Any translation that adds info not in the original will be flagged by the Orchestrator's "Fact-Checker" tool.
