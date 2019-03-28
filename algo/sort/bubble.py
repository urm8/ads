from algo.search.common import get_random_list


def sort(lst):
    for i, one in enumerate(lst):
        for j, other in enumerate(lst[i:], start=i):
            if one > other:
                lst[i], lst[j], one, other = (other, one) * 2

    return lst


if __name__ == '__main__':
    lst = get_random_list(0, 100, 10)
    print(lst)
    print(sort(lst))
