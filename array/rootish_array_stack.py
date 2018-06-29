"""

    A Rootish Array Stack is an ordered array based structure that minimizes
    wasted space (based on Gauss's summation technique).

    A Rootish Array Stack consists of an array holding many fixed size arrays
    in ascending size.

    better read it
    https://github.com/raywenderlich/swift-algorithm-club/tree/master/Rootish%20Array%20Stack

"""

import math


class RootishArrayStack(object):
    def __init__(self):
        self._blocks = []
        self._internal_count = 0

    def __repr__(self):
        return "{0}".format(self._blocks)

    def __getitem__(self, index):
        block = self.block(index)
        inner_block_index = self.inner_block_index(index, block)
        return self._blocks[block][inner_block_index]

    def __setitem__(self, index, value):
        block = self.block(index)
        inner_block_index = self.inner_block_index(index, block)
        self._blocks[block][inner_block_index] = value

    @property
    def count(self):
        return self._internal_count

    @property
    def capacity(self):
        return int(len(self._blocks) * (len(self._blocks) + 1) / 2)

    def block(self, from_index):
        return int(math.ceil((-3.0 + math.sqrt(9.0 + 8.0 * from_index)) / 2))

    def inner_block_index(self, from_index, from_block):
        return int(from_index - from_block * (from_block + 1) / 2)

    def grow_if_need(self):
        if self.capacity - len(self._blocks) < self.count + 1:
            new_array = [None for i in range(len(self._blocks) + 1)]
            self._blocks.append(new_array)

    def shrink_if_need(self):
        if self.capacity + len(self._blocks) >= self.count:
            while len(self._blocks) > 0 and (len(self._blocks) - 2) * (
                    len(self._blocks) - 1) / 2 > self.count:
                self._blocks.remove(self._blocks[int(len(self.block) - 1)])

    def insert(self, element, at_index):
        self.grow_if_need()
        self._internal_count += 1
        i = self.count - 1

        while i > at_index:
            self[i] = self[i - 1]
            i -= 1

        self[at_index] = element

    def append(self, element):
        self.insert(element, self.count)

    def remove(self, at_index):
        element = self[at_index]
        for i in range(at_index, self.count - 1):
            self[i] = self[i + 1]

        self._internal_count -= 1
        self.make_none(self.count)
        self.shrink_if_need()
        return element

    def make_none(self, index):
        block = self.block(index)
        inner_block_index = self.inner_block_index(index, block)
        self._blocks[block][inner_block_index] = None


if __name__ == "__main__":
    r = RootishArrayStack()
    r.insert(6, 0)
    r.insert(100, 0)
    r.insert(1000, 0)
    r.append(-6)
    r.remove(2)
    r.append(88)

    print(r)
