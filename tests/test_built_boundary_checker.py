"""Negative controls for the release artifact inspection, without private code."""
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts" / "check_distribution_boundary.py"
spec = importlib.util.spec_from_file_location("distribution_checker", path)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def test_private_import_is_rejected_in_built_python():
    assert checker.inspect_members([
        ("vetolatch/adapter.py", b"from brain_bus import Example")
    ], wheel=True) == ["vetolatch/adapter.py:private-import"]


def test_unexpected_package_and_secret_file_are_rejected():
    assert checker.inspect_members([
        ("other_package/__init__.py", b""),
        ("vetolatch/.env", b"FAKE_EXAMPLE_ONLY=1"),
    ], wheel=True) == ["other_package/__init__.py", "vetolatch/.env"]


def test_documented_provenance_is_allowed():
    assert checker.inspect_members([
        ("vetolatch/__init__.py", b'"""Private RuntimeKernel is excluded."""'),
        ("vetolatch-0.4.0a1.dist-info/METADATA", b"Name: vetolatch"),
    ], wheel=True) == []
