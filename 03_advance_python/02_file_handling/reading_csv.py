"""Read employees.csv and print each row as an Employee namedtuple."""

import csv
from pathlib import Path
from typing import NamedTuple


def read_csv_file(csv_path: Path) -> None:
    """_Return data inside the CSV File_.

    Args:
        csv_path (Path): CSV file name with path

    """
    try:
        # csv_path = Path(__file__).parent / "data/employees.csv"
        with csv_path.open(mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            Employee = NamedTuple(
                "Employee", [(field, str) for field in next(reader)])
            for row in reader:
                employee = Employee(*row)
                print(employee)
                """
                print statements used for debugging should be omitted from production code. They can lead the accidental inclusion of sensitive information in logs, and are not configurable by
                clients, unlike logging statements.
                https://docs.astral.sh/ruff/rules/print/
                """  # noqa: E501
    except FileNotFoundError:
        print("The file 'employees.csv' was not found.")
    except OSError as e:
        print(f"An error occurred while reading the file: {e}")


if __name__ == "__main__":
    read_csv_file(Path(__file__).parent / "data/employees.csv")
