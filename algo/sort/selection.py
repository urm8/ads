from algo.search.common import get_random_list


def sort(lst):
    lst_len = len(lst)
    for ins_pos in range(lst_len):
        min_pos = ins_pos
        for swp_pos, elem in enumerate(lst[ins_pos:], start=ins_pos):
            if elem <= lst[min_pos]:
                min_pos = swp_pos
        lst[ins_pos], lst[min_pos] = lst[min_pos], lst[ins_pos]
    return lst


if __name__ == '__main__':
    lst = get_random_list(0, 100, 10)
    print(lst)
    print(sort(lst))
