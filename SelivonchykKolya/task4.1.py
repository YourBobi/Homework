# Task 4.1
# Implement a function which receives a string and replaces all " symbols with ' and vise versa.


def main():
    s = "\' hh gg \""
    s = reformat_string(s)
    print(s)


def reformat_string(s):
    # we do new string because you cannot replace a specific element in a string
    s2 = ''
    for el in s:
        if el == "\'":
            s2 += "\""
        elif el == "\"":
            s2 += "\'"
        else:
            s2 += el
    return s2


if __name__ == '__main__':
    main()
