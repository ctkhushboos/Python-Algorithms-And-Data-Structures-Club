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

class Heap:
    pass


class Priority_Queue:
    def __init__(self):
        pass




if __name__ == '__main__':
    pass
