"""
    A binary search tree is a special kind of binary tree
    (a tree in which each node has at most two children)
    that performs insertions and deletions such that the tree is always sorted.
    For more information about a tree, read
    https://github.com/raywenderlich/swift-algorithm-club/tree/master/Tree.
"""

class Node:
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
    @property
    def height(self):
        if self.is_leaf():
            return 0
        else:
            left_h = 0
            right_h = 0
            if self.left:
                left_h = self.left.height
            if self.right:
                right_h = self.right.height
            return 1 + max(left_h, right_h)

    @value.setter
    def value(self, new_value):
        self._value = new_value
    @parent.setter
    def parent(self, new_value):
        self._parent = new_value
    @left.setter
    def left(self, new_value):
        self._left = new_value
    @right.setter
    def right(self, new_value):
        self._right = new_value
    def is_root(self):
        return self._parent == None

    def is_leaf(self):
        return self._left == None and self._right == None

    def is_left_child(self):
        if self.parent is not None:
            return self._parent._left == self

    def is_right_child(self):
        if self.parent is not None:
            return self._parent._left == self

    def has_left_child(self):
        return self._left != None

    def has_right_child(self):
        return self._left != None

    def has_any_child(self):
        return self.has_left_child() or self.has_right_child()

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()


class Binary_Search_Tree:
    def __init__(self):
        self._root = None

    def __str__(self):
        self.postorder()

    @property
    def root(self):
        return self._root

    def insert(self, new_value):
        if self._root == None:
            self._root = Node(new_value)
        else:
            current = self._root
            while True:
                if new_value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(new_value)
                        current.left.parent = current
                        break
                elif new_value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(new_value)
                        current.right.parent = current
                        break
                else:
                    break

    def find_min(self, node):
        while True:
            if node.left is None:
                return node
            else:
                node = node.left

    def find_max(self, node):
        while True:
            if node.right is None:
                return node
            else:
                node = node.right

    def remove(self, key):
        if self.search(key) is not None:
            current = self._root
            while True:
                # if value is less than node, search left
                if key < current.value:
                    current = current.left
                elif key > current.value:
                    current = current.right
                else:
                    # find the node that we want
                    # if node is leaf
                    if current.is_leaf():
                        current = None
                        break
                    # if only one child
                    elif current.left is None:
                        max = self.find_max(current.right)
                        max.parent.right = None
                        if current.parent:
                            if current.is_left_child():
                                current.parent.left = max
                            else:
                                current.parent.right = max
                            max.parent = current.parent
                        else:
                            self._root = max

                        max.right = current.right
                        if max.right:
                            max.right.parent = max
                        current = None
                        break
                    else:
                        min = self.find_min(current.left)
                        min.parent.left = None
                        if current.parent:
                            if current.is_left_child():
                                current.parent.left = min
                            else:
                                current.parent.right = min
                            min.parent = current.parent
                        else:
                            self._root = min

                        min.right = current.right
                        if min.right:
                            min.right.parent = min
                        min.left = current.left
                        if min.left:
                            min.left.parent = min
                        current = None
                        break

    def search(self, key):
        current = self._root

        while True:
            if key == current.value:
                return current
            elif key > current.value:
                current = current.right
            else:
                current = current.left

    def inorder(self, node):
        """
            In-order (or depth-first): first look at the left child of a node
            then at the node itself and finally at its right child.
        """
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def preorder(self, node):
        """
            Pre-order: first look at a node then its left and right children.
        """
        if node is not None:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """
            Post-order: first look at the left and right children and
            process the node itself last.
        """
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

if __name__ == '__main__':
    bst = Binary_Search_Tree()
    arr = [7, 2, 5, 10, 9, 1]
    for i in arr:
        bst.insert(i)
    print('--------inorder----------')
    bst.inorder(bst.root)
    print('--------postorder----------')
    bst.postorder(bst.root)
    print('--------preorder----------')
    bst.preorder(bst.root)
    print('--------remove-------------')
    bst.remove(2)
    bst.inorder(bst.root)
    print(bst.root.height)
