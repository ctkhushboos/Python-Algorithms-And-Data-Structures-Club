"""
    Goal: To sort an array from low to high (or high to low).

    Find the lowest number in the array

    Swap the lowest number with the number at index 0.
    Now, the sorted portion consists of just the number at index 0.

    Go to index 1.

    Find the lowest number in the rest of the array.
    This time you start looking from index 1.
    Again you loop until the end of the array and keep track of the lowest
    number you come across.

    Swap the lowest number with the number at index 1.
    Now, the sorted portion contains two numbers and
    extends from index 0 to index 1.

    And continue until no numbers remain to be sorted.

"""


def swapAt(array, from_index, to_index):
    temp = array[from_index]
    array[from_index] = array[to_index]
    array[to_index] = temp
    return array


def selection_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array) - 1):
        lowest_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_index]:
                lowest_index = j

        if i is not lowest_index:
            swapAt(array, i, lowest_index)

    return array


if __name__ == '__main__':
    array = [4, 1, 3, 9, 2, 7]
    selection_sort(array)
    print(array)
