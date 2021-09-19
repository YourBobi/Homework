# Task 4.5
# Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits. Example:
#
# >>> get_digits(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


def main():
    print(get_digits(451234589))


def get_digits(number):
    tpl = tuple(int(el) for el in str(number))
    return tpl


if __name__ == '__main__':
    main()
