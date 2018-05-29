"""

This is an array that is always sorted from low to high.
Whenever you add a new item to this array,
it is inserted in its sorted position.

An ordered array is useful for when you want your data to be sorted and you're
inserting new items relatively rarely. In that case,
it's faster than sorting the entire array. However,
if you need to change the array often,
it's probably faster to use a regular array and sort it manually.

"""


class OrderdArray(object):

    def __init__(self, array):
        self._array = sorted(array)

    def __repr__(self):
        return  "{0}".format(self._array)

    def __getitem__(self, index):
        if index < 0:
            raise "index cannot lower than zero"
        elif index >= self.count:
            raise "index out of range"
        else:
            return self._array[index]

    @property
    def count(self):
        return len(self._array)

    def is_empty(self):
        return len(self._array) == 0

    def remove_at(self, index):
        if index < 0:
            raise "index cannot lower than zero"
        elif index >= self.count:
            raise "index out of range"
        else:
            return self._array.remove(index)

    def remove_all(self):
        self._array = []

    def find_insert_point(self, element):
        start_index = 0
        end_index = self.count

        while start_index < end_index:
            mid_index = int(start_index + (end_index - start_index) / 2)

            if self._array[mid_index] == element:
                return mid_index
            elif self._array[mid_index] < element:
                start_index = mid_index + 1
            else:
                end_index = mid_index

        return  start_index

    def insert(self, new_element):
        i = self.find_insert_point(new_element)
        self._array.insert(i, new_element)
        return i


if __name__ == "__main__":
    a = OrderdArray(array=[5, 1, 3, 9, 7, -1])

    print(a)

    a.insert(4)
    print(a)

    a.insert(-2)
    print(a)

    a.insert(10)
    print(a)
