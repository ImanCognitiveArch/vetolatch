"""Inspect built distributions for the documented private-Core boundary.
ROLE: fail CI on unexpected wheel packages, private module paths/imports or secret
filenames. This scoped check is evidence, not a general proof of zero disclosure.
"""
import ast
from pathlib import Path
import tarfile
import zipfile

PRIVATE = {"brain_bus", "collective_intelligence", "evolution", "self_improvement",
           "runtimekernel", "genome", "cognitiveentity", "stigmergic", "scl"}
SECRET_NAMES = {".env", ".pypirc", "credentials.json", "id_rsa", "id_ed25519"}


def inspect_members(members, *, wheel=False):
    forbidden = []
    for name, data in members:
        path = Path(name)
        parts = {part.lower() for part in path.parts}
        if parts & PRIVATE or path.stem.lower() in PRIVATE or path.name in SECRET_NAMES:
            forbidden.append(name)
        if wheel and not (path.parts[0] == "vetolatch"
                          or path.parts[0].endswith(".dist-info")):
            forbidden.append(name)
        if path.suffix != ".py":
            continue
        for node in ast.walk(ast.parse(data.decode("utf-8"), filename=name)):
            modules = ([node.module or ""] if isinstance(node, ast.ImportFrom)
                       else [alias.name for alias in node.names]
                       if isinstance(node, ast.Import) else [])
            if any(set(module.lower().split(".")) & PRIVATE for module in modules):
                forbidden.append(name + ":private-import")
    return sorted(set(forbidden))


def main():
    wheels = sorted(Path("dist").glob("*.whl"))
    sources = sorted(Path("dist").glob("*.tar.gz"))
    if len(wheels) != 1 or len(sources) != 1:
        raise SystemExit("Expected exactly one wheel and one sdist in dist/")
    forbidden = []
    for archive in wheels:
        with zipfile.ZipFile(archive) as package:
            forbidden += inspect_members(
                [(n, package.read(n)) for n in package.namelist() if not n.endswith("/")],
                wheel=True,
            )
    for archive in sources:
        with tarfile.open(archive) as package:
            forbidden += inspect_members(
                [(m.name, package.extractfile(m).read()) for m in package if m.isfile()]
            )
    print("FORBIDDEN=" + json_list(forbidden))
    if forbidden:
        raise SystemExit(1)


def json_list(items):
    import json
    return json.dumps(sorted(set(items)))


if __name__ == "__main__":
    main()
