"""
VetoLatch human-governance engine.

ROLE
----
Own the public approval boundary: proposal -> pending_human -> approved/rejected
-> outcome. The engine never executes the proposed action itself. It only emits
an authorization receipt that an integrating application may choose to honor.

ARCHITECTURE CONTRACT
---------------------
- Recommendation/proposal is not authority.
- No state-changing action is auto-approved.
- review_id and action_id remain stable for the lifetime of a review.
- A final human decision cannot be overwritten.
- Private RuntimeKernel, Genome, Cognitive Bus, SCL, and self-improvement code
  are deliberately absent from this package.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from threading import RLock
from typing import Any, Literal
from uuid import uuid4

from .audit import AuditLedger


ReviewStatus = Literal["pending_human", "approved", "rejected"]


class GovernanceError(RuntimeError):
    """Raised when a caller violates the governance state machine."""


@dataclass
class ReviewRecord:
    """Stable public record for one proposed state-changing action."""

    review_id: str
    action_id: str
    proposal: str
    status: ReviewStatus = "pending_human"
    metadata: dict[str, Any] = field(default_factory=dict)
    decided_by: str | None = None
    decision_note: str | None = None
    outcome: str | None = None

    @property
    def dispatch_authorized(self) -> bool:
        """True only after an explicit human approval."""
        return self.status == "approved"

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["dispatch_authorized"] = self.dispatch_authorized
        return result


class GovernanceEngine:
    """Thread-safe in-memory implementation of the public governance contract."""

    def __init__(self, ledger: AuditLedger | None = None) -> None:
        self._records: dict[str, ReviewRecord] = {}
        self._lock = RLock()
        self.ledger = ledger or AuditLedger()

    def create_review(
        self,
        proposal: str,
        *,
        metadata: dict[str, Any] | None = None,
        source: str = "external_agent",
    ) -> ReviewRecord:
        clean = str(proposal).strip()
        if not clean:
            raise GovernanceError("proposal cannot be empty")

        record = ReviewRecord(
            review_id=f"rev_{uuid4().hex}",
            action_id=f"act_{uuid4().hex}",
            proposal=clean,
            metadata=dict(metadata or {}),
        )
        with self._lock:
            self._records[record.review_id] = record

        self.ledger.append(
            event_type="proposal_created",
            review_id=record.review_id,
            action_id=record.action_id,
            actor=source,
            details={"status": record.status},
        )
        return record

    def get_review(self, review_id: str) -> ReviewRecord:
        with self._lock:
            try:
                return self._records[review_id]
            except KeyError as exc:
                raise GovernanceError(f"unknown review_id: {review_id}") from exc

    def approve(
        self,
        review_id: str,
        *,
        actor: str = "human",
        note: str | None = None,
    ) -> ReviewRecord:
        return self._decide(review_id, "approved", actor=actor, note=note)

    def reject(
        self,
        review_id: str,
        *,
        actor: str = "human",
        note: str | None = None,
    ) -> ReviewRecord:
        return self._decide(review_id, "rejected", actor=actor, note=note)

    def _decide(
        self,
        review_id: str,
        status: Literal["approved", "rejected"],
        *,
        actor: str,
        note: str | None,
    ) -> ReviewRecord:
        clean_actor = str(actor).strip()
        if not clean_actor:
            raise GovernanceError("actor cannot be empty")

        with self._lock:
            record = self.get_review(review_id)
            if record.status != "pending_human":
                raise GovernanceError(
                    f"review {review_id} is already final: {record.status}"
                )
            record.status = status
            record.decided_by = clean_actor
            record.decision_note = note

        self.ledger.append(
            event_type=f"human_{status}",
            review_id=record.review_id,
            action_id=record.action_id,
            actor=clean_actor,
            details={"note": note, "dispatch_authorized": record.dispatch_authorized},
        )
        return record

    def record_outcome(
        self,
        review_id: str,
        outcome: str,
        *,
        actor: str = "integrating_system",
    ) -> ReviewRecord:
        clean_outcome = str(outcome).strip()
        if not clean_outcome:
            raise GovernanceError("outcome cannot be empty")

        with self._lock:
            record = self.get_review(review_id)
            if record.status == "pending_human":
                raise GovernanceError("outcome cannot be recorded before human decision")
            if record.outcome is not None:
                raise GovernanceError("outcome is already recorded")
            record.outcome = clean_outcome

        self.ledger.append(
            event_type="outcome_recorded",
            review_id=record.review_id,
            action_id=record.action_id,
            actor=str(actor),
            details={"outcome": clean_outcome, "decision": record.status},
        )
        return record

    def audit(self, review_id: str) -> list[dict[str, Any]]:
        self.get_review(review_id)
        return self.ledger.for_review(review_id)

