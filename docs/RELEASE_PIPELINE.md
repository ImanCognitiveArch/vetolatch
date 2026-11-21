# VetoLatch release pipeline

Updated: 2026-11-21. Candidate: 0.4.0a1.

## Verified engineering state

- Existing GitHub CI at be3d1fd passed; repository is private staging.
- Added example-local `@veto_gate` around a standard function-call payload.
- External execution is disposable in-memory SQLite; the SDK never executes tools.
- 23 local tests passed, including rejection/default-deny, approved arguments,
  stable audit identity, real SQL dispatch, and scanner negative controls.
- Wheel and sdist built; both passed `twine check`.
- Built-distribution scanner reported `FORBIDDEN=[]`.
- Publish workflows now require tests and artifact boundary checks before upload.
- Live test/boundary badges are present; PyPI version badge awaits actual release.
- No changes to `src/vetolatch/` or the private UniversalMind Core.

## Publishing identity (exact match required)

| Registry | Project | Owner | Repository | Workflow filename | Environment |
| --- | --- | --- | --- | --- | --- |
| TestPyPI | vetolatch | ImanCognitiveArch | vetolatch | testpypi.yml | testpypi |
| PyPI | vetolatch | ImanCognitiveArch | vetolatch | release.yml | pypi |

GitHub environments `testpypi` and `pypi` already exist.
Trusted Publishers belong in each registry account's Publishing page.
For a new project, add a pending publisher. Do not enter the full workflow path
in the workflow filename field. Authentication uses OIDC, never a saved API token.

## Pending evidence

1. Account owner completes/validates 2FA separately on both registries.
   Screenshots show a setup form, not proof of completed activation.
   Replace the authenticator secrets shown in shared setup screenshots; do not
   put QR codes, provisioning keys, recovery codes or credentials in Git.
2. Register/verify the exact TestPyPI pending publisher.
3. Run `testpypi.yml`; confirm successful OIDC upload.
4. Install from TestPyPI into a fresh environment and run `vetolatch doctor`.
5. Close existing public-release license/IP/brand gates deliberately.
6. Publish approved release to PyPI, verify independent installation, then add
   the live PyPI version badge and update the quickstart.

The current cloud browser has reached TestPyPI's sign-in page; it does not share
the Windows browser's authenticated session. Registry completion remains blocked
on account access, not on a request to provide passwords or OTPs in chat.
Public PyPI publication and repository visibility are separate from this TestPyPI rehearsal.

## Continuation contract

Preserve UniversalMind's architecture freeze, Golden Baseline, Cognitive Bus,
human authority, stable review_id/action_id, licensing and independent Git history.
Keep the example decorator outside the SDK. Do not add model providers, change
the AI model, connect production tools or expand the research runtime for this release.

## Fresh local wheel installation

A fresh Python 3.11 virtual environment installed the built wheel successfully.
`vetolatch doctor` passed; import resolved from that environment's site-packages
and reported version `0.4.0a1`, not the editable source checkout.

## Observed GitHub results for implementation commit 7b7530b

- Tests passed on Python 3.10, 3.11 and 3.12:
  https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941250766
- Core boundary workflow passed:
  https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941250779
- TestPyPI rehearsal was actually dispatched:
  https://github.com/ImanCognitiveArch/vetolatch/actions/runs/44941251525
  Its build, tests, distribution validation and boundary inspection passed.
  Upload stopped with `invalid-publisher`: valid OIDC token, no matching publisher.
  This establishes a registry identity/configuration blocker, not a package build failure.
- Secure TestPyPI sign-in reached a username validation error: use the account's
  username, not its email address. No completed signed-in state was observed.

Next action: account owner completes authentication/credential setup, then verifies
or registers the exact TestPyPI publisher from the table above. Rerun the failed
publish job and perform the TestPyPI clean-install rehearsal. Do not mark either
registry upload or TestPyPI installation as successful before observing them.
