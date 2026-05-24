import pathlib
from pathlib import Path

"""Python Basics: File System Operations

Along the way, you'll also learn about:

· Files
. The file system
. Differences between Windows and UNIX systems
. Absolute and relative paths
· Glob patterns
. Recursive matching
. The shutil module

Table of Contents:

. Creating Directories and Subdirectories
. Creating Files
. Iterating Over Directory Contents
. Searching for Files Using .glob()
. Understanding Common Wildcard Characters: *, ? , and [ ]
. Searching Recursively
. Moving Files and Directories
. Deleting Files and Directories
"""

"""The Anatomy of a File:

It is introduced in 3.4 with PEP428. It provide OOP way of interacting with file paths. As a programmer, we see a file as they all consist of a sequence of bits(8): 01001000, read from right to left. and that's binary number. when we convert it into the decimal number, we get 72. and when we convert it into the ASCII character, we get 'H'. because files use ASCII or UTF-8 encoding.

File paths are different on different operating systems:
. macOS: /Users/martin/Documents/hello.txt
. Ubuntu Linux: /home/martin/Documents/hello.txt
. Windows: C:\\Users\\martin\\Documents\\hello.txt
"""
# we create Path object with it

# from string ("/Users/martin/Documents/hello.txt")
my_path_obj: Path = pathlib.Path(r"C:\\Users\\martin\\Documents\\hello.txt")
print(my_path_obj)
# if we do use /, pathlib library automatically converts it to the \

# form Path.home() and Path.cwd() class methods
print(pathlib.Path.home())  # prints home directory path
print(pathlib.Path.cwd())
# prints full path to current directory.
# Path.cwd() is a dynamic reference to a directory where a process on the
# computer is currently working

# with the / operator
print(Path.home().joinpath("Documents").joinpath("Projects/hello.txt"))
# we edit joinpath() with / for simplicity and recommended
print(Path.home() / "Documents" / "Projects" / "file.txt")
print(Path.home() / "Documents" / "Projects/file.txt")
# we can create as mush as we want, because it user generated
# Path will not check this path, if you wanna check, do this:
user_path: Path = Path.home() / "Documents" / "Projects" / "file.txt"
print(user_path.exists())
user_path: Path = Path.home() / "Documents"
print(user_path.exists())

# creating new directory
current_path: Path = Path.cwd() / "demo_dir"
try:
    current_path.mkdir()
except FileExistsError:
    print(f"directory already exists: {current_path.name}")

# removing directory
# current_path: Path = Path.cwd() / "demo_dir"
# try:
#     current_path.rmdir()
# except FileNotFoundError:
#     print(f'File not found: "{current_path.name}"')
