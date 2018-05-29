"""
    Shell sort is based on insertion sort as a general way to improve
    its performance, by breaking the original list into smaller sublists which
    are then individually sorted using insertion sort.

    There is a nice video created at Sapientia University which shows the
    process as a Hungarian folk dance.
    https://www.youtube.com/watch?v=CmPA7zE8mx0

    The performance of shell sort is O(n^2) in most cases or O(n log n)
    if you get lucky. This algorithm produces an unstable sort;
    it may change the relative order of elements with equal values.
"""

def insertion_sort(array, start, gap):

    array_copy = array.copy()
    for i in range(start + gap, len(array_copy), gap):
        y = i
        temp = array_copy[y]
        while y > 0 and temp < array_copy[y - gap]:
            array_copy[y] = array_copy[y - gap]
            y -= gap

        array_copy[y] = temp

    return array_copy

def shell_sort(array):
    sublist_count = len(array) / 2

    while sublist_count > 0:
        sublist_count = int(sublist_count)
        for pos in range(sublist_count):
            array = insertion_sort(array, pos, sublist_count)

        sublist_count /= 2

    return array

if __name__ == '__main__':
    array = [64, 20, 50, 33, 72, 10, 23, -1, 4, 5]
    array = shell_sort(array)

    print(array)
