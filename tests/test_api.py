"""HTTP contract tests for the standalone local governance API."""

from fastapi.testclient import TestClient

from universalmind.api import app, engine


client = TestClient(app)


def setup_function():
    # Tests use a fresh in-memory engine state by replacing its private stores
    # only inside the test process; production callers use the public methods.
    engine._records.clear()
    engine.ledger._events.clear()


def test_health_and_workbench_are_available():
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"

    ui = client.get("/")
    assert ui.status_code == 200
    assert "AI may propose" in ui.text


def test_review_requires_explicit_human_decision():
    created = client.post(
        "/reviews",
        json={"proposal": "Refund $4,500", "metadata": {"amount": 4500}},
    )
    assert created.status_code == 201
    body = created.json()
    assert body["status"] == "pending_human"
    assert body["dispatch_authorized"] is False

    approved = client.post(
        f"/reviews/{body['review_id']}/approve",
        json={"actor": "finance_manager", "note": "verified"},
    )
    assert approved.status_code == 200
    assert approved.json()["action_id"] == body["action_id"]
    assert approved.json()["dispatch_authorized"] is True


def test_unknown_review_returns_404():
    response = client.get("/reviews/rev_missing")
    assert response.status_code == 404
