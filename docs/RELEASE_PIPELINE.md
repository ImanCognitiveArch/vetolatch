# VetoLatch release pipeline

Updated: 2026-11-22. Public alpha: `0.4.0a1`.

## Current position

**Primary PyPI publication, independent installation and public source access passed.**
The next milestone is external feedback. No external evaluator or paying customer
has been counted merely because the package shipped.

| Stage | State | Evidence |
| --- | --- | --- |
| Standalone SDK tests | Passed | 23 tests; CI Python 3.10, 3.11, 3.12 |
| TestPyPI OIDC rehearsal | Passed | Run 44941251525, attempt 2 |
| Primary PyPI OIDC publication | Passed | Run 45022350358, release v0.4.0a1 |
| Fresh primary PyPI install | Passed | Unqualified pip install vetolatch, no wheel cache |
| CLI and dependency check | Passed | vetolatch doctor and pip check |
| Installed decision/audit smoke | Passed | Pending, approve/reject, final API decision, stable IDs, outcome events |
| Public repository | Verified | Anonymous repository API and raw source returned HTTP 200 |
| History and credential checks | Passed within scope | Release base 1ebc314: 8 commits, 68 unique blobs; no findings |
| Actions-log credential check | Passed within scope | 17 completed-run logs, no Gitleaks findings |
| Demo and brief | Prepared | docs/demo.gif, MP4 and updated ten-page PDF |
| External evaluators | 0 of target 3 | Awaiting real external feedback |
| Paid pilots | 0 of target 1 | Discovery target, not an achieved sale |
| LinkedIn | Published and verified | Live video post: https://lnkd.in/p/e2XQd-Zk |
| Evaluator invitations | Scheduled | Up to 10 relevant free DMs, 2026-11-23 10:00 America/New_York |

## Verified release links

- Package: https://pypi.org/project/vetolatch/0.4.0a1/
- Source: https://github.com/ImanCognitiveArch/vetolatch
- Release: https://github.com/ImanCognitiveArch/vetolatch/releases/tag/v0.4.0a1
- Publication workflow: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/45022350358
- Release CI: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/45022349785
- Boundary CI: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/45022349694

## Registry-origin evidence

A fresh Python 3.11.9 virtual environment installed `vetolatch` directly from
primary PyPI, without an exact pin or `--pre`. It resolved to `0.4.0a1`.
The install report identified `files.pythonhosted.org` as the wheel source.
Its SHA-256 matched primary PyPI's version metadata:

`68a948db479028b43cbe9cf59ce3dd6a4eb7691b9ac7227639dc051cbda4aae6`

Imports resolved from the new environment's `site-packages`. Dependency and CLI
checks passed. The installed package's pending/default-deny, explicit approval,
rejection, final decision API protection, stable review/action identity and
outcome/audit events passed smoke checks.

The primary PyPI wheel differs from the TestPyPI wheel because release
documentation and the Licensed Work name were updated. Runtime source did not
change between those releases. A Windows default-text-encoding issue affected
reading the pip report; the verification resumed with explicit UTF-8 and passed.

## Disclosure and trust limits

The full reachable release history and tracked source were scanned with
Gitleaks 8.30.1 after verifying the official release archive checksum. A separate
blob audit checked private-Core paths/imports, credential patterns, contact
addresses and local paths. Commit emails use GitHub noreply addresses.

These are scoped checks, not a universal proof of zero disclosure. Public
visibility exposes source, history and Actions logs. Installing this package
discloses the public SDK source; it does not grant access to the separate private
UniversalMind Core. No credentials or bridge to that Core are bundled.

This alpha is an in-memory reference state machine for a trusted process.
Caller labels are not authenticated identity. Same-process code can invoke
decision APIs or mutate returned objects. Production integrators own
authentication, authorization, protected state and external execution.

## Next actions

1. Use docs/INDEPENDENT_EVALUATION.md to invite genuine external evaluation.
2. Review responses to the published LinkedIn demo/copy: https://lnkd.in/p/e2XQd-Zk
3. Execute the scheduled individual evaluator invitations, then count actual results.
4. Scope one paid pilot around a single workflow only after a discovery conversation.

Owner authorized the public alpha on 2026-11-22. BUSL-1.1 remains in effect.
Publication does not assert formal trademark clearance or a legal/security certification.
UniversalMind's architecture freeze, Golden Baseline, Cognitive Bus and private
research hold remain unchanged. No AI-model changes were made.

## Outreach delivery preparation

The three professor drafts contain the current ten-page VetoLatch PDF and live
GitHub/PyPI links. Sending is scheduled via ChatGPT Automations, not Gmail's
native Scheduled folder. On 2026-11-23, Scheutz and Huang are scheduled for
09:15 America/New_York; Admoni for 09:35. Actual delivery remains a future check.

The updated public source commit 7cc9bc0 passed history and Gitleaks scans:
9 reachable commits, 76 unique blobs, no detected findings. The public demo
and PDF are also attached to the v0.4.0a1 GitHub release.
