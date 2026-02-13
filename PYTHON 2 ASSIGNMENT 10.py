class Node:
    """
    Represents a node in the Binary Tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Basic Binary Tree implementation with insertion
    and traversal methods (in-order, pre-order, post-order).
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a node into the binary tree using level-order insertion.
        """
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        # Use a queue for level-order traversal
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # -----------------------
    # Traversal Methods
    # -----------------------

    def ino

