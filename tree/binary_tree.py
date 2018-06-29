"""
    https://github.com/raywenderlich/swift-algorithm-club/tree/master/Binary%20Tree
    it is the tutorial that must read
"""


class Node(object):
    def __init__(self, value=None):
        self._value = value
        self._parent = None
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @left.setter
    def left(self, new_left):
        self._left = new_left

    @right.setter
    def right(self, new_right):
        self._right = new_right


class BinaryTree(object):
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, value):
        if self.root is None:
            self._root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._insert(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value > node.value and node.right is not None:
            self._find(value, node.right)
        elif value < node.value and node.left is not None:
            self._find(value, node.left)
        else:
            print('cannot find the node')

    def delete_tree(self):
        if self.root is not None:
            self.right = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print('{0} '.format(node.value))
            self._print_tree(node.right)


if __name__ == '__main__':
    tree = BinaryTree()

    tree.insert(1)
    tree.insert(20)
    tree.insert(19)
    tree.insert(5)
    tree.insert(-4)

    tree.print_tree()

    print(tree.find(-4))
    print(tree.find(99))

    tree.delete_tree()
