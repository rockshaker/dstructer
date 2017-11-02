class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.right = self.right
            self.right = temp

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_root(self):
        return self.root

    def set_root(self, val):
        self.root = val
