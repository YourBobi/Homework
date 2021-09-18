# ### Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```


def main():
    tpl = (1, 2, 3, 4)
    print(converting_tuple(tpl))


def converting_tuple(tpl):
    number = 0
    degree = len(tpl) - 1
    for i in range(len(tpl)):
        number += tpl[i] * 10**degree
        degree -= 1

    return number


if __name__ == '__main__':
    main()
