# Task 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close.
# Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output
from task7_5 import check_number, NumberLessThanThree, DivisibleByTwo


# Является ли число простым
def prime_number(number):
    n = 0
    for i in range(1, number + 1):
        if number % i == 0:
            n += 1
        if n > 2:
            return False

    return True


# Если число четное то проверяем гипотезу Голдбраха
def goldbach(number):
    try:
        number = int(number)
        check_number(number)
    except (ValueError, NumberLessThanThree):
        ...
    except DivisibleByTwo:
        for el in range(number//2, number):
            if prime_number(el) and prime_number(number - el):
                return [el, number - el]


if __name__ == '__main__':
    while True:
        n = input("enter your number: \n")
        if n == "q":
            break
        print(goldbach(n))
