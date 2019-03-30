from algo.search.common import get_random_list


def sort(lst, n=None):
        """
        Recursive bubble sort, no advantages against regular. Just for fun
        """
        if not n:
            n = len(lst)
        if n == 1:
            return
        for idx in range(n - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
        sort(lst, n - 1)


if __name__ == '__main__':
    lst = get_random_list(0, 100, 5)
    print(lst)
    sort(lst)
    print(lst)
