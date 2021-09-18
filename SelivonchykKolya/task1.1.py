# # Python Practice - Session 1
#
# ### Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.


def main():
    s = input("Enter your string:\n")
    print("Length of string = ", length_of_string(s))


def length_of_string(s):
    length = 0
    for el in s:
        length += 1

    return length


if __name__ == '__main__':
    main()
