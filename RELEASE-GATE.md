# VetoLatch - Public Release Gate

## Architecture / IP

- [x] Public package imports no private UniversalMind Core modules.
- [x] Private-Core markers are rejected by the distribution-boundary tests.
- [x] Clean install from the built wheel passes `vetolatch doctor`.
- [x] Examples perform no persistent or production external action (SQLite is in-memory).
- [x] Public repository has independent Git history from the private Core.

## Package quality

- [x] Test suite passes.
- [x] Wheel and sdist build cleanly.
- [x] `twine check` passes.
- [x] Wheel content inspected for private-Core leakage.
- [x] TestPyPI clean-install rehearsal completed.
- [x] Public PyPI clean-install rehearsal completed; unqualified pip install, doctor and dependency checks passed.

## Brand / legal

- [x] Public package/product mark selected: `VetoLatch`.
- [x] Owner explicitly authorized this public alpha release on 2026-11-22.
- [ ] Formal trademark/legal clearance (not performed or claimed).
- [x] BUSL-1.1 license text and public/private boundary staged.
- [x] BUSL-1.1 parameters, private-Core exclusion and disclosure limits reviewed for this alpha.
- [ ] Independent legal/IP opinion (not performed or claimed).

## Accounts / publishing

- [x] TestPyPI account verified and 2FA enabled.
- [x] PyPI account verified and 2FA enabled.
- [x] Trusted Publishing or API-token publishing configured.
- [x] All reachable Git history reviewed before public visibility: 7 commits, 63 blobs; Gitleaks found no leaks.
- [x] Owner authorized version 0.4.0a1 for primary PyPI and public source.

## Current posture

Public PyPI alpha release: `0.4.0a1`; OIDC publication, independent installation and anonymous public source access passed.

Account 2FA was confirmed by the owner after key replacement. Both publisher
registrations were shown in account screenshots; the TestPyPI OIDC identity was
additionally verified by successful publication. Primary PyPI OIDC publication and independent installation are now verified.
See `docs/RELEASE_PIPELINE.md` for evidence.

Public alpha release is authorized. Record primary PyPI installation and public visibility after observing success. Formal legal clearance is not implied by publication.
