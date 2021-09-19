# Task 4.8
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
# Pairs should be formed as in the example. If there is only one element in the list return None instead. Example:
#
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
#
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
#
# >>> get_pairs([1])
# None


def main():
    ls = ['need', 'to', 'sleep', 'more']
    print(get_pairs(ls))


def get_pairs(ls):
    # do with recursion
    if len(ls) < 2:
        return None

    if len(ls) > 2:
        ls = [(ls[0], ls[1])] + get_pairs(ls[1:])
    else:
        ls.append((ls.pop(0), ls.pop(0)))
    return ls


if __name__ == '__main__':
    main()
