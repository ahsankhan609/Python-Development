# File Handling in Python

## Course Resources:-

- [File Handling in Python - Code-Yug](https://www.youtube.com/playlist?list=PLI4OVrCFuY55ZrOMkfYNt7CQGEkskxJlj)📚 Mar 15, 2021
- [File Handling Exercise - Code-Yug](https://www.youtube.com/playlist?list=PLI4OVrCFuY55obuW8Sp7b-3_KgtpgURYp)📚
- [Working with Files - GitHub (teclado)](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/6_files)
- [Day 14: Working with Files - teclado Article](https://teclado.com/30-days-of-python/python-30-day-14-files/)
- [Working with Files in Python - Visually Explained](https://www.youtube.com/playlist?list=PL8HmoRTjTSlETCd57NyDEmtTBim6DG1JZ) 📚

## Course Notes:-

- File handling is a crucial aspect of programming that allows us to read from and write to files on our computer.
- In Python, we can use the built-in `open()` function to work with files. The `open()` function takes two arguments: the file name and the mode in which we want to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
- When we open a file, we get a file object that we can use to perform various operations on the file, such as reading its contents, writing to it, or closing it when we're done.
- It's important to close the file after we're done with it to free up system resources. We can use the `close()` method to close the file, or we can use a `with` statement to automatically close the file when we're done.
- To read the contents of a file, we can use the `read()` method, which reads the entire contents of the file as a string.
- We can also use the `readline()` method to read one line at a time, or the `readlines()` method to read all lines into a list.
- When writing to a file, we can use the `write()` method to write a string to the file, or the `writelines()` method to write a list of strings to the file.
- When working with files, it's important to handle exceptions that may occur, such as `FileNotFoundError` when trying to open a file that doesn't exist, or `OSError` when there are issues with reading or writing to the file.
- So, We should use try-except blocks to catch these exceptions and handle them gracefully in our code.
- For smaller applications use **file_handling**, but for larger applications, it's better to use a **database** to store and manage data efficiently.

#### File-Handling :-

- **What is file handling?**
  - open a file - performing some operations on it
  - close the file
- **What is a file?**
  - Files are named locations on disk to store information.
  - They are used to store data permanently.
  - Data stored in files are non-volatile memory
  - we can retrieve data whenever required
- **Types of files**
  - Text Files
    - store data in the form of characters. it is used to store data and strings.
  - Binary Files
    - store data in the form of bytes(group of 8 bits). it is used to store images, videos, pdf, audio files, etc.

```python
# it provides a file handler(f), which is used to perform operations,
# by using file object functions.
# f(obj) - refers to the beginning of the file.
# file name and file mode should be string
# read only mode - 'r' - it is default value of mode
f = open(filename, mode='r', buffering, encoding=None,
errors=None, newline=None, closefd=True)
```
