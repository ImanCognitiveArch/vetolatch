# UniversalMind Governance SDK — Public Release Gate

**Current state:** PRIVATE STAGING. Do not publish to PyPI or make the repository public until every required gate below is explicitly closed.

## Product and distribution

- [x] Standalone public package has independent Git history.
- [x] Public package imports no private UniversalMind Core modules.
- [x] Unit/API/boundary tests pass.
- [x] Wheel and sdist pass `twine check`.
- [x] Clean install from the built wheel passes `universalmind doctor`.
- [x] Wheel content audit contains no private-Core paths.
- [ ] TestPyPI rehearsal completed from a tagged commit.
- [ ] Reproducible release artifact/hash recorded for the public package.

## Legal and IP

- [x] BSL 1.1 text included with staged parameters.
- [x] Copyright and public/private boundary notices included.
- [ ] Qualified IP counsel reviews the BSL parameters and commercial model.
- [ ] U.S. trademark clearance for `UniversalMind` / preferred public mark completed.
- [ ] Final decision recorded on whether to keep `UniversalMind`, use `UniversalMind Governance`, or adopt a more distinctive mark.

## Security

- [x] Built-in server refuses non-loopback binding.
- [x] SDK does not execute external actions itself.
- [x] Security boundary is documented.
- [ ] Independent security review of the public package completed.
- [ ] Public vulnerability-reporting contact/channel confirmed.

## PyPI and release operations

- [x] Candidate PyPI project name `universalmind` was available when checked on 2026-11-21.
- [ ] PyPI project/account security and 2FA confirmed by Iman.
- [ ] PyPI Trusted Publisher configured for `ImanCognitiveArch/universalmind-sdk` and the release workflow.
- [ ] First public version number approved.
- [ ] Public repository visibility change approved.

## Commercial/readiness

- [ ] Commercial production-use terms reviewed by counsel.
- [ ] First architecture-pilot offer and pricing hypothesis approved.
- [ ] Public claims checked against evidence; no safety, compliance, deployment, or immutability overclaim.
- [ ] First external evaluator flow ready for the public SDK.

## Release rule

No single green test, GitHub tag, PyPI name availability check, or legal document is permission to publish. Public release requires the combined engineering + IP + security + claims gate above.
