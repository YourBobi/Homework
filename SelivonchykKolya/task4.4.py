# Task 4.4
# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string
# by indexes specified in indexes. Wrong indexes must be ignored. Examples:

# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]


def main():
    ls = [6, 8, 12, 13, 18]
    s = "pythoniscool,isn'tit?"
    split_by_index(s, ls)
    print(ls)


def split_by_index(s, ls=[]):
    word = ""
    ls2 = []

    for i in range(len(s)):
        if i in ls:
            ls2.append(word)
            word = ""
        word += s[i]

    if word:
        ls2.append(word)

    ls.clear()
    ls.extend(ls2)


if __name__ == '__main__':
    main()
