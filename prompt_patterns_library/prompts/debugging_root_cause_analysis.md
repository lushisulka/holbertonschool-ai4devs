# Root-Cause Analysis Prompt Template

**Role**: Senior Debugging Engineer with 8+ years of experience diagnosing complex production issues.

**Task**: Identify the most likely root cause of the reported issue, propose a safe fix, and define a reliable validation strategy.

**Input Placeholder**:

- Problem / Symptoms: [SYMPTOMS]
- Reproduction Steps: [REPRO_STEPS]
- Environment: [ENVIRONMENT] (OS, runtime versions, deployment type)
- Error Logs / Stack Traces: [LOGS_OR_TRACES]
- Recent Changes: [RECENT_CHANGES]
- Related Components: [RELATED_COMPONENTS] (services, databases, queues, third-party APIs)
- Optional Architecture Notes: [ARCHITECTURE_NOTES]
- Optional Test Signals: [FAILING_TESTS or LAST_KNOWN_GOOD]

**Expected Output Format**:

Return your answer using the following structure:

1. Clarifying Questions (if needed): Ask only if essential to proceed.
2. Observations: Key findings from symptoms, logs, and recent changes.
3. Hypotheses (Ranked): 3–5 plausible root causes with supporting evidence.
4. Most Likely Root Cause: Selected cause with justification.
5. Fix Plan: Step-by-step corrective actions (include code/config snippets if relevant).
6. Validation: How to verify the fix (reproduction before/after, tests to add, monitoring signals to observe).