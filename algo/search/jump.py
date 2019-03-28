import math

from algo.search import test_it


def find(lst, val, jump=None):
    if lst[0] == val:
        return 0
    len_list = len(lst)
    if not jump:
        jump = int(math.sqrt(len_list))

    hi = 0
    while hi + jump < len_list and val > lst[hi]:
        hi += jump

    if hi + jump >= len_list:
        hi = len_list - 1
    for idx in range(hi, -1, -1):
        if lst[idx] == val:
            return idx
    return -1

if __name__ == '__main__':
    test_it(find)



