import os

from pure_eval.utils import ast_name
from test.test_monitoring import just_pass

# show current OS
print(f"Current OS: {os.name}")

# show OS separator symbol.
# its benefit is to write OS independent path.
print(f"OS Separator: {os.sep}")

# this create a new folder in the current directory
try:
    os.mkdir("new_folder")
except FileExistsError as fe:
    print(fe)

# this create parent/child new folder(s) in the current directory
# if exists, it will raise FileExistsError
try:
    os.makedirs("parent_folder/sub_folder")
except FileExistsError as fe:
    print(fe)

# this function return full path to the current working directory
print(f"Current Working Directory full Path: {os.getcwd()}")

# this function return name of the current working directory
print(f"Current Working Directory Name: {os.path.basename(os.getcwd())}")

# return stats of the file
print(f"File Stats: {os.stat('notes.txt')}")

# create a simple txt file in folder
current_folder: str = os.getcwd()
new_folder_path: str = os.path.join(current_folder, "new_folder")
file_name: str = os.path.join(new_folder_path, "sample_file.txt")

with open(file_name, "a") as f:
    f.write("\nanother some random text")

# create new folder in the current directory, if already exists, ok.
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")

# rename file, cut and paste to new directory
try:
    os.rename("new_folder/sample_file.txt", "my_folder/sample_file.md")
except FileExistsError as fe:
    print(f"File already exists:{fe}")

# rmdir() only remove particular directory - if empty
# rmdirs() remove tree of all directories and subdirectories.
try:
    os.removedirs("parent_folder/sub_folder")
except OSError as oe:
    print(f"Directory is not empty: {oe}")
