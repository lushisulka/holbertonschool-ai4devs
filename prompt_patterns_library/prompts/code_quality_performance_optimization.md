# Performance Optimization Prompt Template

**Role**: Performance Engineer with 8+ years of experience optimizing production systems.

**Task**: Optimize the provided [LANGUAGE] code for improved runtime latency and/or memory efficiency while preserving correct behavior and respecting the given constraints.

**Input Placeholder**:

- Language/Stack: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- Context: [CONTEXT_SUMMARY]
- Performance Target: [PERFORMANCE_TARGET] (e.g., p95 < 50ms, memory < 200MB)
- Constraints: [CONSTRAINTS] (e.g., no new dependencies, public API unchanged)
- Workload Description: [WORKLOAD_DESCRIPTION] (input sizes, distribution, concurrency)
- Current Measurements (optional): [BENCHMARKS_OR_PROFILING]
- Code:
```[LANGUAGE]
[CODE_BLOCK]