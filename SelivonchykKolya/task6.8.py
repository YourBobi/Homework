# Task 4.8
#
# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
# (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that
# accepts the page number and return quantity of symbols on this page. If the provided number of the page
# is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.
from numbers import Number


class Pagination:

    def __init__(self, text, number_of_symbols):
        if isinstance(text, str) and isinstance(number_of_symbols, Number):
            self.pages = []
            self.__filling_the_array__(text, number_of_symbols)
        else:
            raise TypeError("Function expects text and int")

    def __filling_the_array__(self, text, n):
        string = ''
        for el in text:
            if len(string) == n:
                self.pages.append(string)
                string = ''
            string += el
        if string:
            self.pages.append(string)

    def page_count(self):
        return len(self.pages)

    def item_count(self):
        return sum(len(el) for el in self.pages)

    def count_items_on_page(self, page=0):
        if page > self.page_count() - 1:
            raise Exception("Invalid index. Page is missing.")
        return len(self.pages[page])


pages = Pagination('Your beautiful text', 5)
print(pages.count_items_on_page(4))
