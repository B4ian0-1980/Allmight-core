---
name: pre-mortem
description: "Cognitive risk discovery and failure anticipation methodology. Run before writing code or launching features: assumes project has already failed in the future to uncover blind spots, technical traps, and false assumptions."
metadata:
  version: 1.0.0
upstream_source: https://github.com/borghei/Claude-Skills
last_updated: 2026-10-10
---

# Pre-Mortem Risk Discovery & Failure Anticipation

The Pre-Mortem is a psychological debiasing technique developed by Gary Klein. Instead of asking *"what could go wrong?"* (which triggers optimism bias), the team assumes:
> **"It is 6 months from now. The project has failed catastrophically. What happened?"**

---

## ⚡ The 5-Step Pre-Mortem Protocol

### Step 1: Set the Failure Scenario
State clearly: *"The feature was deployed, but user adoption was near zero, the database locked up under load, and users complained of confusing UX. The launch was considered a complete failure."*

### Step 2: Individual Brainstorming of Failure Modes
List all plausible failure mechanisms across 5 categories:
1. **Technical & Scalability**: N+1 queries, unindexed columns, memory leaks, single points of failure.
2. **UX & Usability Friction**: Violations of Laws of UX, confusing navigation, steep learning curve.
3. **Product & Market Fit**: Solving a problem the user doesn't care about, incorrect default assumptions.
4. **Security & Compliance**: Exposed credentials, broken access control (BOLA/IDOR), missing rate limits.
5. **Operational & Maintenance**: Complex deploy procedures, missing logs/monitoring, unmaintainable code.

### Step 3: Rank Failures by Impact & Probability
Score each failure candidate:
- **Impact (1-5)**: How devastating is this failure?
- **Probability (1-5)**: How likely is this to occur if left unaddressed?
- **Risk Score** = $\text{Impact} \times \text{Probability}$.

### Step 4: Proactive Remediation & Safeguards
For the top 3 highest-scoring risks, establish immediate architectural safeguards before writing production code:
- Circuit breakers, database indexes, fallback providers, progressive disclosure, unit tests.

### Step 5: Document the "Safeguard Ledger"
Include the mitigations directly in the task execution plan (`{task-slug}.md`).
