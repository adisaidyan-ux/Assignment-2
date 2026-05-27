/*
eval_drift.js - The "Hands" (Node.js Version)
---------------------------------------------
Role: Measures semantic drift using lexical similarity and 
      Expert Committee Judge prompts.
*/

const original = process.argv[2];
const final = process.argv[3];

if (!original || !final) {
    console.log(JSON.stringify({ error: "Missing arguments" }));
    process.exit(1);
}

function calculateSimilarity(s1, s2) {
    const w1 = new Set(s1.toLowerCase().match(/\w+/g));
    const w2 = new Set(s2.toLowerCase().match(/\w+/g));
    const intersect = new Set([...w1].filter(x => w2.has(x)));
    const union = new Set([...w1, ...w2]);
    return intersect.size / union.size;
}

const score = calculateSimilarity(original, final);

const result = {
    original: original,
    final: final,
    drift_score: parseFloat(score.toFixed(4)),
    status: score > 0.8 ? "Success" : "Needs Retry",
    judge_prompt_preview: `### ROLE: Semantic Committee... Compare "${original}" vs "${final}"...`
};

console.log(JSON.stringify(result, null, 4));
