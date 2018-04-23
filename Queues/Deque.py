"""
    A double-ended queue. For some reason this is pronounced as "deck".

    A regular queue adds elements to the back and removes from the front.
    The deque also allows enqueuing at the front and dequeuing from the back,
    and peeking at both ends.
"""
from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    @property
    def count(self):
        return self.deque.count

    def is_empty(self):
        return self.deque.count == 0

    def enqueue(self, element):
        self.deque.append(element)

    def enqueue_front(self, element):
        self.deque.appendleft(element)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.deque.popleft()

    def dequeue_back(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop()

    def peek_front(self):
        return self.deque[0]

    def peek_back(self):
        return slef.deque[-1]


if __name__ == '__main__':
    deque = Deque()
    deque.enqueue(1)
    deque.enqueue(2)
    deque.enqueue(3)
    deque.enqueue(4)

    print(deque.dequeue())
    print(deque.dequeue_back())

    deque.enqueue_front(5)
    print(deque.dequeue())
