### Task 4.5
# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.
#
# ```python
# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result
#
# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"
# ```
result = None


def remember_result(fun):
    def wrapper(*args, **kwargs):
        global result
        print(f"Last result = '{result}'")
        if all(isinstance(i, int) for i in args):  # проверка на int
            args = str(sum(args))
        result = fun(*args, **kwargs)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""

    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result
