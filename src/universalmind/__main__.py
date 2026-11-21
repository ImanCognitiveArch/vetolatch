"""Allow `python -m universalmind` to invoke the public SDK CLI."""

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())
