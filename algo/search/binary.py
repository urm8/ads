from algo.search import test_it


def find(lst, val, lo=None, hi=None):
    if not lo:
        lo = 0
    if not hi:
        hi = len(lst)
    idx = hi // 2
    while lst[idx] != val and (lo - hi) not in (0, -1, 1):
        if lst[idx] > val:
            hi = idx
        else:
            lo = idx
        idx = (hi + lo) // 2
    if lst[idx] == val:
        return idx
    return -1


if __name__ == '__main__':
    test_it(find)
