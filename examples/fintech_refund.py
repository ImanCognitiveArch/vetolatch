"""
VetoLatch end-to-end example: governed high-value refund authorization.

ROLE
----
Demonstrate the real public Python contract without connecting to a bank,
payment processor, or the private UniversalMind Core. This example never
transfers money.

Run:
    python examples/fintech_refund.py
"""

from vetolatch import GovernanceEngine


def main() -> None:
    gate = GovernanceEngine()

    print("\n[1] AGENT PROPOSAL")
    review = gate.create_review(
        "Refund $4,500 to customer #8841 after duplicate billing investigation.",
        metadata={
            "workflow": "refund",
            "amount_usd": 4500,
            "customer_id": "8841",
        },
        source="mock_support_agent",
    )

    print("review_id:", review.review_id)
    print("action_id:", review.action_id)
    print("status:", review.status)
    print("dispatch_authorized:", review.dispatch_authorized)
    assert review.status == "pending_human"
    assert review.dispatch_authorized is False

    print("\n[2] HUMAN AUTHORITY BOUNDARY")
    raw = input("Type approve or reject: ").strip().lower()
    if raw not in {"approve", "reject"}:
        raise SystemExit("No decision recorded. Nothing is authorized.")

    if raw == "approve":
        decided = gate.approve(
            review.review_id,
            actor="finance_manager",
            note="Duplicate charge verified in mock scenario.",
        )
    else:
        decided = gate.reject(
            review.review_id,
            actor="finance_manager",
            note="Operator rejected the mock refund.",
        )

    print("status:", decided.status)
    print("same_action_id:", decided.action_id == review.action_id)
    print("dispatch_authorized:", decided.dispatch_authorized)

    if not decided.dispatch_authorized:
        print("\n[3] EXTERNAL EXECUTION")
        print("BLOCKED: no external side effect is authorized.")
        gate.record_outcome(
            review.review_id,
            "Mock workflow closed without dispatch.",
            actor="mock_refund_adapter",
        )
    else:
        print("\n[3] EXTERNAL EXECUTION")
        print("AUTHORIZED: an integrating system could now execute.")
        print("DEMO SAFETY: this example does not call a bank API.")
        gate.record_outcome(
            review.review_id,
            "Mock adapter reported simulated success; no funds moved.",
            actor="mock_refund_adapter",
        )

    print("\n[4] AUDIT EVENTS")
    for event in gate.audit(review.review_id):
        print(event["event_type"], event["review_id"], event["action_id"])


if __name__ == "__main__":
    main()
