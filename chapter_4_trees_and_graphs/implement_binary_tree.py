# create tress class

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)




