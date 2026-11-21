"""Allow `python -m vetolatch` to invoke the public SDK CLI."""

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())

