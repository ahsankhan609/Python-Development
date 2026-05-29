"""Demonstrate ExceptionGroup (Python 3.11+) with real-life scenarios.

ExceptionGroup bundles multiple exceptions raised during a single operation
(for example, parallel tasks or batch validation) so callers can inspect every
failure instead of stopping at the first one.

Key APIs:
- ExceptionGroup(message, exceptions)
- except* SomeError  — handle matching exceptions inside a group
- group.exceptions   — tuple of nested exceptions (groups can nest)
"""

from __future__ import annotations

import asyncio
from pathlib import Path

# ---------------------------------------------------------------------------
# Example 1: Bulk CSV import — collect every bad row, not just the first
# ---------------------------------------------------------------------------


def parse_age(raw_age: str) -> int:
    """Parse an age string into a positive integer."""
    age: int = int(raw_age)
    if age < 0 or age > 120:
        raise ValueError(f"age out of range: {age}")
    return age


def import_users(rows: list[dict[str, str]]) -> list[dict[str, int | str]]:
    """Import user rows and raise one ExceptionGroup if any row fails."""
    valid_users: list[dict[str, int | str]] = []
    row_errors: list[Exception] = []

    for index, row in enumerate(rows, start=1):
        try:
            user: dict[str, int | str] = {
                "name": row["name"],
                "age": parse_age(row["age"]),
            }
            valid_users.append(user)
        except (KeyError, ValueError) as exc:
            # Wrap the row index so the caller knows which record failed.
            row_errors.append(ValueError(f"row {index} ({row!r}): {exc}"))

    if row_errors:
        raise ExceptionGroup("user import failed", row_errors)

    return valid_users


# ---------------------------------------------------------------------------
# Example 2: Service health check — report all broken dependencies at once
# ---------------------------------------------------------------------------


def check_database() -> None:
    """Simulate a database connectivity check."""
    raise ConnectionError("postgres: connection refused on port 5432")


def check_redis() -> None:
    """Simulate a Redis connectivity check."""
    raise TimeoutError("redis: timed out after 3s")


def check_disk_space() -> None:
    """Simulate a disk space check."""
    raise OSError("disk: only 2% free on /var")


def run_health_checks() -> None:
    """Run dependency checks and raise a single group if any check fails."""
    failures: list[Exception] = []

    for check in (check_database, check_redis, check_disk_space):
        try:
            check()
        except Exception as exc:  # noqa: BLE001 — demo: collect any check failure
            failures.append(exc)

    if failures:
        raise ExceptionGroup("health check failed", failures)


# ---------------------------------------------------------------------------
# Example 3: Parallel file validation — every invalid file is reported
# ---------------------------------------------------------------------------


def validate_config_file(path: Path) -> None:
    """Validate that a config file exists and is non-empty."""
    if not path.exists():
        raise FileNotFoundError(f"missing config: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"empty config: {path}")


def validate_all_configs(paths: list[Path]) -> None:
    """Validate multiple config files and group all validation errors."""
    errors: list[Exception] = []

    for path in paths:
        try:
            validate_config_file(path)
        except (FileNotFoundError, ValueError) as exc:
            errors.append(exc)

    if errors:
        raise ExceptionGroup("config validation failed", errors)


# ---------------------------------------------------------------------------
# Example 4: Handling groups with except* (Python 3.11+)
# ---------------------------------------------------------------------------


def handle_import_errors() -> None:
    """Demonstrate selective handling of exceptions inside a group."""
    bad_rows: list[dict[str, str]] = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob"},  # missing age
        {"name": "Carol", "age": "not-a-number"},
    ]

    try:
        import_users(bad_rows)
    except* ValueError as group:
        # Handles every ValueError nested in the group (including wrapped ones).
        print(f"found {len(group.exceptions)} value errors:")
        for exc in group.exceptions:
            print(f"  - {exc}")
    except* KeyError as group:
        print(f"found {len(group.exceptions)} missing-field errors")


# ---------------------------------------------------------------------------
# Example 5: asyncio TaskGroup — real source of ExceptionGroup in production
# ---------------------------------------------------------------------------


async def fetch_user(user_id: int) -> dict[str, int | str]:
    """Simulate an async API call that may fail."""
    if user_id == 2:
        raise ConnectionError(f"API timeout for user {user_id}")
    if user_id == 4:
        raise ValueError(f"invalid user payload for user {user_id}")
    return {"id": user_id, "name": f"user-{user_id}"}


async def fetch_all_users(user_ids: list[int]) -> list[dict[str, int | str]]:
    """Fetch users concurrently; TaskGroup raises ExceptionGroup on failure."""
    results: list[dict[str, int | str]] = []

    async with asyncio.TaskGroup() as task_group:
        tasks = [task_group.create_task(fetch_user(uid)) for uid in user_ids]

    for task in tasks:
        results.append(task.result())

    return results


async def demo_async_task_group() -> None:
    """Show how asyncio surfaces multiple task failures as an ExceptionGroup."""
    try:
        await fetch_all_users([1, 2, 3, 4])
    except* ConnectionError as group:
        print(f"network errors: {group.exceptions}")
    except* ValueError as group:
        print(f"data errors: {group.exceptions}")


# ---------------------------------------------------------------------------
# Run demos
# ---------------------------------------------------------------------------


def main() -> None:
    """Run interactive demos for each real-life ExceptionGroup scenario."""
    print("=== Example 1: bulk CSV import ===")
    try:
        import_users(
            [
                {"name": "Alice", "age": "28"},
                {"name": "Bob", "age": "-5"},
                {"age": "30"},
            ]
        )
    except ExceptionGroup as group:
        print(group)
        print("nested exceptions:", group.exceptions)

    print("\n=== Example 2: health checks ===")
    try:
        run_health_checks()
    except ExceptionGroup as group:
        for exc in group.exceptions:
            print(f"  - {type(exc).__name__}: {exc}")

    print("\n=== Example 3: config validation ===")
    empty_config: Path = Path("empty_config.toml")
    empty_config.write_text("")
    try:
        validate_all_configs([Path("missing.toml"), empty_config])
    except ExceptionGroup as group:
        print(group)
    finally:
        empty_config.unlink(missing_ok=True)

    print("\n=== Example 4: except* handling ===")
    handle_import_errors()

    print("\n=== Example 5: asyncio TaskGroup ===")
    asyncio.run(demo_async_task_group())


if __name__ == "__main__":
    main()
