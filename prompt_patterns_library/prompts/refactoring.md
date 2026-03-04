# Refactoring for Readability Prompt Template

**Role**: Senior Software Engineer with 8+ years of experience maintaining large production codebases.

**Task**: Refactor the provided [LANGUAGE] code to improve readability and maintainability while preserving its existing behavior and public API.

**Input Placeholder**:

- Language / Stack: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- Context: [CONTEXT_SUMMARY]
- Constraints: [CONSTRAINTS] (e.g., public API unchanged, no new dependencies)
- Expected Behavior: [EXPECTED_BEHAVIOR]
- Code: [CODE_BLOCK]
- Optional Tests: [RELEVANT_TESTS]
- Optional Lint / Typecheck Commands: [LINT_TYPECHECK_COMMANDS]

**Expected Output Format**:

Return your answer using the following structure:

1. Assumptions: Bullet list of assumptions about behavior, environment, or constraints.
2. Refactoring Plan: 3–7 concise bullets describing intended structural and readability improvements.
3. Refactored Code: Full updated code in a fenced code block labeled [LANGUAGE].
4. Key Changes: Bullet list mapping each major change to its readability or maintainability benefit.
5. Validation: Steps to confirm behavior is unchanged (tests to run, sample inputs/outputs, lint/typecheck commands).