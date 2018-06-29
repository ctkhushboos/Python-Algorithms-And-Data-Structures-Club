"""

Sorts an array from low to high using a heap.

A heap is a partially sorted binary tree that is stored inside an array.
The heap sort algorithm takes advantage of the structure of the heap to perform
a fast sort.

To sort from lowest to highest, heap sort first converts the unsorted array to
a max-heap, so that the first element in the array is the largest

"""

import heapq


def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]


if __name__ == "__main__":
    array = [9, 2, 3, 4, 6, 3, 2, 2, 0, -1, -99, 100]

    print(heap_sort(array))
