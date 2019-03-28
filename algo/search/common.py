import random

import numpy as np
import time

np.random.seed(int(time.time()))
np.set_printoptions(precision=0)


def get_random_list(lo, hi, size):
    return list(np.random.randint(lo, hi, size, dtype=np.uint8))


def get_sorted_list(lo, hi, size):
    return np.sort(get_random_list(lo, hi, size)).tolist()

def get_random_int(lo, hi):
    return get_random_list(lo, hi, 1)[0]

lo = 1
hi = 10

def test_it(function):
    i = 0
    for i in range(10001):
        lst_size = random.randint(2000, 10000)
        lst = get_random_list(0, 100, lst_size)
        lst = list(sorted(set(lst)))
        actual = random.randint(0, len(lst) - 1)
        val = lst[actual]
        found = function(lst, val)
        assert actual == found, "Test case #%d failed: found - %s, " \
                                "while actual - " \
                                "%s\nValue: %s\nList: %s" % (i + 1, found,
                                                             actual, val, lst)
    print(f'All {i} test cases passed')
