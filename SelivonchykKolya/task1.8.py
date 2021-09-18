# ### Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
#
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28
# ```


def main():
    a = 2
    b = 4
    c = 3
    d = 7
    print(pretty_table(a, b, c, d))


def pretty_table(a, b, c, d):
    s = " " + "\t"
    for i in range(c, d + 1):
        s += str(i) + "\t"

    for i in range(a, b + 1):
        s += "\n" + str(i) + "\t"
        for j in range(c, d + 1):
            s += str(i * j) + "\t"

    return s


if __name__ == '__main__':
    main()
