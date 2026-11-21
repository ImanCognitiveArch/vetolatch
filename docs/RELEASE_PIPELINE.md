# VetoLatch release pipeline

Updated: 2026-11-21. Evaluation version: `0.4.0a1`.

## Current position

**TestPyPI publication and independent installation are complete.**
Next: one independent evaluation of the install/review/audit flow, then deliberate
closure of the existing public PyPI/repository release gates.

| Stage | State | Evidence |
| --- | --- | --- |
| Public/private SDK isolation | Passed | Source unchanged; scoped artifact checks passed |
| Python tests | Passed | 23 tests; GitHub matrix 3.10, 3.11, 3.12 green |
| Wheel and sdist validation | Passed | build, twine check, FORBIDDEN=[] |
| TestPyPI OIDC publication | Passed | Run 44941251525, attempt 2 |
| Independent TestPyPI installation | Passed | Fresh Python 3.11 venv, no wheel cache, registry-origin digest verified |
| Dependency consistency and CLI | Passed | pip check and vetolatch doctor |
| Installed approval/rejection/audit behavior | Passed | Pending denies; explicit approval authorizes; final decision protected; IDs stable |
| Account 2FA | Owner confirmed complete | New keys on both registries; no secrets recorded |
| PyPI publisher registration | Configured | Owner screenshot: release.yml, environment pypi |
| Public PyPI release | Pending | Not triggered by the TestPyPI rehearsal |
| Repository visibility | Private staging | No visibility change |

## Exact publisher identities

| Registry | Project | Owner | Repository | Workflow filename | Environment |
| --- | --- | --- | --- | --- | --- |
| TestPyPI | vetolatch | ImanCognitiveArch | vetolatch | testpypi.yml | testpypi |
| PyPI | vetolatch | ImanCognitiveArch | vetolatch | release.yml | pypi |

The initial TestPyPI attempt failed with `invalid-publisher`. After the account
owner registered the matching publisher, only the failed publish job was rerun.
Attempt 2 successfully published the already-tested implementation commit
`7b7530b035f0557583dc6a6d2503e9f774467bcf`.

- Publication: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941251525
- Implementation tests: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941250766
- Implementation boundary check: https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941250779
- Package: https://test.pypi.org/project/vetolatch/0.4.0a1/

## Independent installation evidence

A new Python 3.11.9 virtual environment downloaded the wheel directly from
TestPyPI using `pip install --no-cache-dir --no-deps --index-url
https://test.pypi.org/simple/ vetolatch==0.4.0a1`.
Declared dependencies were fetched separately from the primary PyPI index;
no mixed-index dependency lookup was needed. The first dependency-resolution
attempt failed; a retry against primary PyPI succeeded without changing requirements.

The pip installation report identified `test-files.pythonhosted.org` as the
wheel source. Its SHA-256 matched the registry's version JSON:

`57e0d751db87d81e09cbfeff8292efdde88583384505a88d44e9b56b794ff6b4`

The import resolved from the new environment's `site-packages`, not an editable
checkout. `pip check` and `vetolatch doctor` passed. A smoke check against the
installed package verified pending/default-deny, explicit approval, rejection,
final-decision protection, stable review/action identity, and outcome/audit events.

The local machine-readable installation report and digest check are kept under
the repository's ignored `.git/testpypi-install-proof-20261121/` directory.
This report contains the durable, non-secret evidence needed to repeat the check.

## Next release gates

1. Use `docs/INDEPENDENT_EVALUATION.md` for one external non-production review.
   Collect installation friction, clarity of pending/approve/reject, and audit identity.
2. Deliberately close the existing license/IP, brand, visibility, and final
   release-tag gates in `RELEASE-GATE.md`; do not imply legal clearance.
3. Publish the approved PyPI release using `release.yml`, then verify a fresh
   installation from primary PyPI and add the live PyPI version badge.

## Continuation contract

Preserve UniversalMind's architecture freeze, Golden Baseline, Cognitive Bus,
human authority, stable review_id/action_id, licensing and independent Git history.
Keep the example decorator outside the SDK. Do not change the AI model, add
model providers, connect production tools, or expand the research runtime here.
