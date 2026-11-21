# UniversalMind â€” B2B Positioning Draft

## Category

Human-governed approval and audit boundary for AI-agent actions.

## Hero

**AI may propose. Humans retain authority.**

VetoLatch places an explicit `pending_human` gate between an AI-generated proposal and a consequential state-changing action. It creates stable review/action identities, records the human decision, and preserves an auditable local event history without pretending that recommendation equals authority.

## The business problem

An AI agent can be excellent at reasoning and still be unacceptable in production if Security, Risk, Legal, or an engineering owner cannot answer:

- What exactly did the agent propose?
- Who had authority to approve it?
- Did anything execute before approval?
- Which proposal did the human actually approve?
- What outcome was observed afterward?

VetoLatch turns those questions into an explicit software contract.

## Initial buyer hypotheses

Start with teams where a wrong action is expensive but the workflow can still be piloted safely:

1. AI agencies building agent workflows for clients.
2. B2B SaaS teams adding state-changing AI automation.
3. DevOps/internal-tool teams gating destructive or production-changing actions.
4. FinTech operations teams evaluating human approval around refunds or account operations in controlled pilots.

Avoid marketing the first release as a clinical, safety-critical, compliance-certified, or autonomous-system product.

## Commercial wedge

**Architecture Pilot â€” 2 weeks**

Map one existing agent workflow, place the governance boundary immediately before one state-changing adapter, instrument review/action/outcome identity, and leave the customer's execution system responsible for the actual action.

Deliverables:
- integration boundary diagram;
- local proof of concept;
- human-approval workflow;
- audit event schema;
- friction/risk findings;
- production-readiness gap report.

## Commercial model hypothesis

1. Source-available SDK for non-production evaluation under BSL 1.1.
2. Paid production-use license.
3. Paid architecture/integration pilot.
4. Private enterprise connectors, persistence, authentication/SSO, team approvals, and support.

Pricing is deliberately NOT frozen before discovery calls and legal review.

## Claims discipline

Say:
- explicit human-approval boundary;
- proposal is not authority;
- stable review/action identities;
- local audit event history;
- public SDK does not execute the external action;
- negative research results are preserved rather than promoted.

Do not say:
- immutable/cryptographic audit trail (not implemented in the public SDK);
- certified compliance;
- safety-certified;
- deployed in banking/healthcare/robots/spacecraft;
- prevents all agent failures;
- autonomous learning is production-ready.
