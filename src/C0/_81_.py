# stacks and queues baybeee
# queues are fifo
# stack are first in last out like pancakes
import collections


def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())


# implement a stack with max API
class Stack:
    # my ADT
    cacheElementMax = collections.namedtuple("cacheElementMax",('element', 'max'))

    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def max(self):
        if self.empty():
            raise IndexError
        return self.stack[-1].max

    def pop(self):
        if self.empty():
            raise IndexError
        return self.stack.pop().element

    def push(self, x):
        self.append(self.cacheElementMax(x, x if self.empty() else max(x, self.max())))


