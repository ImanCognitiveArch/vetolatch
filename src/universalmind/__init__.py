"""
UniversalMind Public Governance SDK.

ROLE
----
Expose a small, stable, human-governed approval contract without importing or
publishing the private UniversalMind cognitive runtime.
"""

__version__ = "0.4.0a1"

from .governance import GovernanceEngine, GovernanceError, ReviewRecord

__all__ = ["GovernanceEngine", "GovernanceError", "ReviewRecord", "__version__"]
