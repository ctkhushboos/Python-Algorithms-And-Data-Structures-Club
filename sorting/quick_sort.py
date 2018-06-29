import random

"""
    Goal: Sort an array from low to high (or high to low).

    Quicksort is one of the most famous algorithms in history.
    It was invented way back in 1959 by Tony Hoare,
    at a time when recursion was still a fairly nebulous concept.

    quicksort does not produce a "stable" sort (unlike merge sort, for example)
    Most of the time that's not a big deal.
"""


def equals(element_a, element_b):
    return element_a == element_b


def less(element_a, element_b):
    return element_a < element_b


def greater(element_a, element_b):
    return element_a > element_b


def swapt_at(array, indexFrom, indexTo):
    temp = array[indexFrom]
    array[indexFrom] = array[indexTo]
    array[indexTo] = temp


def quick_sort(array):
    """ basic way """
    size = len(array)

    if size <= 1:
        return array
    else:
        pivot = array[int(size / 2)]

        def less_pivot(element):
            return less(element, pivot)

        def greater_pivot(element):
            return greater(element, pivot)

        def equals_pivot(element):
            return equals(element, pivot)

        less_array = list(filter(less_pivot, array))
        greater_array = list(filter(greater_pivot, array))
        equal_array = list(filter(equals_pivot, array))
        return quick_sort(less_array) + equal_array + quick_sort(greater_array)


def partition_dutch_flag(array, low, high, pivotIndex):
    """ Dutch national flag partitioning """
    pivot = array[pivotIndex]

    smaller = low
    equal = low
    larger = high

    while equal <= larger:
        if array[equal] < pivot:
            swapt_at(array, smaller, equal)
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            equal += 1
        else:
            swapt_at(array, equal, larger)
            larger -= 1

    return smaller, larger


def quick_sort_dutch_flag(array, low, high):
    if low < high:
        pivotIndex = random.randint(low, high)
        (p, q) = partition_dutch_flag(array, low, high, pivotIndex)
        quick_sort_dutch_flag(array, low, p - 1)
        quick_sort_dutch_flag(array, q + 1, high)


if __name__ == '__main__':
    test_array = [10, 0, 3, 9, 2, 14, 8, 27, 1, 5, 8, -1, 26]

    quick_sort_dutch_flag(test_array, 0, len(test_array) - 1)

    print(test_array)
