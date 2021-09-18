# ### Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# ```


def main():
    s = input("Enter your string:\n")
    print(number_of_characters(s))


def number_of_characters(s):
    dct = {}
    for el in s:
        if el in dct:
            continue
        elif el.isalpha():
            dct[el.lower()] = 2
        elif el.isspace():
            dct[el] = 3
        elif el.isdigit():
            dct[el] = 4
        else:
            dct[el] = 1

    return dct


if __name__ == '__main__':
    main()
