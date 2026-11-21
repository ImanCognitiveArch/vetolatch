"""Example-only tool adapter: human approval before in-memory SQLite dispatch.
The SDK records authority; this external adapter executes the tool. No model/API key.
Run: python examples/tool_calling.py
"""
import json
import sqlite3
from functools import wraps

from vetolatch import GovernanceEngine

gate = GovernanceEngine()


def veto_gate(tool):
    """Bind one proposal to one call; deny by default at the human boundary."""
    @wraps(tool)
    def guarded(*, decide=input, **arguments):
        # Freeze JSON arguments before review so dispatch uses the reviewed values.
        approved_arguments = json.loads(json.dumps(arguments))
        review = gate.create_review(
            json.dumps({"name": tool.__name__, "arguments": approved_arguments}),
            source="tool_call_example",
        )
        print("PENDING", review.review_id, review.action_id)
        choice = decide("Type approve or reject: ").strip().lower()
        if choice == "approve":
            gate.approve(review.review_id, actor="local_operator")
        else:
            gate.reject(review.review_id, actor="local_operator")
        if not gate.get_review(review.review_id).dispatch_authorized:
            print("BLOCKED: tool was not executed")
            return review.review_id, None
        # Execution belongs to this adapter, never to the governance SDK.
        result = tool(**approved_arguments)
        gate.record_outcome(review.review_id, str(result), actor="local_operator")
        return review.review_id, result
    return guarded


@veto_gate
def drop_table(*, table):
    """A real SQL operation confined to a disposable in-memory demo database."""
    if table != "demo":
        raise ValueError("Only the disposable demo table is allowed")
    with sqlite3.connect(":memory:") as database:
        database.execute("CREATE TABLE demo (id INTEGER)")
        database.execute("DROP TABLE demo")
    return "Dropped demo table in memory; no persistent database touched."


def dispatch(call, *, decide=input):
    """Accept an OpenAI-style function payload, with a fixed tool allowlist."""
    if call["name"] != "drop_table":
        raise ValueError("Unknown tool")
    return drop_table(decide=decide, **json.loads(call["arguments"]))


if __name__ == "__main__":
    tool_call = {"name": "drop_table", "arguments": '{"table": "demo"}'}
    review_id, result = dispatch(tool_call)
    print(result)
    for event in gate.audit(review_id):
        print(event["event_type"], event["review_id"], event["action_id"])
