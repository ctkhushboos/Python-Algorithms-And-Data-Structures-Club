"""

    A fixed-size sequence of n bits. Also known as bit array or bit vector.

    To store whether something is true or false you use a Bool. Every programmer
    knows that... But what if you need to remember whether 10,000 things are
    true or not?

    You could make an array of 10,000 booleans but you can also go hardcore and
    use 10,000 bits instead. That's a lot more compact because 10,000 bits fit
    in less than 160 Ints on a 64-bit CPU.

    Since manipulating individual bits is a little tricky,
    you can use BitSet to hide the dirty work.

    https://blog.csdn.net/thomashtq/article/details/45250401

    if you don't familiar with bit manipulation
    https://www.youtube.com/watch?v=7jkIUgLC29I

    https://www.youtube.com/watch?v=Ub1fE-bAroA

    https://www.youtube.com/watch?v=G8SI2Jrqeww
    watch above tutorial

"""

import numpy as np


if __name__ == "__main__":
    pass
