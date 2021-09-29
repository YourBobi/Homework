# Task 7.7
# Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
# It should NOT inherit any other collections. If user tries to add a string or any non numerical object there,
# exception `TypeError` should be raised. Method init sholud be able to take either `start,end,step` arguments,
# where `start` - first number of collection, `end` - last number of collection or some ordered iterable
# collection (see the example).
# Implement following functionality:
# * appending new element to the end of collection
# * concatenating collections together using `+`
# * when element is addressed by index(using `[]`), user should get square of the addressed element.
# * when iterated using cycle `for`, elements should be given normally
# * user should be able to print whole collection as if it was list.

# здесь не наследуются никакие коллекции
class MyNumberCollection:

    def __init__(self, start, end=0, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.collection = []
        self.build_collection()

    def build_collection(self):
        if isinstance(self.start, (list, set, tuple)):
            for el in self.start:
                if not isinstance(el, (float, int)):
                    raise TypeError(f"{el} - object is not a number!")
            self.collection = list(self.start)
        else:
            for i in range(self.start, self.end, self.step):
                self.collection.append(i)
            # В цикле всегда не берется self.end
            self.collection.append(self.end)

    def append(self, el):
        if not isinstance(el, (float, int)):
            raise TypeError(f"{el} - object is not a number!")
        self.collection.append(el)

    def __add__(self, other):
        return self.collection + other.collection

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.collection):
            x = self.collection[self.i]
            self.i += 1
            return x
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.collection[item] ** 2

    def __repr__(self):
        return str(self.collection)


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    col1.append(7)
    print(col1)

    print(col1 + col2)

    print(col2[4])
    for item in col1:
        print(item)
