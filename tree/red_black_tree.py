"""

A red-black tree (RBT) is a balanced version of a Binary Search Tree
guaranteeing that the basic operations.
(search, predecessor, successor, minimum, maximum, insert and delete)
have a logarithmic worst case performance.

Binary search trees (BSTs) have the disadvantage that they can become
unbalanced after some insert or delete operations.

"""


class Color(object):
    def __init__(self):
        self._red = 'red'
        self._black = 'black'

    @classmethod
    def RED(self):
        return self._red

    @classmethod
    def BLACK(self):
        return self._black


class Node(object):
    def __init__(self, value):
        self._color = Color.RED
        self._value = value
        self._parent = None
        self._left = None
        self._right = None

    def __str__(self):
        return 'color: {0}; value: {1}'.format(self._color, self._value)

    @property
    def color(self):
        return self._color

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

    @color.setter
    def color(self, new_color):
        self._color = new_color

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


class RedBlackTree(object):
    def __init__(self):
        self._root = None
        self._left_tree = None
        self._right_tree = None

    @property
    def root(self):
        return self._root

    @property
    def left_tree(self):
        return self._left_tree

    @property
    def right_tree(self):
        return self._right_tree

    @root.setter
    def root(self, new_root):
        self._root = new_root

    @left_tree.setter
    def left_tree(self, new_left_tree):
        self._left_tree = new_left_tree

    @right_tree.setter
    def right_tree(self, new_right_tree):
        self._right_tree = new_right_tree

    def insert(self, value):
        if self.root is None:
            # 1) insert root
            self.root = Node(value)
            self.root.color = Color.BLACK


if __name__ == '__main__':
    n = Node(5)

    print(n)
