"""
UniversalMind public-SDK example: governed refund authorization.

ROLE
----
Demonstrate the public contract without connecting to a bank, payment processor,
or private UniversalMind Core. The example never transfers money.
"""

from universalmind import GovernanceEngine


def main() -> None:
    engine = GovernanceEngine()

    review = engine.create_review(
        "Refund $4,500 to customer #8841 after duplicate billing investigation.",
        metadata={
            "workflow": "refund",
            "amount_usd": 4500,
            "customer_id": "8841",
        },
        source="mock_support_agent",
    )

    print("PROPOSAL RECEIVED")
    print("review_id:", review.review_id)
    print("action_id:", review.action_id)
    print("status:", review.status)
    print("dispatch_authorized:", review.dispatch_authorized)

    # In a real integration, an authenticated human-review surface would make
    # this call. This example keeps the decision explicit and local.
    decision = engine.approve(
        review.review_id,
        actor="finance_manager",
        note="Duplicate charge verified; refund approved.",
    )

    print("\nHUMAN DECISION")
    print("status:", decision.status)
    print("dispatch_authorized:", decision.dispatch_authorized)

    # The SDK does not execute the refund. The integrating application remains
    # responsible for dispatch and then records the observed real-world result.
    final = engine.record_outcome(
        review.review_id,
        "mock_refund_adapter reported success",
        actor="mock_refund_adapter",
    )

    print("\nOUTCOME RECORDED")
    print("outcome:", final.outcome)
    print("audit_events:", len(engine.audit(review.review_id)))


if __name__ == "__main__":
    main()
