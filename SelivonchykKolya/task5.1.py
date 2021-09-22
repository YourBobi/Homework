# ### Task 4.1
# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file
# called `sorted_names.txt`. Each name should start with a new line as in the following example:
#
# ```
# Adele
# Adrienne
# ...
# Willodean
# Xavier
# ```
import functools


def main():
    ls = get_info_from_file(way="../data/unsorted_names.txt")
    create_new_file(way="../data", name="sorted_names.txt", list_values=ls)


def get_info_from_file(*, way):
    f = open(way, 'r')
    ls = [el for el in f]
    f.close()
    return ls


def sorting(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        kwargs.get('list_values').sort()
        return fun(*args, **kwargs)

    return wrapper


@sorting
def create_new_file(*, way, name, list_values):
    f = open(way + "/" + name, 'w')
    for el in list_values:
        f.write(el)
    f.close()


if __name__ == '__main__':
    main()
