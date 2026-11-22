# Independent evaluation: VetoLatch 0.4.0a1

Purpose: verify that an independent developer can install the evaluation release
and understand proposal, human authority, and audit identity without a model key.
This is a non-production evaluation. Allow approximately 10 minutes.

## Install into a fresh environment

Python 3.10 or newer is required. Windows PowerShell:

```powershell
py -3.11 -m venv .venv-vetolatch
& .\.venv-vetolatch\Scripts\Activate.ps1
python -m pip install --no-cache-dir vetolatch==0.4.0a1
python -m pip check
vetolatch doctor
vetolatch serve
```

For macOS/Linux, create the environment with `python3 -m venv .venv-vetolatch`
and activate with `source .venv-vetolatch/bin/activate`; the pip/CLI steps are
the same. The release and its dependencies install from primary PyPI.

## Review using the installed Workbench

Open `http://127.0.0.1:8000/` and use synthetic text only.

1. Create a proposed demo action. Confirm pending status and no authorization.
2. Explicitly approve it. Confirm authorization and unchanged review/action IDs.
3. Record a simulated outcome and inspect the audit events.
4. Create a different review, reject it, and confirm dispatch stays unauthorized.
5. Inspect the HTTP contract at `http://127.0.0.1:8000/docs`.

Nothing here calls a production tool. The SDK records authority; an external
adapter would own execution. The example-local decorator and SQLite demo are
available in the published source distribution and repository, not as SDK exports.

## Return these observations

- Python/OS and whether installation/doctor passed.
- The first point where the flow or contract was unclear.
- Whether review_id and action_id were understandable and stable.
- Whether an agent-tool integration would need a different approval boundary.
- Any reproducible failure, with synthetic inputs only.

The Workbench is loopback-only, unauthenticated, and in-memory. Decisions do not
persist across server restarts. Caller-supplied actor labels are not authenticated
human identity. The audit history is not a cryptographically immutable ledger.

Reference: https://pypi.org/project/vetolatch/0.4.0a1/
Licensing and public/private boundaries remain as documented in the package.
