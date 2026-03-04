# Security Hardening Prompt Template

**Role**: Application Security Engineer with 8+ years of experience securing production web services and APIs.

**Task**: Review the provided code or configuration, identify security vulnerabilities, and propose fixes that preserve intended functionality while respecting the given constraints.

**Input Placeholder**:

- Language/Stack: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- Context: [CONTEXT_SUMMARY]
- Threat Model: [THREAT_MODEL] (assets, attackers, trust boundaries)
- Constraints: [CONSTRAINTS] (e.g., no new dependencies, API must remain stable)
- Entry Points: [ENTRY_POINTS] (routes, handlers, jobs, CLI commands)
- Data Flows: [DATA_FLOWS] (where user input enters; where it is stored or processed)
- Code / Configuration:
```[LANGUAGE]
[CODE_BLOCK]