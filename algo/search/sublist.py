from ds.linked_list import LinkedList


def find(one, other):
    if not one or not other:
        return False
    for el_f, el_s in zip(one, other):
        if el_f != el_s:
            return False
    return True


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(1)
    l1.append(4)
    l1.append(3)
    l2.append(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)

    print(find(l1, l2))
