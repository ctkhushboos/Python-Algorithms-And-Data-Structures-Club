"""
    must read it
    https://github.com/raywenderlich/swift-algorithm-club/tree/master/Tree

"""

class TreeNode(object):
    def __init__(self, value):
        self._value = value
        self._childern = []
        self._parent = None

    def __repr__(self):
        return "value: {0} childern: {1} parent: {2}".format(self._value, \
         [c.value for c in self._childern], "None" if self.parent is None else \
         self.parent.value)

    @property
    def value(self):
        return  self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    def add_caild(self, child):
        self._childern.append(child)
        child.parent = self

    def search(self, value):

        if value == self.value:
            return  self

        for child in self._childern:
            if child.search(value):
                return child.search(value)

        return "cannot find this one, try another one"


if __name__ == "__main__":
    root = TreeNode("root")
    root.add_caild(TreeNode("jamfly"))
    root.add_caild(TreeNode("henry"))
    root.add_caild(TreeNode("cool_1"))
    print(root)
    print(root.search("trump"))
