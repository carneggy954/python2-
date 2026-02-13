class Node:
    """
    Represents a single node in the Binary Search Tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation with insert and search methods.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """
        Helper method to insert recursively.
        """
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            # Value already exists in BST (no duplicates allowed)
            pass

    def search(self, value):
        """
        Searches for a value in the BST.
        Returns True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        """
        Helper method to search recursively.
        """
        if current_node is None:
            return False

        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)


# -------------------------
# Test Cases
# -------------------------

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert values
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for value in values_to_insert:
        bst.insert(value)

    # Test search (existing values)
    print("Searching for 50:", bst.search(50))  # True
    print("Searching for 30:", bst.search(30))  # True
    print("Searching for 80:", bst.search(80))  # True

    # Test search (non-existing values)
    print("Searching for 25:", bst.search(25))  # False
    print("Searching for 90:", bst.search(90))  # False

    # Edge case: empty tree
    empty_bst = BinarySearchTree()
    print("Searching in empty tree:", empty_bst.search(10))  # False
