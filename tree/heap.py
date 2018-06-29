"""
    A heap is a binary tree inside an array,
    so it does not use parent/child pointers.

    A heap is sorted based on the "heap property" that determines the order of
    the nodes in the tree.

    implement in array
"""


def order(value_1, value_2):
    return value_1 < value_2


def reverse(value_1, value_2):
    return value_1 > value_2


class Heap(object):
    def __init__(self, array=[], sort=order):
        self.sort = sort
        self.configure_heap(array)
        self.nodes = array

    def __repr__(self):
        return '{}'.format(self.nodes)

    @property
    def is_empty(self):
        return len(self.nodes) == 0

    @property
    def count(self):
        return len(self.nodes)

    @property
    def order_criteria(self):
        """
            determines how to compare two nodes in the heap.
            use 'order' for a max-heap or 'reverse' for a min-heap,
            or provide a comparing
            method if the heap is made of custom elements, for example tuple
        """
        return self.sort

    @order_criteria.setter
    def order_criteria(self, value):
        self.sort = value

    def configure_heap(self, array):
        """
            configure the max-heap or max-heap from an array, in a bottom-up
            manner performance: it runs pretty much in O(n)
        """
        self.nodes = array
        for i in range(int(len(self.nodes) / 2 - 1), 0, -1):
            self.shift_down(i)

    def parent_index(self, index):
        """
            return the index of parent of the element at index i
            the element at index 0 is the root of the tree and has no parent
        """
        return int((index - 2) / 2)

    def left_child_index(self, index):
        """
            return the index of the left child of the element at index i
            note that this index can be greater than the heap size, in which
            case there is not left child
        """
        return int(2 * index + 1)

    def right_child_index(self, index):
        """
            return the index of the right child of the element at index i
            note that this index can be greater than the heap size, in which
            case there is not right child
        """
        return int(2 * index + 2)

    def peak(self):
        """
            return the max value in the heap (for a max-heap) or the minimum
            value (for a min-heap)
        """
        try:
            return self.nodes[0]
        except ValueError:
            return None

    def insert(self, value):
        """
            adds a new value to the heap. This reorders the heap so that the
            max heap or min-heap property still holdsself.
            performance: O(log n)
        """
        self.nodes.append(value)
        self.shift_up(len(self.nodes) - 1)

    def insert_sequence(self, sequence):
        """
            adds a sequence of values to the heap. It reorders the heap so that
            the max-heap or min-heap property still holds.
            performance: O(log n)
        """
        for s in sequence:
            self.insert(s)

    def replace(self, index, value):
        """
            allows you to change an element. It reorders the heap so that the
            max-heap or min-heap property still holds.
        """
        if not index < len(self.nodes):
            return

        self.remove(index)
        self.insert(value)

    def remove_root(self):
        """
            removes the root node from the heap. For a max-heap, this is the
            maximum value; for a min-heap it is the minimum valueself.
            performance: O(log n)
        """
        if self.is_empty():
            return
        elif self.count == 1:
            return self.nodes.remove_last()
        else:
            # use the left node to replace the first one, the fix the heap by
            # shifting this new first node into its proper position
            value = self.nodes[0].copy()
            self.nodes[0] = self.nodes.remove_last()

            return value

    def remove(self, index):
        """
            removes an arbitrary node from the heapself.
            performance: O(log n)
            note that you need to know the node's index
        """
        if not index < len(self.nodes):
            return None

        size = len(self.nodes) - 1
        if not index == size:
            self.nodes.swap_at(index, size)
            self.shift_down_from(index, size)
            self.shift_up(index)

        return self.nodes.remove_last()

    def shift_up(self, index):
        """
            takes a child node and looks at its parents; if a parent is not
            larger (max-heap) or not smaller (min-heap) than the child, we
            exchange them.
        """
        child_index = index
        child = self.nodes[child_index]
        parent_index = self.parent_index(child_index)

        while child_index > 0 and self.order_criteria(
                child, self.nodes[parent_index]):
            self.nodes[child_index] = self.nodes[parent_index]
            child_index = parent_index
            parent_index = self.parent_index(child_index)

        self.nodes[child_index] = child

    def shilft_down_from(self, from_index, end_index):
        """
            looks at a parent node and makes sure it is still larger (max-heap)
            or smaller (min-heap) than its children.
        """
        left_child_index = self.left_child_index(from_index)
        right_child_index = left_child_index + 1
        # figure out thich comes first if we order them by sort function:
        # the parent, the left child, or right child. If the parent comews
        # first, we're done. If not, that element is out-of-place and we make
        # if 'float down' the tree untill the heap property is restored
        first = from_index
        if left_child_index < end_index and self.order_criteria(
                self.nodes[left_child_index], self.nodes[first]):
            first = left_child_index

        if right_child_index < end_index and self.order_criteria(
                self.nodes[right_child_index], self.nodes[first]):
            first = right_child_index

        if first == from_index:
            return

        self.swap_at(from_index, first)
        self.shilft_down_from(first, end_index)

    def shift_down(self, index):
        self.shilft_down_from(index, len(self.nodes))

    def swap_at(self, index_1, index_2):
        temp = self.nodes[index_1]
        self.nodes[index_1] = self.nodes[index_2]
        self.nodes[index_2] = temp


if __name__ == '__main__':
    _list = [1, 2, 3, 4, 5]
    heap = Heap(_list, reverse)
    heap.insert(1)
    print(heap)
