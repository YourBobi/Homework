# ### Task 1.4
# Write a Python program to sort a dictionary by key.


def main():
    dct = {1: "dd", 2: "pp", "f": 1, -1: "jkl"}
    dct = {key: value for key, value in sorted(dct.items(), key=unique)}
    print(dct)


def unique(el):
    return ord(str(el[0])[0])  # конструкция el[0] берёт ключ, а str(el[0])[0] конвертит в str и берёт 0 элемент


if __name__ == '__main__':
    main()
