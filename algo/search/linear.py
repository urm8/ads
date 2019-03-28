from algo.search import test_it


def find(lst, val):
    for pos, elem in enumerate(lst):
        if elem == val:
            return pos
    return -1


if __name__ == '__main__':
    test_it(find)

