"""
VetoLatch audit primitives.

ROLE
----
Provide an append-only-in-process event ledger for governance receipts. This is
an auditable event history, not a cryptographically immutable ledger.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from threading import RLock
from typing import Any


@dataclass(frozen=True)
class AuditEvent:
    """One immutable event in a review's local governance history."""

    event_type: str
    review_id: str
    action_id: str
    timestamp: str
    actor: str
    details: dict[str, Any]


class AuditLedger:
    """Thread-safe append-only event ledger owned by the public SDK."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []
        self._lock = RLock()

    def append(
        self,
        *,
        event_type: str,
        review_id: str,
        action_id: str,
        actor: str,
        details: dict[str, Any] | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            event_type=event_type,
            review_id=review_id,
            action_id=action_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            actor=actor,
            details=dict(details or {}),
        )
        with self._lock:
            self._events.append(event)
        return event

    def for_review(self, review_id: str) -> list[dict[str, Any]]:
        with self._lock:
            return [asdict(event) for event in self._events if event.review_id == review_id]

    def all_events(self) -> list[dict[str, Any]]:
        with self._lock:
            return [asdict(event) for event in self._events]

