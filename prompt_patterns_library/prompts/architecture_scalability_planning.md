# Scalability Planning Prompt Template

**Role**: Distributed Systems Architect with 10+ years of experience designing scalable and reliable systems.

**Task**: Create a scalability plan for the described system, identifying bottlenecks, defining scaling strategies, and outlining a practical migration and rollout path.

**Input Placeholder**:

- System Overview: [SYSTEM_OVERVIEW]
- Current Architecture: [CURRENT_ARCHITECTURE] (services, databases, caches, queues, third-party integrations)
- Traffic Estimates: [TRAFFIC_ESTIMATES] (average/peak RPS, concurrency, geographic distribution)
- Read/Write Ratio: [READ_WRITE_RATIO]
- Data Volume and Growth: [DATA_GROWTH] (current storage and projected growth)
- SLO/SLA Targets: [SLO_SLA] (latency, availability, reliability targets)
- Constraints: [CONSTRAINTS] (budget, timeline, team capacity, technology stack, compliance requirements)

**Expected Output Format**:

Return your answer using the following structure:

1. Assumptions: Clearly labeled assumptions with concrete numbers if missing.
2. Scalability Risks: Ranked list of likely bottlenecks (compute, database, cache, network, external dependencies).
3. Scaling Strategies: Recommended scaling approaches for major components (caching, replication, partitioning, async processing, load balancing, CDN).
4. Data Strategy: Schema and indexing considerations, partitioning keys, and consistency trade-offs.
5. Capacity Plan: Rough sizing guidance and key metrics to monitor and refine estimates.
6. Migration / Rollout Plan: Step-by-step evolution from current to target architecture with minimal downtime.
7. Validation: Load testing strategy, success criteria, monitoring, and alerting updates.