# Task 7.3
# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
from time import time
from contextlib import closing


# filename - файл в который записывается результат
def execution_time(filename):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, "w") as write_file:
                start_time = time()
                func(*args, **kwargs)
                write_file.write(str(time() - start_time))  # Подсчет времени выполнения, и запись файл

        return wrapper
    return my_decorator


@execution_time("../time_file.txt")
def main():
    i = 100000000
    while i:
        i -= 1


if __name__ == '__main__':
    main()