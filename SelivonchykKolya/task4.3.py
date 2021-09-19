# Task 4.3
# Implement a function which works the same as str.split method (without using str.split itself, ofcourse).


def main():
    s = "lol,kek, chheburek, ,llll, ddd "
    print(split_2_0(s, ","))


def split_2_0(s, symbol=" ", *, maxsplit=True):
    result = []
    n = 0          # Индекс начала среза
    iteration = 0

    for i in range(len(s)):
        if s[i] is symbol:
            result.append(s[n:i])
            iteration += 1
            n = i + 1
        if maxsplit is iteration:
            break
    if n < len(s):
        result.append(s[n:])

    return result


if __name__ == '__main__':
    main()
