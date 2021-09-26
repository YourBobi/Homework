# Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A,
# B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
# excluding those already used in the key.
import string


class Cipher:

    def __init__(self, word=''):
        Cipher.check_word(word)  # Проверяем, есть ли в строке повторяющиеся буквы, или символы
        self.normal_ABC = string.ascii_letters
        self.cipher_ABC = ''
        self.__make_cipher_ABC(word)

    # Проверка на повтор букв и символы
    @staticmethod
    def check_word(word):
        for i in range(len(word)):
            if word[i] in word[0:i] + word[-i:i:-1]:
                raise RuntimeError("There are 2 or more repeated letters in a line")
            elif not word[i].isalpha():
                raise RuntimeError("Incorrect word")

    # создаём зашифрованный словарь
    def __make_cipher_ABC(self, word=''):
        self.cipher_ABC += word.lower()
        for el in string.ascii_lowercase:  # буквы в нижнем регистре
            if el not in word.lower():
                self.cipher_ABC += el

        self.cipher_ABC += word.upper()
        for el in string.ascii_uppercase:  # буквы в верхнем регистре
            if el not in word.upper():
                self.cipher_ABC += el

    def encode(self, word):
        code_word = ''
        for el in word:
            code_word += self.cipher_ABC[self.normal_ABC.index(el)] if el in self.normal_ABC else el

        print(code_word)
        return code_word

    def decode(self, word):
        decode_word = ''
        for el in word:
            decode_word += self.normal_ABC[self.cipher_ABC.index(el)] if el in self.cipher_ABC else el

        print(decode_word)
        return decode_word


a = Cipher("crypto")
a.encode("Hello world")
a.decode("Fjedhc dn atidsn")
