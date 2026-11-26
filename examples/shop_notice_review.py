"""Review a shop notice locally with VetoLatch; no notice is posted or sent.

This evaluation example uses the public SDK only. Approval releases a preview
to this terminal, never an email/social account. Actor labels are not verified
identities; this in-memory flow is not an authenticated production service.
"""
from vetolatch import GovernanceEngine

NOTICE = "Example shop notice: our window display will change for one afternoon."


def main() -> None:
    gate = GovernanceEngine()
    review = gate.create_review(
        NOTICE,
        source="synthetic_notice_draft",
        metadata={"workflow": "shop_notice", "delivery": "terminal_preview_only"},
    )
    print("Synthetic notice:", NOTICE)
    print("status:", review.status)
    print("dispatch_authorized:", review.dispatch_authorized)
    raw = input("Review the exact notice. Type approve or reject: ").strip().lower()
    if raw not in {"approve", "reject"}:
        print("BLOCKED: no valid decision. Nothing was released.")
        return
    if raw == "approve":
        decision = gate.approve(review.review_id, actor="local_operator")
    else:
        decision = gate.reject(review.review_id, actor="local_operator")
    if decision.dispatch_authorized:
        # This adapter only renders a preview; it has no publishing capability.
        print("APPROVED PREVIEW:", NOTICE)
        outcome = "Preview rendered in terminal; no notice posted or sent."
    else:
        print("BLOCKED: the notice was rejected.")
        outcome = "Closed without releasing a preview; no notice posted or sent."
    gate.record_outcome(review.review_id, outcome, actor="terminal_preview_adapter")
    print("same_action_id:", decision.action_id == review.action_id)
    print("audit_events:", [event["event_type"] for event in gate.audit(review.review_id)])
    print(outcome)


if __name__ == "__main__":
    main()
