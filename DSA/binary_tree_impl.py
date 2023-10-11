from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.value, end=' ')
            self._inorder_recursive(root.right)

# Usage example:
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert elements into the binary tree
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    # Inorder traversal
    print("Inorder Traversal:")
    tree.inorder_traversal()
    print()

    # Search for an element
    key = 40
    result = tree.search(key)
    if result:
        print(f"{key} found in the tree.")
    else:
        print(f"{key} not found in the tree.")