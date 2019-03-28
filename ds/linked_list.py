from builtins import ValueError


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __eq__(self, other) -> bool:
        return self.data == other.data

    def __str__(self) -> str:
        return f'{{{self.data}}}'

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def append(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value, prev=self.tail)
            self.tail = self.tail.next

    def pop(self):
        if not (self.tail or self.head):
            raise AttributeError()
        elif self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def __iter__(self):
        cur_pos = self.head
        while cur_pos:
            yield cur_pos
            cur_pos = cur_pos.next

    def __str__(self):
        return ' => '.join(str(node) for node in self)

    def __bool__(self):
        return self.head is not Node
