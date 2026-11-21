"""
UniversalMind standalone local API.

ROLE
----
Expose the public governance state machine over HTTP for local integrations.
The API authorizes or denies dispatch; it never performs the external action.

SECURITY BOUNDARY
-----------------
This first public SDK has no authentication. The CLI therefore binds only to
loopback addresses. Production deployment requires a separately licensed and
secured integration.
"""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from . import __version__
from .governance import GovernanceEngine, GovernanceError
from .schemas import (
    AuditResponse,
    CreateReviewRequest,
    DecisionRequest,
    OutcomeRequest,
    ReviewResponse,
)


engine = GovernanceEngine()
app = FastAPI(
    title="UniversalMind Governance SDK",
    version=__version__,
    description=(
        "Human-governed approval and audit boundary for proposed AI-agent actions. "
        "This service does not execute external actions."
    ),
)


def _review_response(review_id: str) -> ReviewResponse:
    return ReviewResponse.model_validate(engine.get_review(review_id).to_dict())


def _governance_error(exc: GovernanceError) -> HTTPException:
    message = str(exc)
    status = 404 if message.startswith("unknown review_id") else 409
    return HTTPException(status_code=status, detail=message)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}


@app.get("/", include_in_schema=False)
def workbench_ui():
    index = Path(__file__).resolve().parent / "static" / "index.html"
    return FileResponse(index)


@app.post("/reviews", response_model=ReviewResponse, status_code=201)
def create_review(request: CreateReviewRequest) -> ReviewResponse:
    try:
        record = engine.create_review(
            request.proposal,
            metadata=request.metadata,
            source=request.source,
        )
        return ReviewResponse.model_validate(record.to_dict())
    except GovernanceError as exc:
        raise _governance_error(exc) from exc


@app.get("/reviews/{review_id}", response_model=ReviewResponse)
def get_review(review_id: str) -> ReviewResponse:
    try:
        return _review_response(review_id)
    except GovernanceError as exc:
        raise _governance_error(exc) from exc


@app.post("/reviews/{review_id}/approve", response_model=ReviewResponse)
def approve_review(review_id: str, request: DecisionRequest) -> ReviewResponse:
    try:
        record = engine.approve(review_id, actor=request.actor, note=request.note)
        return ReviewResponse.model_validate(record.to_dict())
    except GovernanceError as exc:
        raise _governance_error(exc) from exc


@app.post("/reviews/{review_id}/reject", response_model=ReviewResponse)
def reject_review(review_id: str, request: DecisionRequest) -> ReviewResponse:
    try:
        record = engine.reject(review_id, actor=request.actor, note=request.note)
        return ReviewResponse.model_validate(record.to_dict())
    except GovernanceError as exc:
        raise _governance_error(exc) from exc


@app.post("/reviews/{review_id}/outcome", response_model=ReviewResponse)
def record_outcome(review_id: str, request: OutcomeRequest) -> ReviewResponse:
    try:
        record = engine.record_outcome(
            review_id,
            request.outcome,
            actor=request.actor,
        )
        return ReviewResponse.model_validate(record.to_dict())
    except GovernanceError as exc:
        raise _governance_error(exc) from exc


@app.get("/reviews/{review_id}/audit", response_model=AuditResponse)
def audit_review(review_id: str) -> AuditResponse:
    try:
        return AuditResponse(review_id=review_id, events=engine.audit(review_id))
    except GovernanceError as exc:
        raise _governance_error(exc) from exc
