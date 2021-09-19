# Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary,
# where the key is a number and the value is the square of that number.
#
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def main():
    number = 5
    print(generate_squares(number))


def generate_squares(number):
    result = {}
    i = 1

    while i <= number:
        result[i] = i**2
        i += 1

    return result


if __name__ == '__main__':
    main()
