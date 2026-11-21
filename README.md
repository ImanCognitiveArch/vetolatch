# UniversalMind Governance SDK

**AI may propose. Humans retain authority.**

UniversalMind is a small Python governance layer for AI-agent workflows that need an explicit, auditable human decision before a proposed state-changing action may proceed.

This public SDK is intentionally **not** the private UniversalMind cognitive runtime. It contains no RuntimeKernel, Cognitive Bus, Genome/evolution, self-improvement engine, or SCL research implementation.

## Install

```bash
pip install universalmind
```

For the staged prerelease build:

```bash
pip install --pre universalmind
```

## 60-second example

```python
from universalmind import GovernanceEngine

engine = GovernanceEngine()
review = engine.create_review(
    "Refund $4,500 to customer #8841 after duplicate billing investigation.",
    metadata={"amount_usd": 4500, "workflow": "refund"},
)

print(review.status)               # pending_human
print(review.dispatch_authorized)  # False

approved = engine.approve(
    review.review_id,
    actor="finance_manager",
    note="Invoice and duplicate charge verified.",
)

print(approved.dispatch_authorized)  # True
```

UniversalMind does **not** execute the refund. It issues the governance receipt; your integration remains responsible for the external action.

## Local Workbench / API

```bash
universalmind doctor
universalmind serve
```

Open `http://127.0.0.1:8000/` for the local Workbench or `http://127.0.0.1:8000/docs` for the API schema.

The first public release refuses non-loopback binding because it has no authentication.

## Governance contract

```text
proposal
   |
   v
pending_human ----> reject ----> no dispatch authority
   |
   +--------------> approve ---> dispatch_authorized = true
                                      |
                                      v
                                   outcome
                                      |
                                      v
                                audit events
```

Three rules are intentionally boring and hard:

1. Proposal is not authority.
2. No state-changing action is auto-approved.
3. A human decision is final for that review identity.

## Why this exists

Agent frameworks are good at generating plans and tool calls. The last-mile problem is different: who has authority to let a consequential action cross from proposal into execution, and what evidence remains afterward?

UniversalMind turns that boundary into a small protocol that can sit between an agent and its execution adapter.

## License

Source-available under **Business Source License 1.1**. Non-production use is permitted by the BSL. Production use requires a commercial license unless an Additional Use Grant says otherwise. See `LICENSE` and `COMMERCIAL-LICENSING.md`.

The BSL Change Date for this distribution is `2030-11-20`, subject to the license's earlier-fourth-anniversary rule.

## Private Core

See `PUBLIC-PRIVATE-BOUNDARY.md` for the architectural boundary between this public SDK and the private UniversalMind Core.

## Status

This repository is a staged public-SDK candidate. It is not production safety certification and should not be used as the sole control for high-stakes systems.
