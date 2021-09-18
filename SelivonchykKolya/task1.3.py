# ### Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']
# ```


def main():
    ls = ['red', 'white', 'black', 'red', 'green', 'black']
    ls.sort()
    sorting_by_identity(ls)
    print(ls)


def sorting_by_identity(ls):
    for el in ls:
        if ls.count(el) > 1:
            ls.remove(el)


if __name__ == '__main__':
    main()
