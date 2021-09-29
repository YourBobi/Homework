# Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.
from contextlib import suppress


class MyFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.conn = open(self.filename, self.mode)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print("File closed!!")
        if exc_val or exc_type or exc_tb:
            raise


if __name__ == '__main__':
    with suppress(RuntimeError, FileNotFoundError, IOError):
        with MyFile("../README.md", "r") as m:
            my_file = m.read()
            print(my_file)
