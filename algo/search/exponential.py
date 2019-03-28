from algo.search import binary
from algo.search.common import test_it


def find(lst, val):
    if lst[0] == val:
        return 0

    i = 1
    while i < len(lst) and lst[i] <= val:
        i *= 2
    return binary.find(lst, val, i // 2, min(i, len(lst)))


if __name__ == '__main__':
    test_it(find)
