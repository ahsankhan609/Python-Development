"""Binary Bit Explorer

Demonstrates how text and integers are represented at the binary level.

Every character is encoded in ASCII / UTF-8.  The pipeline looks like:

    character  →  decimal (code-point)  →  binary bits (8 bits per byte)

Example
-------
    'H'  →  72  →  01001000

    Bits are read right-to-left:
        position:  7  6  5  4  3  2  1  0
        bit value: 0  1  0  0  1  0  0  0
                   64 32 16  8  4  2  1  0
        sum:       0 +32 +0  +8 +0  +0 +0 +0 = 72  ✓

Usage
-----
    convert_text("hello world")   # str  → shows char / decimal / bits per character
    convert_text(72)              # int  → shows decimal / bits / corresponding character
"""

_SEPARATOR = "-" * 40


def _bits(value: int) -> str:
    """Return the binary string for *value*, zero-padded to the nearest full byte.

    Standard ASCII fits in 8 bits; larger Unicode code-points are padded to
    the next multiple of 8 so the output always represents whole bytes.
    """
    byte_count: int = max(1, (value.bit_length() + 7) // 8)
    return format(value, f"0{byte_count * 8}b")


def _safe_char(char: str) -> str:
    """Return *char* itself when printable and encodable in the current terminal.

    Falls back to repr() for control characters or characters outside the
    terminal's codec (e.g. emoji on a cp1252 Windows console).
    """
    import sys

    if not char.isprintable():
        return repr(char)
    try:
        char.encode(sys.stdout.encoding or "utf-8")
        return char
    except (UnicodeEncodeError, LookupError):
        # ascii() produces a pure-ASCII escape like \U0001f40d, safe for any terminal.
        return ascii(char).strip("'")


def _show_int(value: int) -> None:
    """Print decimal → bits → character for a single integer code-point.

    Args:
        value: A non-negative integer within the Unicode range 0–1,114,111.

    Raises:
        ValueError: If *value* is outside the valid Unicode range.
    """
    if not (0 <= value <= 1_114_111):
        raise ValueError(
            f"Integer {value!r} is outside the Unicode range 0–1,114,111."
        )

    char: str = chr(value)
    print(f"{'Decimal':<14} {'Bits':<26} {'Character'}")
    print(_SEPARATOR)
    print(f"{value:<14} {_bits(value):<26} {_safe_char(char)}")


def _show_str(text: str) -> None:
    """Print char → decimal → bits for every character in *text*.

    Args:
        text: A non-empty string to analyse.

    Raises:
        ValueError: If *text* is empty.
    """
    if not text:
        raise ValueError("Input string must not be empty.")

    print(f"{'Char':<8} {'Decimal':<14} {'Bits'}")
    print(_SEPARATOR)
    for ch in text:
        decimal: int = ord(ch)
        print(f"{_safe_char(ch):<8} {decimal:<14} {_bits(decimal)}")


def convert_text(data: str | int) -> None:
    """Convert a string or integer into its bit, decimal, and character representations.

    String input
    ------------
    Each character is broken down into:
      - the character itself
      - its decimal code-point (``ord(ch)``)
      - its binary representation padded to the nearest full byte

    Integer input
    -------------
    The number is treated as a Unicode code-point and shown alongside:
      - its binary representation padded to the nearest full byte
      - the corresponding Unicode character (``chr(value)``)

    Args:
        data: A ``str`` or a non-negative ``int``.
            * ``str``  — must not be empty.
            * ``int``  — must be in the Unicode range 0–1,114,111.

    Raises:
        TypeError:  If *data* is neither ``str`` nor ``int``.
        ValueError: If *data* is an empty string or an out-of-range integer.

    Examples:
        >>> convert_text("Hi")
        Char     Decimal        Bits
        ----------------------------------------
        H        72             01001000
        i        105            01101001

        >>> convert_text(72)
        Decimal        Bits                       Character
        ----------------------------------------
        72             01001000                   H
    """
    if not isinstance(data, (str, int)):
        raise TypeError(
            f"Expected str or int, got {type(data).__name__!r}. "
            "Pass a string like convert_text('hello') or an integer like convert_text(72)."
        )

    if isinstance(data, int):
        _show_int(data)
    else:
        _show_str(data)


# ---------------------------------------------------------------------------
# Demo – runs only when the script is executed directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== String: 'Hello' ===")
    convert_text("Hello, World!")

    print()
    print("=== Integer: 72 ===")
    convert_text(72)

    print()
    print("=== String: 'Hi \\U0001f40d' (multi-byte Unicode) ===")
    convert_text("Hi \U0001f40d")

    print()
    print("=== Error handling demo ===")
    for bad in ([], 1.5, -1, 1_200_000, ""):
        try:
            convert_text(bad)  # type: ignore[arg-type]
        except (TypeError, ValueError) as exc:
            print(f"  {type(exc).__name__}: {exc}")
