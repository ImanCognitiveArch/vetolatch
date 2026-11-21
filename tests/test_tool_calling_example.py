"""Exercise the human boundary of the external example, including actual dispatch."""
import importlib.util
from pathlib import Path

import pytest

@pytest.fixture
def adapter():
    path = Path(__file__).resolve().parents[1] / "examples" / "tool_calling.py"
    spec = importlib.util.spec_from_file_location("tool_calling_example", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@pytest.mark.parametrize("decision", ["reject", "", "yes", "APPROVED"])
def test_nonapproval_never_calls_tool(adapter, decision):
    executions = []
    guarded = adapter.veto_gate(lambda **kw: executions.append(kw))
    review_id, result = guarded(decide=lambda _: decision, table="demo")
    assert executions == []
    assert result is None
    assert adapter.gate.get_review(review_id).status == "rejected"

def test_approval_dispatches_exact_reviewed_arguments_once(adapter):
    executions = []
    def tool(**kw):
        executions.append(kw)
        return "simulated success"
    guarded = adapter.veto_gate(tool)
    review_id, result = guarded(decide=lambda _: "approve", table="demo")
    assert executions == [{"table": "demo"}]
    assert result == "simulated success"
    events = adapter.gate.audit(review_id)
    assert [e["event_type"] for e in events] == [
        "proposal_created", "human_approved", "outcome_recorded"
    ]
    assert len({e["action_id"] for e in events}) == 1

def test_standard_tool_payload_executes_in_memory_sql(adapter):
    review_id, result = adapter.dispatch(
        {"name": "drop_table", "arguments": '{"table": "demo"}'},
        decide=lambda _: "approve",
    )
    assert result.startswith("Dropped demo table in memory")
    assert adapter.gate.get_review(review_id).dispatch_authorized

def test_unknown_tool_fails_without_review(adapter):
    with pytest.raises(ValueError, match="Unknown tool"):
        adapter.dispatch({"name": "send_wire", "arguments": "{}"})
    assert adapter.gate.ledger is not None

def test_approval_cannot_expand_demo_database_scope(adapter):
    with pytest.raises(ValueError, match="disposable"):
        adapter.dispatch(
            {"name": "drop_table", "arguments": '{"table": "production"}'},
            decide=lambda _: "approve",
        )
