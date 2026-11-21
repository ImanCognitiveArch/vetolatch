# VetoLatch / UniversalMind Public-Private Boundary

## Public: VetoLatch

VetoLatch is a standalone reference implementation of one governance contract:

`proposal -> pending_human -> approve/reject -> outcome -> audit events`

It may include:

- stable `review_id` and `action_id` identities;
- explicit human approval/rejection state transitions;
- local API and CLI;
- a minimal local Workbench;
- non-cryptographic local audit events;
- integration schemas and documentation.

## Private: UniversalMind Core

The following remain outside the public repository and package:

- `RuntimeKernel` and Cognitive Bus internals;
- Genome, mutation, fitness, and evolution engines;
- governed self-improvement orchestration;
- collective-intelligence and SCL experimental machinery;
- private research datasets, stress surfaces, and unpublished evidence;
- enterprise connectors, customer-specific adapters, SSO/auth, persistence, and commercial deployment logic.

## Dependency direction

VetoLatch MUST NOT import from the private UniversalMind Core.

Private integrations may depend on the public governance protocol, but the public package must remain independently installable and testable.

## Release gate

A public wheel fails release if it contains any path matching private-Core package names such as `brain_bus`, `collective_intelligence`, `evolution`, `self_improvement`, or private research assets.
