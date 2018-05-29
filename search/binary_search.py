"""
    Goal: Quickly find an element in an array.

    Split the array in half and determine whether the thing you're looking for, known as the search key, is in the left half or in the right half.

    How do you determine in which half the search key is? This is why you sorted the array first, so you can do a simple < or > comparison.

    If the search key is in the left half, you repeat the process there: split the left half into two even smaller pieces and look in which
    piece the search key must lie. (Likewise for when it's the right half.)

    This repeats until the search key is found. If the array cannot be split up any further, you must regrettably conclude that the search key is not present in the array.

"""

def binary_search(_list, key, lower, upper):
    """ recursive version """
    if lower >= upper:
        return None
    else:
        mid = int(lower + (upper - lower) / 2)
        if _list[mid] > key:
            return binary_search(_list, key, lower, mid)
        elif _list[mid] < key:
            return binary_search(_list, key, mid + 1, upper)
        else:
            return mid

def _binary_search(_list, key):
    """ loop version """
    lower = 0
    upper = len(_list)
    while lower < upper:
        mid = int(lower + (upper - lower) / 2)
        if _list[mid] == key:
            return mid
        elif _list[mid] < key:
            lower = mid + 1
        else:
            upper =mid

    return None

if __name__ == '__main__':
    numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

    print(binary_search(numbers, 43, 0, len(numbers)))
    print(_binary_search(numbers, 43))
