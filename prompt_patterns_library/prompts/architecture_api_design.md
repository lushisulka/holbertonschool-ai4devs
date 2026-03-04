# API Design Prompt Template

**Role**: API Architect with 10+ years of experience designing production-grade REST APIs.

**Task**: Design a RESTful API for the described domain, including resources, endpoints, authentication, error handling, versioning, and operational considerations.

**Input Placeholder**:

- Domain: [DOMAIN_DESCRIPTION]
- Primary Users/Clients: [CLIENT_TYPES] (web app, mobile, partners, internal services)
- Core Resources/Entities: [RESOURCES] (e.g., User, Order, Product)
- Required Operations: [OPERATIONS] (CRUD + custom actions)
- Authentication/Authorization Model: [AUTH_MODEL] (JWT/OAuth2/API keys; roles/scopes/tenancy)
- Data Ownership Rules: [OWNERSHIP_RULES]
- Performance Targets: [PERFORMANCE_TARGETS] (RPS, p95 latency, SLA)
- Constraints: [CONSTRAINTS] (stack, naming conventions, backward compatibility)
- Query Capabilities: [QUERY_CAPABILITIES] (pagination, sorting, filtering)
- Idempotency Requirements: [IDEMPOTENCY_REQUIREMENTS]
- Versioning Preference: [VERSIONING_PREFERENCE] (path/header/media-type)

**Expected Output Format**:

Return your answer using the following structure:

1. Assumptions: Bullet list of explicit assumptions.
2. Resource Model: List resources, relationships, identifiers, ownership rules.
3. Endpoints: Markdown table with Method, Path, Description, Authentication, Notes.
4. Request/Response Examples: JSON examples for 3–5 key endpoints.
5. Error Handling Model: Standard error schema and mapping of common HTTP status codes.
6. Rate Limiting & Idempotency: Proposed limits and idempotency strategy.
7. Versioning & Compatibility: Version evolution and deprecation policy.
8. Validation: Testing and contract verification approach.