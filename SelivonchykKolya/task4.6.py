# Task 4.6
# Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
# The word can contain any symbols except whitespaces ( , \n, \t and so on).
# If there are multiple longest words in the string with a same length return the word that occures first. Example:
#
# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'
#
# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
import re


def main():
    s = 'Python is simple, and-effective!?'
    print(get_longest_word(s))


def get_longest_word(s):
    # вообщем, для слов через дефиз я проверки не делал, из-за того, что они не всегда являются одним словом.
    # Например: инженер-программист (два слова), где-то (одно)
    ls = re.split(r"[\W]+", s)  # получаем слова без пунктуации
    longest_word = ls[0]

    for el in ls:
        if len(el) > len(longest_word):
            longest_word = el

    return longest_word


if __name__ == '__main__':
    main()
