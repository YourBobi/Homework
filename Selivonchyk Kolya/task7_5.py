# Task 7.5
# Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).


class PersonalException(Exception):
    ...


class DivisibleByTwo(PersonalException):
    def __init__(self, *args):
        if args:
            self.text = args[0]
        else:
            self.text = "number % 2 == 0"

    def __str__(self):
        return "{0}".format(self.text)


class NumberLessThanThree(PersonalException):
    def __init__(self, *args):
        if args:
            self.text = args[0]
        else:
            self.text = "number less than 2"

    def __str__(self):
        return "{0}".format(self.text)


def check_number(number):
    if number < 3:
        raise NumberLessThanThree
    elif number % 2 == 0:
        raise DivisibleByTwo
