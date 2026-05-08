# https://claude.ai/share/a2b5c9f4-ef7c-43ce-887c-4b6361f48c73
def main() -> None:
    """
    Context Manager (with statement) استعمال کرتے ہوئے
    Note:- This code works in Python 3.13+
    """

    file_path: str = "data.txt"

    # Reading - First time
    print("📖 Reading file...")
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
    # with helps to close file automatically

    # Writing - data overwrite
    print("\n✍️  Writing to file...")
    user_input: str = input("Please enter your name: ")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(user_input)
    # file automatically closes

    # Reading - Second Time
    print("\n📖 Reading file (updated)...")
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
    # file automatically closes


if __name__ == "__main__":
    main()
