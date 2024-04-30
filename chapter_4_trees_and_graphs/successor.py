# define tree node class

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# method to traverse the leftmost node
def find_left_most(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node


def find_successor(n):
    if not n:
        return None
    # in inorder traversal the successor of node n will be the left most child of the left tree
    if n.right is not None:
        return find_left_most(n.right)
    else:
        q = n
        x = q.parent
        # go up until we are on left instead of right
        while x is not None and x.left != q:
            q = x
            x = x.parent
        return x





