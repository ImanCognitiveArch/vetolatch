"""Contract tests for the standalone public governance engine."""

import pytest

from universalmind import GovernanceEngine, GovernanceError


def test_review_starts_pending_and_unauthorized():
    engine = GovernanceEngine()
    review = engine.create_review("Deploy database migration")

    assert review.status == "pending_human"
    assert review.dispatch_authorized is False
    assert review.review_id.startswith("rev_")
    assert review.action_id.startswith("act_")


def test_human_approval_preserves_identity_and_authorizes_dispatch():
    engine = GovernanceEngine()
    review = engine.create_review("Issue customer refund")

    approved = engine.approve(review.review_id, actor="finance_manager")

    assert approved.review_id == review.review_id
    assert approved.action_id == review.action_id
    assert approved.status == "approved"
    assert approved.dispatch_authorized is True


def test_rejection_never_authorizes_dispatch():
    engine = GovernanceEngine()
    review = engine.create_review("Rotate production credentials")

    rejected = engine.reject(review.review_id, actor="security_lead")

    assert rejected.status == "rejected"
    assert rejected.dispatch_authorized is False


def test_final_decision_cannot_be_overwritten():
    engine = GovernanceEngine()
    review = engine.create_review("Change account limit")
    engine.approve(review.review_id)

    with pytest.raises(GovernanceError, match="already final"):
        engine.reject(review.review_id)


def test_outcome_requires_human_decision_and_is_single_assignment():
    engine = GovernanceEngine()
    review = engine.create_review("Refund customer")

    with pytest.raises(GovernanceError, match="before human decision"):
        engine.record_outcome(review.review_id, "completed")

    engine.approve(review.review_id)
    completed = engine.record_outcome(review.review_id, "completed")
    assert completed.outcome == "completed"

    with pytest.raises(GovernanceError, match="already recorded"):
        engine.record_outcome(review.review_id, "changed")


def test_audit_records_proposal_decision_and_outcome_with_same_ids():
    engine = GovernanceEngine()
    review = engine.create_review("Refund customer")
    engine.approve(review.review_id, actor="manager")
    engine.record_outcome(review.review_id, "refund_sent")

    events = engine.audit(review.review_id)
    assert [event["event_type"] for event in events] == [
        "proposal_created",
        "human_approved",
        "outcome_recorded",
    ]
    assert {event["review_id"] for event in events} == {review.review_id}
    assert {event["action_id"] for event in events} == {review.action_id}
