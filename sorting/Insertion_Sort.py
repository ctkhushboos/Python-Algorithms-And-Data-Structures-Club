"""
    Goal: Sort an array from low to high (or high to low).

    Put the numbers on a pile. This pile is unsorted.
    Pick a number from the pile. It doesn't really matter which one you pick,
    but it's easiest to pick from the top of the pile.
    Insert this number into a new array.

    Pick the next number from the unsorted pile and
    also insert that into the new array.
    It either goes before or after the first number you

    picked, so that now these two numbers are sorted.
    Again, pick the next number from the pile and
    insert it into the array in the proper sorted position.

    Keep doing this until there are no more numbers on the pile.
    You end up with an empty pile and an array that is sorted.

    The worst-case and average case performance of insertion sort is O(n^2).
    That's because there are two nested loops in this function.
    Other sort algorithms, such as quicksort and merge sort,
    have O(n log n) performance, which is faster on large inputs.

"""

def swapAt(_list, x, y):
    temp = _list[x]
    _list[x] = _list[y]
    _list[y] = temp

def insertion_sort(array):
    array_copy = array.copy()
    for i in range(1, len(array_copy)):
        y = i
        while y > 0 and array_copy[y] < array_copy[y - 1]:
            swapAt(array_copy, y - 1, y)
            y -= 1

    return array_copy

def _insertion_sort(array):
    """ improve the performance of last one"""
    array_copy = array.copy()
    for i in range(1, len(array_copy)):
        y = i
        temp = array_copy[y]
        while y > 0 and temp < array_copy[y - 1]:
            array_copy[y] = array_copy[y - 1]
            y -= 1

        array_copy[y] = temp

    return array_copy

if __name__ == '__main__':
    _list = [1, 6, 1, 5, 0, -1, 2, 6]
    swapAt(_list, 0, 1)
    print(_list)
    #print(insertion_sort(_list))
    print(_insertion_sort(_list))
