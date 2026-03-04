# Test Strategy Creation Prompt Template

**Role**: QA Lead / Test Architect with 8+ years of experience designing test strategies for production systems.

**Task**: Create a comprehensive and risk-based test strategy for the described component or system, covering unit, integration, end-to-end, and performance testing, including CI/CD guidance.

**Input Placeholder**:

- Component / System: [COMPONENT_NAME]
- Description: [COMPONENT_DESCRIPTION]
- Critical User Flows: [CRITICAL_FLOWS]
- Dependencies: [DEPENDENCIES] (databases, services, third-party APIs)
- Risk Level: [RISK_LEVEL] (Low/Medium/High) + [RISK_NOTES]
- Environments: [ENVIRONMENTS] (local, CI, staging, production)
- Constraints: [CONSTRAINTS] (timeline, tooling, team skills)
- Optional Architecture Notes: [ARCHITECTURE_NOTES]

**Expected Output Format**:

Return your answer using the following structure:

1. Scope & Goals: Define in-scope vs out-of-scope and quality objectives.
2. Risk-Based Priorities: Ranked risks and how the test strategy mitigates them.
3. Test Pyramid Plan: Recommended distribution of unit, integration, and E2E tests with rationale.
4. Test Categories:
   - Unit Tests: What to cover and example test cases.
   - Integration Tests: Key integration points and example scenarios.
   - End-to-End Tests: Critical user journeys and example scenarios.
   - Performance Tests: Load/stress targets and test scenarios.
5. Tooling: Recommended tools or frameworks per test layer.
6. CI/CD Integration: What runs on pull requests, merges, and nightly builds.
7. Metrics & Coverage Targets: Coverage expectations and reporting approach.
8. Exit Criteria: Conditions required to consider the component ready for release.