# Task 7.8
# Implement your custom iterator class called MySquareIterator which gives squares of elements
# of collection it iterates through.
# Example:
# ```python
# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25


class MySquareIterator:

    def __init__(self, ls):
        self.ls = ls
        self.checker()

    def checker(self):
        if not isinstance(self.ls, (list, set, tuple)):
            raise TypeError("error")

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.ls):
            x = self.ls[self.i] ** 2
            self.i += 1
            return x
        else:
            raise StopIteration


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)