from algo.search.common import test_it

def get_pos(lo, hi, val, l_hi, l_lo):
    return lo + int(((float(hi - lo) /
                     (l_hi - l_lo) * (val - l_lo))))

def find(lst, val, lo=0, hi=0):
    if not lo:
        lo = 0
    if not hi:
        hi = len(lst) - 1

    while (hi - lo) > 1:
        pos = get_pos(lo, hi, val, lst[hi], lst[lo])
        at_pos = lst[pos]
        if val == at_pos:
            return pos
        if val > at_pos:
            lo = pos + 1
        else:
            hi = pos - 1
    if lst[hi] == val:
        return hi
    elif lst[lo] == val:
        return lo
    else:
        return -1


if __name__ == '__main__':
    test_it(find)
