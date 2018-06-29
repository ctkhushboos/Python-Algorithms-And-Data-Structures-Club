"""
    Goal: Sort an array from low to high (or high to low)
    Invented in 1945 by John von Neumann,
    merge-sort is an efficient algorithm with a best,
    worst, and average time complexity of O(n log n).

    The merge-sort algorithm uses the divide and conquer approach
    which is to divide a big problem into smaller problems and solve them.
    I think of the merge-sort algorithm as split first and merge after.

    Put the numbers in an unsorted pile.
    Split the pile into two. Now, you have two unsorted piles of numbers.

    Keep splitting the resulting piles until you cannot split anymore.
    In the end, you will have n piles with one number in each pile.

    Begin to merge the piles together by pairing them sequentially.
    During each merge, put the contents in sorted order.

    This is fairly easy because each individual pile is already sorted.
"""


def merge(left_array, right_array):
    """
        This method may look scary, but it is quite straightforward:

        You need two indexes to keep track of your progress
        or the two arrays while merging.

        This is the merged array.
        It is empty right now,
        but you will build it up in subsequent steps by appending elements
        from the other arrays.

    """
    left_index = 0
    right_index = 0
    order_pile = []
    """
        This while-loop will compare the elements from the left and
        right sides and append them into the orderedPile
        while making sure that the result stays in order.
    """

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            order_pile.append(left_array[left_index])
            left_index += 1
        elif left_array[left_index] > right_array[right_index]:
            order_pile.append(right_array[right_index])
            right_index += 1
        else:
            order_pile.append(left_array[left_index])
            left_index += 1
            order_pile.append(right_array[right_index])
            right_index += 1
    """
        If control exits from the previous while-loop,
        it means that either the leftPile or
        the rightPile has its contents completely merged into the orderedPile.
        At this point, you no longer need to do comparisons.
        Just append the rest of the contents of the other array until
        there is no more to append.
    """
    while left_index < len(left_array):
        order_pile.append(left_array[left_index])
        left_index += 1

    while right_index < len(right_array):
        order_pile.append(right_array[right_index])
        right_index += 1

    return order_pile


def merge_sort(array):
    if len(array) <= 1:
        return array

    middleIndex = int(len(array) / 2)
    left_array = merge_sort(array[0: middleIndex])
    right_array = merge_sort(array[middleIndex:len(array)])

    return merge(left_array, right_array)


if __name__ == '__main__':
    print(merge_sort([9, 8, 7, 6, 5, 4, 5, 7]))
