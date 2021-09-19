# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
#
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
import string


def main():
    ls = ["hello", "world", "python", ]
    print(test_1_4(*ls))


def test_1_1(*ls):
    result = set()

    for i in string.ascii_lowercase:
        number = 0
        for el in ls:
            if i in el.lower():
                number += 1
        if number == len(ls):
            result.add(i)

    return result


def test_1_2(*ls):
    result = set()

    for i in string.ascii_lowercase:
        for el in ls:
            if i in el.lower() and i not in result:
                result.add(i)

    return result


def test_1_3(*ls):
    result = set()

    for i in string.ascii_lowercase:
        number = 0
        for el in ls:
            if i in el.lower():
                number += 1
        if number >= 2:
            result.add(i)

    return result


def test_1_4(*ls):
    result = set()

    for i in string.ascii_lowercase:
        number = 0
        for el in ls:
            if i in el.lower():
                number += 1
        if number == 0:
            result.add(i)

    return result


if __name__ == '__main__':
    main()