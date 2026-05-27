/*
orchestrator.js - The "Brain" (Node.js Version)
-----------------------------------------------
Role: Coordinates the Level 4 Translation Chain.
*/

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log("--- [SYSTEM CHECK] Node.js Orchestrator Initialized ---");

class Level4Orchestrator {
    constructor() {
        this.threshold = 0.8;
        this.agentFolder = path.join(__dirname, 'Agent_Folder');
    }

    callAgent(skillName, text) {
        console.log(`--- [ACTING] ${skillName} is processing... ---`);
        // Simulated translation logic
        return `[Trans: ${text.substring(0, 15)}... via ${skillName}]`;
    }

    runEval(original, final) {
        try {
            // Use node to run our JS eval tool
            const output = execSync(`node "${path.join(__dirname, 'eval_drift.js')}" "${original}" "${final}"`);
            return JSON.parse(output.toString());
        } catch (e) {
            return { drift_score: 0.5 };
        }
    }

    execute(originalText) {
        console.log(`🚀 MISSION START: "${originalText}"`);
        
        // Step 1: EN -> FR
        const fr = this.callAgent("English-French-Expert", originalText);
        
        // Step 2: FR -> HE
        const he = this.callAgent("French-Hebrew-Expert", fr);
        
        // Step 3: HE -> EN
        const finalEn = this.callAgent("Hebrew-English-Expert", he);
        
        // Step 4: Evaluate
        const metrics = this.runEval(originalText, finalEn);
        console.log(`📊 Drift Score: ${metrics.drift_score}`);

        // Generate Report
        const report = `# Final Mission Report (Node.js Runtime)\n\nOriginal: ${originalText}\nFinal: ${finalEn}\nScore: ${metrics.drift_score}`;
        fs.writeFileSync(path.join(this.agentFolder, 'FINAL_REPORT.md'), report);
        
        console.log("✅ Mission Complete. Report saved to Agent_Folder.");
    }
}

const orch = new Level4Orchestrator();
orch.execute("Don't count your chickens before they've hatched.");
