# Log/Trace Interpretation Prompt Template

**Role**: Site Reliability Engineer (SRE) with 8+ years of experience troubleshooting distributed systems.

**Task**: Analyze the provided logs, traces, and/or metrics to determine the most likely failure point, explain what is happening, and recommend the next best debugging steps.

**Input Placeholder**:

- System / Service: [SERVICE_NAME]
- Context: [CONTEXT_SUMMARY] (what changed, what users are experiencing)
- Environment: [ENVIRONMENT] (prod/staging, region, versions)
- Time Window: [TIME_WINDOW] (start/end, timezone)
- Logs: [LOG_SNIPPETS]
- Traces (optional): [TRACE_SNIPPETS]
- Metrics (optional): [METRICS_SNAPSHOT] (error rate, latency, saturation)
- Recent Changes: [RECENT_CHANGES] (deployments, configuration changes, infrastructure updates)
- Optional Architecture Notes: [ARCHITECTURE_NOTES]

**Expected Output Format**:

Return your answer using the following structure:

1. Assumptions: Key assumptions about topology, traffic patterns, or dependencies.
2. Signal Summary: What the logs, traces, and metrics indicate (errors, latency spikes, retries, timeouts, saturation).
3. Likely Failure Point(s): Ranked list. For each include:
   - Component
   - Evidence
   - Scope (single instance, region-wide, global)
4. Next Actions (Priority Order): 5–10 concrete debugging steps, including what to check and why.
5. Immediate Mitigations (if needed): Safe short-term actions and associated risks.
6. Instrumentation Improvements: Logging, tracing, metrics, or alerting enhancements to improve future diagnosis.