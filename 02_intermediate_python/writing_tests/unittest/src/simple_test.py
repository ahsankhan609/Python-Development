def main() -> None:
    try:
        assert sum([1, 2, 3]) == 6, "Should be 6"
    except AssertionError as e:
        print(
            f"AssertionError: {e}")
    else:
        print("Test passed")


if __name__ == "__main__":
    main()
