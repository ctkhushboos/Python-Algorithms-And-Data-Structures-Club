"""

A priority queue is a queue where the most important element is always at the front.

The queue can be a max-priority queue (largest element first) or a min-priority
(smallest element first).



There are different ways to implement priority queues:

As a sorted array. The most important item is at the end of the array.
Downside: inserting new items is slow because they must be inserted in sorted order.

As a balanced binary search tree. This is great for making a double-ended priority queue because it implements both "find minimum" and "find maximum" efficiently.

As a heap. The heap is a natural data structure for a priority queue.
In fact, the two terms are often used as synonyms.
A heap is more efficient than a sorted array because a heap only has to be partially sorted.
All heap operations are O(log n).

"""

import sys
sys.path.append('../Tree/')

from Heap import*

def order(value1, value2):
    return value1 < value2

def reverse(value1, value2):
    return value1 > value2


class Priority_Queue:
    def __init__(self, sort):
        self.heap = Heap([], sort)

    def __repr__(self):
        return '{}'.format(self.heap)

    @property
    def count(self):
        return self.heap.count

    def is_empty(self):
        self.heap.is_empty()

    def peek(self):
        return self.peek()

    def enqueue(self, element):
        self.heap.insert(element)

    def dequeue(self):
        return self.heap.remove()

    def change_priority(self, index, value):
        return self.heap.replace(index, value)

if __name__ == '__main__':
    _list = [1, 2, 3, 4, 5]
    p = Priority_Queue(order)
    for l in _list:
        p.enqueue(l)
    print(p)
