# Task 7.2
# Implement context manager for opening and working with file, including handling exceptions
# with @contextmanager decorator.
from contextlib import contextmanager, suppress


@contextmanager
def my_context_manager(filename, mode):
    f = 0  # Чтобы не выбило ошибку в finally
    try:
        f = open(filename, mode)
        yield f
    except FileNotFoundError:
        print("FileNotFoundError")
    except IOError:
        print("File error")
    finally:
        if f:
            print('Closing file')
            f.close()


if __name__ == '__main__':
    with suppress(RuntimeError):
        with my_context_manager("../README.md", "r") as m:
            my_file = m.read()
            print(my_file)
