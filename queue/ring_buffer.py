"""
    Also known as a circular buffer.

    The problem with a queue based on an array is that adding new items to the
    back of the queue is fast, O(1), but removing items from the front of the
    queue is slow, O(n). Removing is slow because it requires the remaining
    array elements to be shifted in memory.

    A more efficient way to implement a queue is to use a ring buffer or
    circular buffer. This is an array that conceptually wraps around back to
    the beginning, so you never have to remove any items.
    All operations are O(1).
"""


class RingBuffer(object):
    def __init__(self, count):
        self.buffer = [None] * count
        self.read_index = 0
        self.write_index = 0

    @property
    def available_space_for_reading(self):
        return self.write_index - self.read_index

    @property
    def is_empty(self):
        return self.available_space_for_reading == 0

    @property
    def available_space_for_writing(self):
        return len(self.buffer) - self.available_space_for_reading

    @property
    def is_full(self):
        return self.available_space_for_writing == 0

    def write(self, element):
        if not self.is_full:
            self.buffer[self.write_index % len(self.buffer)] = element
            self.write_index += 1
            return True
        else:
            return False

    def read(self):
        if not self.is_empty:
            element = self.buffer[self.read_index % len(self.buffer)]
            self.read_index += 1
            return element
        else:
            return None


if __name__ == '__main__':
    buffer = RingBuffer(5)
    buffer.write(123)
    buffer.write(456)
    buffer.write(789)
    buffer.write(666)

    print(buffer.read())  # 123
    print(buffer.read())  # 456
    print(buffer.read())  # 789

    buffer.write(333)
    buffer.write(555)

    print(buffer.read())  # 666
    print(buffer.read())  # 333
    print(buffer.read())  # 555
    print(buffer.read())  # None
