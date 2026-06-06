"""One-off helper to commit remaining tidy-project changes one file at a time."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a git command in the repo root."""
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return result


def commit_message(path: str, status: str) -> str:
    """Build a commit message for a single path and change status."""
    if status == "D":
        if "08_iterators_generators" in path:
            body = (
                "Deletes the old 08_iterators_generators path as part of the tidy-project\n"
                "reorg. Content now lives under 03_advance_python/01_iterators_generators."
            )
            summary = f"Remove {path} after iterators folder renumber"
        elif "01_learn_functions" in path:
            body = (
                "Deletes the old 01_learn_functions path. The functions study material was\n"
                "renamed to 02_intermediate_python/01_functions for consistent numbering."
            )
            summary = f"Remove {path} after functions folder rename"
        elif "02_object_orinted_programming" in path or "oop_with_freecodecamp" in path:
            body = (
                "Deletes a stale path under the misspelled or duplicate OOP folders removed\n"
                "during tidy-project. Content now lives under 02_object_oriented_programming."
            )
            summary = f"Remove {path} after OOP folder cleanup"
        elif "01_generators_in_python" in path:
            body = (
                "Deletes 03_advance_python/01_generators_in_python/notes.py after folding\n"
                "generators content into the iterators_generators topic folder."
            )
            summary = "Remove obsolete generators placeholder at old path"
        elif "reading_env_variables" in path or path.endswith("string_module/tmp"):
            body = (
                "Deletes the old path after moving env/secrets examples into secrets_module\n"
                "or replacing string_module/tmp with .gitkeep for GitHub directory tracking."
            )
            summary = f"Remove {path} after misc module consolidation"
        elif path.startswith("01_basic_python/") and path.count("/") == 1:
            body = (
                "Deletes the file from the topic root after tidy-project moved fundamentals\n"
                "scripts and notes into numbered subfolders (01_basics, 02_control_flow, etc.)."
            )
            summary = f"Remove loose basics file from 01_basic_python root"
        elif path.startswith("01_basic_python/data_structures/"):
            body = (
                "Deletes the pre-reorg data_structures path. Files were moved into\n"
                "01_basic_python/03_data_structures with numbered subfolders and 00_overview."
            )
            summary = f"Remove {path} from old data_structures layout"
        elif path.startswith("01_basic_python/modules_and_packages/"):
            body = (
                "Deletes the pre-reorg modules path after renaming the folder to\n"
                "01_basic_python/04_modules_and_packages."
            )
            summary = f"Remove {path} from old modules_and_packages path"
        elif path.startswith("04_misc_python/") and Path(path).name in {
            "NOQA.py",
            "test.py",
            "write_better_docstrings.py",
        }:
            body = (
                "Deletes a loose misc script from the topic root after tidy-project placed it\n"
                "in linting_module, scratch, or docstrings_module."
            )
            summary = f"Remove {path} from 04_misc_python root"
        elif path.startswith("05_projects/") and path.endswith(".txt"):
            body = (
                "Deletes the file from the projects root after organizing notes into oauth/ and\n"
                "sending_emails/ subfolders."
            )
            summary = "Remove loose project note from 05_projects root"
        else:
            body = (
                "Deletes the old file location left behind by the project-wide tidy pass that\n"
                "renumbered topic folders and moved loose scripts into dedicated subfolders."
            )
            summary = f"Remove {path} after tidy-project reorganization"
        return f"{summary}\n\n{body}"

    if status == "M" and path.endswith(".code-workspace"):
        return (
            "Expand workspace cspell dictionary for study-notebook terms\n\n"
            "Adds project-specific words to the cspell list in "
            "Python-Development.code-workspace so linting does not flag legitimate "
            "identifiers and names from notebooks."
        )

    if path == "04_misc_python/string_module/.gitkeep":
        return (
            "Add .gitkeep to track string_module directory on GitHub\n\n"
            "Replaces the empty tmp placeholder with .gitkeep so Git preserves the\n"
            "string_module folder even before study notes are added."
        )
    if path.endswith("generator_02.ipynb") and "01_iterators_generators" in path:
        return (
            "Fix generator notebook types and StopIteration demo\n\n"
            "Moves generator_02.ipynb into 01_iterators_generators and updates the\n"
            "generator example: PEP 696 Generator[int] hints, yield from range(10),\n"
            "and a corrected next()/list()/StopIteration demonstration order."
        )
    if path.endswith("faq.md") and "01_iterators_generators" in path:
        return (
            "Add iterators FAQ entry on generator exhaustion\n\n"
            "Moves faq.md into 01_iterators_generators and documents why next() raises\n"
            "StopIteration after list() fully consumes a generator."
        )
    if "03_advance_python/01_iterators_generators/" in path:
        return (
            f"Add {path} under renumbered iterators topic folder\n\n"
            "Places iterators/generators study material in "
            "03_advance_python/01_iterators_generators after renumbering the topic "
            "from 08_iterators_generators during tidy-project."
        )
    if "02_intermediate_python/01_functions/" in path:
        return (
            f"Add {path} under renamed functions topic folder\n\n"
            "Places functions study material in 02_intermediate_python/01_functions after\n"
            "renaming 01_learn_functions for consistent numbering."
        )
    if "02_intermediate_python/02_object_oriented_programming/" in path:
        return (
            f"Add {path} under corrected OOP topic folder\n\n"
            "Places OOP study material in 02_object_oriented_programming after fixing the\n"
            "orinted typo and removing duplicate oop_with_freecodecamp paths."
        )
    if path.startswith("01_basic_python/01_basics/"):
        return (
            f"Add {path} to numbered basics subfolder\n\n"
            "Moves fundamentals scripts and reference notes from the 01_basic_python root\n"
            "into 01_basics as part of the tidy-project folder structure."
        )
    if path.startswith("01_basic_python/02_control_flow/"):
        return (
            f"Add {path} to numbered control-flow subfolder\n\n"
            "Organizes control-flow examples and notes under 02_control_flow after\n"
            "renaming control_flow and moving truthy/pass material into it."
        )
    if path.startswith("01_basic_python/03_data_structures/"):
        return (
            f"Add {path} to renumbered data structures folder\n\n"
            "Places data-structure lessons under 03_data_structures with numbered\n"
            "subfolders and a 00_overview section for comparison notes."
        )
    if path.startswith("01_basic_python/04_modules_and_packages/"):
        return (
            f"Add {path} to renumbered modules and packages folder\n\n"
            "Places modules/packages examples under 04_modules_and_packages after\n"
            "renaming modules_and_packages during tidy-project."
        )
    if any(
        part in path
        for part in (
            "04_misc_python/linting_module/",
            "04_misc_python/scratch/",
            "04_misc_python/docstrings_module/",
        )
    ):
        return (
            f"Add {path} to dedicated misc module subfolder\n\n"
            "Moves a loose 04_misc_python script into a topic-specific subfolder created\n"
            "during tidy-project (linting, scratch, or docstrings)."
        )
    if "04_misc_python/secrets_module/reading_" in path:
        return (
            f"Add {path} to consolidated secrets module folder\n\n"
            "Moves env-variable and secrets reading examples into secrets_module after\n"
            "removing the separate reading_env_variables folder."
        )
    if path.startswith("05_projects/oauth/") or path.startswith("05_projects/sending_emails/"):
        return (
            f"Add {path} to organized projects subfolder\n\n"
            "Places project planning notes into a topic subfolder under 05_projects instead\n"
            "of leaving loose .txt files at the projects root."
        )
    return (
        f"Add {path} after tidy-project reorganization\n\n"
        "Adds the file at its new location after the project-wide tidy pass renumbered\n"
        "topic folders and moved loose scripts into dedicated subfolders."
    )


def collect_queue() -> list[tuple[str, str]]:
    """Collect and sort pending single-file commit units."""
    status = run("status", "--porcelain", check=True).stdout.splitlines()
    new = run("ls-files", "--others", "--exclude-standard", check=True).stdout.splitlines()

    items: list[tuple[str, str]] = []
    for line in status:
        if not line:
            continue
        code = line[:2].strip()
        path = line[3:].strip().strip('"')
        if code == "M":
            items.append((path, "M"))
        elif code == "D":
            items.append((path, "D"))
    for path in new:
        if path:
            items.append((path, "A"))

    def group_key(item: tuple[str, str]) -> tuple[int, str]:
        path, _ = item
        if path in {".cursorrules"} or path.endswith(".code-workspace") or path.endswith(".toml"):
            return (0, path)
        if path.endswith(".py"):
            return (1, path)
        if path.endswith(".ipynb"):
            return (2, path)
        if path.endswith((".md", ".txt")):
            return (3, path)
        return (4, path)

    return sorted(items, key=group_key)


def main() -> None:
    """Commit and push each queued file."""
    queue = [item for item in collect_queue() if item[0] != ".cursorrules"]
    ok = 0
    for index, (path, status) in enumerate(queue, start=2):
        run("add", "--", path)
        msg = commit_message(path, status)
        commit = run("commit", "-m", msg)
        if commit.returncode != 0:
            print(f"FAIL {index} {path}")
            print(commit.stdout)
            print(commit.stderr)
            raise SystemExit(1)
        push = run("push")
        if push.returncode != 0:
            print(f"PUSH_FAIL {index} {path}")
            print(push.stdout)
            print(push.stderr)
            raise SystemExit(1)
        sha = run("log", "-1", "--format=%h", check=True).stdout.strip()
        ok += 1
        print(f"OK {index} {sha} {path}")
    print(f"DONE committed {ok} units")


if __name__ == "__main__":
    main()
