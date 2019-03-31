from algo.search import common


def sort(lst):
    try:
        lst[1]
        middle = len(lst) // 2
        lpart = lst[:middle]
        rpart = lst[middle:]
        sort(lpart)
        sort(rpart)
        pos = 0
        while lpart or rpart:
            if not lpart:
                lst[pos] = rpart.pop(0)
            elif not rpart:
                lst[pos] = lpart.pop(0)
            elif lpart[0] < rpart[0]:
                lst[pos] = lpart.pop(0)
            else:
                lst[pos] = rpart.pop(0)
            pos += 1
    except IndexError:
        pass


if __name__ == '__main__':
    l = common.get_random_list(0, 100, 10)
    sort(l)
