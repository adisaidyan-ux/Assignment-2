"""
eval_drift.py - The "Hands" of the Broken Telephone Agent
---------------------------------------------------------
Role: This script acts as a specialized Tool (O/I) within the Agent Infrastructure. 
It provides empirical feedback to the Orchestrator regarding semantic drift.

Architectural Context (L05): 
The Orchestrator (Brain) uses this Tool (Hands) to measure if the 
"Semantic Cloud" was preserved throughout the translation chain.
"""

import sys
import json
import re

class SemanticJudge:
    def __init__(self):
        self.committee_experts = [
            "Nils Reimers (Embeddings)",
            "Rachel Tatman (Linguistics)",
            "Anis Ayari (LLM-as-a-Judge)"
        ]

    def create_judge_prompt(self, original, final):
        """
        Generates a sophisticated prompt for the LLM to act as a Semantic Judge.
        This prompt focuses on the 'Semantic Cloud' rather than literal words.
        """
        prompt = f"""
        ### ROLE: Senior Semantic Evaluation Committee
        Act as a committee of 5 AI Evaluation experts. Your task is to compare two English sentences.

        ### INPUTS:
        - Original Sentence: "{original}"
        - Final Translation: "{final}"

        ### EVALUATION CRITERIA (The Semantic Cloud):
        1. CORE INTENT: Is the primary message identical?
        2. SENTIMENT & TONE: Does the emotional temperature match (e.g., sarcasm, urgency)?
        3. IDIOMATIC EQUIVALENCE: If an idiom was used, was its cultural meaning preserved?
        4. NUANCE: Are there any "hallucinated" additions or "lost" details?

        ### OUTPUT FORMAT:
        You must output a JSON object with the following fields:
        - "intent_score": (0.0 - 1.0)
        - "sentiment_score": (0.0 - 1.0)
        - "idiom_score": (0.0 - 1.0)
        - "total_drift_score": (A weighted average where Intent is 60%, Sentiment 20%, Nuance 20%)
        - "reasoning": A brief explanation of the drift.

        Final total_drift_score: 1.0 = Zero Distance, 0.0 = Total Loss of Meaning.
        """
        return prompt

    def calculate_drift(self, original, final):
        """
        Executes the drift calculation. 
        In a full Level 4 system, this would trigger an LLM call using the prompt above.
        For this tool, we provide the logic framework.
        """
        # Clean the input
        s1 = original.strip().lower()
        s2 = final.strip().lower()

        # Mock/Fallback logic for standalone execution (String similarity)
        # In production, this is replaced by the LLM-as-a-Judge result.
        if s1 == s2:
            return 1.0
        
        # Simple overlap coefficient as a basic fallback
        words1 = set(s1.split())
        words2 = set(s2.split())
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0

def main():
    if len(sys.argv) < 3:
        print(json.dumps({
            "error": "Missing input. Usage: python eval_drift.py 'Original' 'Final'",
            "drift_score": 0.0
        }))
        return

    original = sys.argv[1]
    final = sys.argv[2]
    
    judge = SemanticJudge()
    
    # In a Level 4 chain, the Orchestrator would take this prompt 
    # and send it to the LLM to get the 'total_drift_score'.
    prompt = judge.create_judge_prompt(original, final)
    
    # Standalone execution returns the framework result
    score = judge.calculate_drift(original, final)
    
    result = {
        "original": original,
        "final": final,
        "drift_score": round(score, 4),
        "status": "Success" if score > 0.85 else "Needs Retry",
        "instruction": "If drift_score < 0.85, the Orchestrator MUST trigger a Skill retry loop.",
        "judge_prompt_preview": prompt[:150] + "..."
    }
    
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
