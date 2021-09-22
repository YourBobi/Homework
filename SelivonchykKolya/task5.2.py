# ### Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.
#
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# ```
# > NOTE: Remember about dots, commas, capital letters etc.
import re


def main():
    print(most_common_words('../data/lorem_ipsum.txt', 4))


def most_common_words(filepath, number_of_words=1):
    ls = []
    with open(filepath, "r") as f:
        dct = {}    # словарь для значений слово:его количество в тексте

        ls = re.findall(r"[\w]+", f.read())
        ls.sort()

        number = 1
        for word in ls:
            if word not in dct:
                number = 1
            dct[word] = number
            number += 1

        # завписываем первые n слов котрые используются чаще
        ls.clear()
        for i in range(number_of_words):
            word = max(dct.items(), key=lambda x: x[1])[0]
            ls.append(word)
            dct.pop(word)

    return ls


if __name__ == '__main__':
    main()