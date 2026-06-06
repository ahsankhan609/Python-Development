"""Log validation errors to file and show them to the user on the console.

Demonstrates a custom logger with separate file and console handlers: DEBUG+
messages go to ``my_log.log``, while ERROR+ messages also appear on stderr so
the user sees feedback when input is invalid.
"""

import logging
import sys

LOG_FILE: str = "my_log.log"


def configure_logger() -> logging.Logger:
    """Create a logger that writes DEBUG+ to file and ERROR+ to the console."""
    app_logger: logging.Logger = logging.getLogger(__name__)
    app_logger.setLevel(logging.DEBUG)
    app_logger.handlers.clear()

    file_formatter: logging.Formatter = logging.Formatter(
        "\n{asctime} {lineno}:{levelname}:{name}:{message}-{process}-{thread}:",
        style="{",
    )
    console_formatter: logging.Formatter = logging.Formatter(
        "%(levelname)s: %(message)s",
    )

    file_handler: logging.FileHandler = logging.FileHandler(
        LOG_FILE,
        mode="a",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(console_formatter)

    app_logger.addHandler(file_handler)
    app_logger.addHandler(console_handler)
    return app_logger


def read_valid_age(app_logger: logging.Logger) -> int:
    """Prompt until the user enters a non-negative integer age."""
    while True:
        raw: str = input("Enter your age: ")
        try:
            age: int = int(raw)
            if age < 0:
                msg: str = "Age cannot be negative"
                raise ValueError(msg)
        except ValueError as exc:
            app_logger.error("Invalid input %r: %s", raw, exc)
        else:
            return age


def main() -> None:
    """Run the age input demo."""
    app_logger: logging.Logger = configure_logger()
    age: int = read_valid_age(app_logger)
    app_logger.info("Valid age entered: %d", age)
    app_logger.warning("Thank you. Your age is %d.", age)


if __name__ == "__main__":
    main()
