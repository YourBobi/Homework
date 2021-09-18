# ### Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```


def main():
    number = int(input("Enter your number: "))
    print(all_divisors(number))


def all_divisors(number):
    ls = []
    x = 1

    while x <= number:
        if number % x == 0:
            ls.append(x)
        x += 1

    return ls


if __name__ == '__main__':
    main()
