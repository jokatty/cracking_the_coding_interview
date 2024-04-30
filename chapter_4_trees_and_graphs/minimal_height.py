# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

# sol: To create a tree of minimal height, we need to match the number of nodes in the
# left subtree to the number of nodes in the right subtree as much as possible.
# This means that we want the root to be the middle of the array,
# since this would mean that half the elements would be less than the root and half would be greater than it.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_minimal_tree(array):
    return array_to_bst(array, 0, len(array)-1)


def array_to_bst(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = array_to_bst(arr, start, mid - 1)
    root.right = array_to_bst(arr, mid + 1, end)
    return root


nums = [1, 2, 3, 4, 5]

print(create_minimal_tree(nums))
