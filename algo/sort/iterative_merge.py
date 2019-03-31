from algo.sort import merge
from algo.search import common


def sort(lst):
    rb = len(lst)
    lb = 0
    sub_arr_len = 1
    while sub_arr_len < rb:
        lb = 0
        while lb < rb - 1:
            m = lb + sub_arr_len
            r = lb + 2 * sub_arr_len
            if r >= rb:
                r = rb
            merge.merge(lst[lb:m], lst, lst[m:r], lb)
            lb += sub_arr_len * 2
        sub_arr_len *= 2


if __name__ == '__main__':
    l = common.get_random_list(0, 15, 10)
    print(l)
    sort(l)
    print(l)
