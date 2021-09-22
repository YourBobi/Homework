# ### Task 4.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.
#
# ```python
# @call_once
# def sum_of_numbers(a, b):
#     return a + b
#
# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55
# ```
import functools


def call_once(fun):
    @functools.lru_cache(maxsize=32)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "ones"):
            wrapper.ones = fun(*args, **kwargs)
        return wrapper.ones

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 13))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 13))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 13))
