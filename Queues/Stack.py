"""
   Inserting at the beginning of an array is O(n) operation,
   because it requires all existing array elements to be shifted in memory.
   Adding at the end is O(1)
"""

class Stack:
    def __init__(self):
        self.list_ = []

    def is_empty(self):
        return len(self.list_) == 0

    def push(self, value):
        self.list_.append(value)

    def pop(self):
        return self.list_.pop()

    @property
    def top(self):
        return self.list_[-1]

    @property
    def count(self):
        return len(self.list_)

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(3)
    stack.push(57)
    print(stack.pop())
    print(stack.pop())
    print(stack.top)
    print(stack.count)
