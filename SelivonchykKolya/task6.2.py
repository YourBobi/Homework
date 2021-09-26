# Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.


class HistoryDict:

    def __init__(self, dct={}):
        if not isinstance(dct, dict):
            raise TypeError("Incorrect value. Dictionary expected.")
        self.dct = dct
        self.changed_keys = []

    def set_value(self, key, value):
        self.dct[key] = value
        self.changed_keys.append(key)

    def get_history(self):
        print(self.changed_keys)
        return self.changed_keys

    def __repr__(self):
        return str(self.changed_keys)


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("bar", 4)
d.get_history()

