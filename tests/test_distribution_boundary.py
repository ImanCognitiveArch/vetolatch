"""Prevent private UniversalMind Core modules from entering the public SDK."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_MARKERS = {
    "brain_bus",
    "collective_intelligence",
    "evolution",
    "self_improvement",
    "RuntimeKernel",
    "stigmergic",
}


def test_public_source_tree_contains_only_public_package():
    source_root = ROOT / "src"
    top_level = {
        path.name
        for path in source_root.iterdir()
        if not path.name.endswith(".egg-info") and path.name != "__pycache__"
    }
    assert top_level == {"universalmind"}


def test_public_python_does_not_reference_private_core_imports():
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (ROOT / "src" / "universalmind").rglob("*.py")
    )
    forbidden_imports = [
        "from brain_bus",
        "import brain_bus",
        "from collective_intelligence",
        "import collective_intelligence",
        "from evolution",
        "from self_improvement",
    ]
    for marker in forbidden_imports:
        assert marker not in text


def test_private_markers_are_not_package_directories():
    package_root = ROOT / "src" / "universalmind"
    names = {path.name for path in package_root.rglob("*")}
    assert not (PRIVATE_MARKERS & names)
