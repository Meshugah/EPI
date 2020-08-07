import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Boot camp: Tree traversal


def tree_traversal(root):
    if root:
        # Pre-Order
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)
        tree_traversal(root.right)


def is_balanced_binary_tree(tree):
    # ADT
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    # return if the tree is balanced first, then height of the tree
    def check_balanced(tree):
        # break condition 1
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # if it's empty, return it is a balanced tree with height -1

        # recursive step
        left_result = check_balanced(tree.left)
        # break condition 2
        if not left_result.balanced:
            # Left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        # recursive step
        right_result = check_balanced(tree.right)
        # break condition 3
        if not right_result.balanced:
            # right subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        # iterative operations
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
