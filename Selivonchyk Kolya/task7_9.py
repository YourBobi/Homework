# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments
# and gives only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
# _Note: Do not use function `range()` at all_


class EvenRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = True

    def checker(self):
        if not isinstance((self.start, self.end), int):
            raise TypeError("not int")

    def __iter__(self):
        self.next = False
        return self

    def __next__(self):
        if self.start % 2 != 0:
            self.start += 1
        if self.start <= self.end and self.start % 2 == 0:
            x = self.start
            self.start += 2
            return x
        if self.next:
            return "Out of numbers!"

        print("Out of numbers!")
        raise StopIteration()


er2 = EvenRange(3, 14)
for number in er2:
    print(number)