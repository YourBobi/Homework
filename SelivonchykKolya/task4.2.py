# Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from here.


def main():
    s = "12321"
    print(palindrome_check(s))


def palindrome_check(s):
    # function that check whether a string is a palindrome or not (implemented with polymorphism)
    if s:
        if s[0] == s[-1]:
            return palindrome_check(s[1:-1])
        else:
            return False
    return True


if __name__ == '__main__':
    main()
