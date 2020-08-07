# Binary Search Trees
# BSTs area a workhouse of data structures and can be used to solve
# almost every data structures problem reasonably efficiently

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# Boot camp
# Binary Search trees boot camp
def search_bst(tree, key):
    return (tree if not tree or tree.data == key
            else search_bst(tree.left, key)
    if key < tree.data
    else search_bst(tree.right, key)
            )


# multi ternary: return 1 if A else 2 if B else 3
# def myexpr(A, B):
#     if A:
#         return 1
#     else:
#         if B:
#             return 2
#         else:
#             return 3


# test if a binary tree is a bst
# requisite: root's key is greater than all of the left subtree and less than all of the right subtree
# for a bst of [l,u] range is [-inf,inf]
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return False
    if not low_range <= tree.data <= high_range:
        return False
    return is_binary_tree_bst(tree.left, low_range, tree.data) and is_binary_tree_bst(tree.right, tree.data, high_range)


# ^ truly beautiful recursive solution

# do the queueing solution!
# coming right up
# deque is initialized left to right, two pointer queue
def is_binary_tree_bst(tree):
    import collections
    QueueEntry = collections.namedTuple('QueueEntry', ('node', 'lower', 'upper'))  # base form of data

    bfs_queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])  # queues the starting range

    while bfs_queue:
        front = bfs_queue.popleft()  # takes element of the top of the queue(not from the bottom as expected) overall still normal queue operation
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]  # understand the value the queue brings
    return True
