# VetoLatch - Public Release Gate

## Architecture / IP

- [x] Public package imports no private UniversalMind Core modules.
- [x] Private-Core markers are rejected by the distribution-boundary tests.
- [x] Clean install from the built wheel passes `vetolatch doctor`.
- [x] The example performs no real external action.
- [x] Public repository has independent Git history from the private Core.

## Package quality

- [x] Test suite passes.
- [x] Wheel and sdist build cleanly.
- [x] `twine check` passes.
- [x] Wheel content inspected for private-Core leakage.
- [ ] TestPyPI clean-install rehearsal completed.
- [ ] Public PyPI clean-install rehearsal completed.

## Brand / legal

- [x] Public package/product mark selected: `VetoLatch`.
- [ ] Formal trademark/legal clearance completed or risk explicitly accepted.
- [x] BUSL-1.1 license text and public/private boundary staged.
- [ ] Final license/IP review completed before public release.

## Accounts / publishing

- [ ] TestPyPI account verified and 2FA enabled.
- [ ] PyPI account verified and 2FA enabled.
- [ ] Trusted Publishing or API-token publishing configured.
- [ ] GitHub repository `ImanCognitiveArch/vetolatch` reviewed before visibility is changed.
- [ ] Final release tag/version approved.

## Current posture

Engineering candidate: `0.4.0a1`.

Do not make the GitHub repository public and do not publish to public PyPI until the remaining unchecked legal/account/release gates are deliberately closed.
