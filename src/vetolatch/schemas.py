"""
VetoLatch public API schemas.

ROLE
----
Define transport contracts for the standalone governance SDK. These schemas do
not expose private cognitive-runtime structures.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class CreateReviewRequest(BaseModel):
    proposal: str = Field(min_length=1, max_length=20_000)
    metadata: dict[str, Any] = Field(default_factory=dict)
    source: str = Field(default="external_agent", min_length=1, max_length=200)


class DecisionRequest(BaseModel):
    actor: str = Field(default="human", min_length=1, max_length=200)
    note: str | None = Field(default=None, max_length=10_000)


class OutcomeRequest(BaseModel):
    outcome: str = Field(min_length=1, max_length=20_000)
    actor: str = Field(default="integrating_system", min_length=1, max_length=200)


class ReviewResponse(BaseModel):
    review_id: str
    action_id: str
    proposal: str
    status: str
    metadata: dict[str, Any]
    decided_by: str | None
    decision_note: str | None
    outcome: str | None
    dispatch_authorized: bool


class AuditResponse(BaseModel):
    review_id: str
    events: list[dict[str, Any]]

