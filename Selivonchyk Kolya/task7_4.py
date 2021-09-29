# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.


def suppressing_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(TypeError)
        except ValueError:
            print(ValueError)
        except RuntimeError:
            print(RuntimeError)
        except:
            print("Some exception")

    return wrapper


@suppressing_exceptions
def main():
    print(edfg)


