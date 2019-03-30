from algo.search.common import get_random_list


def sort(lst):
    n = len(lst)
    for i in range(1, n):
        val = lst[i]
        j = i - 1
        while j >= 0 and val < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = val


if __name__ == '__main__':
    l = get_random_list(0, 100, 5)
    print(l)
    sort(l)
    print(l)
