# VetoLatch

> **AI may propose. Humans retain authority.**

**VetoLatch** is a local-first human-approval and governance primitive for AI-agent workflows. It is the public governance boundary extracted from the private **UniversalMind** cognitive-runtime research architecture.

```text
AI / agent proposal
        |
        v
+---------------------------+
|         VetoLatch         |
| status: pending_human     |
| dispatch_authorized=False |
| review_id + action_id     |
+-------------+-------------+
              |
        Human operator
          /       \
     approve     reject
       |            |
       v            v
authorized=True   no authority
       |
       v
external system executes
       |
       v
outcome + audit events
```

The invariant is deliberately simple:

**Proposal != Authority. Recommendation != Decision.**

## 30-second quickstart

```bash
pip install vetolatch
vetolatch doctor
```

```python
from vetolatch import GovernanceEngine

gate = GovernanceEngine()

review = gate.create_review(
    "Refund $4,500 to customer #8841 after duplicate billing investigation.",
    metadata={"amount_usd": 4500, "workflow": "refund"},
)

assert review.status == "pending_human"
assert review.dispatch_authorized is False

approved = gate.approve(
    review.review_id,
    actor="finance_manager",
    note="Duplicate charge verified.",
)

assert approved.action_id == review.action_id
assert approved.dispatch_authorized is True
```

**VetoLatch never executes the refund.** It produces the governance state and authorization receipt; your integration remains responsible for authentication, external execution, and domain-specific compliance.

## Local Workbench / API

```bash
vetolatch serve
```

Then open:

- Workbench: `http://127.0.0.1:8000/`
- OpenAPI: `http://127.0.0.1:8000/docs`

This evaluation release deliberately refuses non-loopback binding because it has no authentication.

HTTP lifecycle:

```text
POST /reviews
GET  /reviews/{review_id}
POST /reviews/{review_id}/approve
POST /reviews/{review_id}/reject
POST /reviews/{review_id}/outcome
GET  /reviews/{review_id}/audit
```

## Three hard laws

1. **Proposal is not authority.** Creating a review never authorizes dispatch.
2. **No autonomous approval path exists in this SDK.** Approval requires an explicit call to the human-decision transition.
3. **A human decision is final for that review identity.** Approved/rejected reviews cannot be silently overwritten.

## Why this exists

Tool-using agents can produce useful plans and proposed actions. A different engineering question begins at the state-changing boundary:

**Who has authority to let the proposal become execution, and what evidence remains afterward?**

VetoLatch turns that boundary into a small, inspectable protocol that can sit between an agent and an execution adapter.

## Research provenance

VetoLatch comes from the governance work inside **UniversalMind**, a private cognitive-runtime and research architecture.

A quarantined UniversalMind research track has tested coordination and memory-persistence hypotheses under deterministic failure schedules. In one frozen 816-schedule experiment, simple freshness controls did **not** satisfy all preregistered promotion criteria. That mechanism remains on runtime hold rather than being promoted by tuning the result after the fact.

That research result is context for the engineering philosophy; it is **not** a claim that VetoLatch is safety-certified or production-validated.

## Explicit boundaries

VetoLatch `0.4.0a1` is:

- a local-first governance state machine;
- a small HTTP API and CLI;
- a minimal local review Workbench;
- a non-cryptographic local audit-event history;
- independently installable from the private UniversalMind Core.

It is **not**:

- a hosted SaaS;
- an authentication/SSO system;
- a cryptographically immutable ledger;
- a banking, medical, legal, or safety certification;
- a mechanism that performs external side effects;
- the private UniversalMind RuntimeKernel, Cognitive Bus, Genome/evolution, self-improvement, or SCL implementation.

See `PUBLIC-PRIVATE-BOUNDARY.md`.

## Example

```bash
python examples/fintech_refund.py
```

The example is deliberately a mock authorization flow. No bank API is called and no funds move.

## Licensing

VetoLatch is distributed under **Business Source License 1.1 (BUSL-1.1)**.

- Non-production use is permitted under the included BSL terms.
- Production use outside any Additional Use Grant requires separate commercial permission from the Licensor.
- Change Date: `2030-11-20`.
- Change License: Apache License 2.0.
- The BSL's earlier-fourth-anniversary rule still applies.

Read `LICENSE` and `COMMERCIAL-LICENSING.md` before use.

## Feedback

The first milestone is not stars. It is independent friction.

If you build tool-using agents, human-in-the-loop workflows, or HRI systems, open an issue describing:

- what you expected;
- where you hesitated;
- what contract felt unclear;
- what would prevent you from integrating the boundary.

**Built by Iman Khorami.**
Research context: https://imancognitivearch.github.io/universalmind-showcase/
