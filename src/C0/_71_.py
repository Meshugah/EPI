# linked lists baybee
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Linked lists bootcamp
# Implement:
# Search
# Insert
# Delete


def search_list(key, L):
    while L and L.data != key:
        L = L.next  # skrt through that list
    return L


def insert_node(node, new_node):
    # new_node, next gets the node's next node
    new_node.next = node.next
    # all of new_node belongs to us of node.next
    node.next = new_node

    # deletes the node past this one.


def delete_node(node):
    node.next = node.next.next


def merge_sorted_lists(L1, L2):
    # tail
    #  data
    #  next = L1
    # head
    #  data
    #  next
    # L1
    #  becomes the next node
    # l1 and l2, don't just represent themselves
    # by saying L1, you're asking it any of it's node exist

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next

# try running it with an example L1 = odd list, L2 = even list

