"""Reading environment variables from a .env file.

Demonstrates how to securely load secrets and configuration values
from a project-root ``.env`` file using ``python-dotenv``.

Why .env?
---------
Hard-coding secrets (API keys, passwords, URLs) in source code is a
security risk — they end up in version control.  A ``.env`` file stays
out of git (add it to ``.gitignore``) and keeps secrets separate from code.

How it works:
    1. ``load_dotenv()`` reads the ``.env`` file and injects each
       ``KEY=VALUE`` pair into ``os.environ``.
    2. ``os.getenv("KEY")`` retrieves the value, returning ``None``
       when the variable is missing.

Usage:
    uv run python 04_misc_python/reading_secrets.py
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# parents[0] = reading_env_variables/, parents[1] = 04_misc_python/, parents[2] = project root
_ENV_FILE: Path = Path(__file__).parents[2] / ".env"

load_dotenv(_ENV_FILE)  # injects .env variables into os.environ


def get_secret(key: str) -> str:
    """Return the value of an environment variable, raising if it is missing.

    Args:
        key: The environment variable name.

    Raises:
        KeyError: If *key* is not set after loading the .env file.

    """
    value: str | None = os.getenv(key)
    if value is None:
        msg: str = (
            f"Environment variable {key!r} not found. "
            f"Make sure it is defined in {_ENV_FILE}."
        )
        raise KeyError(msg)
    return value


if __name__ == "__main__":
    keys: list[str] = [
        "SWAPI_BASE_URL",
        "SECRET_1",
        "SECRET_2",
    ]

    print(f"Loaded from: {_ENV_FILE}\n")  # noqa: T201
    for k in keys:
        try:
            print(f"{k} = {get_secret(k)}")  # noqa: T201
        except KeyError as e:
            print(f"  Missing: {e}")  # noqa: T201
