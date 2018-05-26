"""

    Early programming languages didn't have very fancy arrays.
    You'd create the array with a specific size and from that moment on
    it would never grow or shrink. Even the standard arrays in C and
    Objective-C are still of this type.

    When you define an array like so, int myArray[10];
"""

class FixedArray(object):
    def __init__(self, max_size, default_value):
        self._max_size = max_size
        self._defaul_value = default_value
        self._array = [default_value for i in range(max_size)]
        self._count = 0

    def __getitem__(self, index):
        if index < 0:
            raise "index cnnot lower than zero"
        elif index >= self.count:
            raise "index out of range"
        else:
            return self._array[index]

    def __repr__(self):
        return "{0}".format(self._array)

    @property
    def max_size(self):
        return  self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = value

    @property
    def default_value(self):
        return  self._defaul_value

    @default_value.setter
    def default_value(self, value):
        self._defaul_value = value

    @property
    def count(self):
        return self._count

    def append(self, new_element):
        if count >= self.max_size:
            raise "it's full cannot add new element"
        else:
            self._array[self.count] = new_element
            self._count += 1

    def remove_at(self, index):
        if index < 0:
            raise "index cnnot lower than zero"
        elif index >= count:
            raise "index out of range"
        else:
            count -= 1
            result = self._array[index]
            self._array[index] = self._array[self.count]
            self._array[self.count] = default_value
            return result

    def remove_all(self):
        for a in self._array:
            a = default_value

        self.count = 0



if __name__ == "__main__":
    a = FixedArray(max_size=10, default_value=0)
    print(a)
