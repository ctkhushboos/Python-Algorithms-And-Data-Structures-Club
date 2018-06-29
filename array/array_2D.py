"""
    In C and Objective-C, you can write the following line
    int cookies[9][7];

    to make a 9x7 grid of cookies. This creates a two-dimensional array of
    63 elements. To find the cookie at column 3 and row 6, you can write:

    myCookie = cookies[3][6];

    This statement is not acceptable in Swift. To create a
    multi-dimensional array in Python, you can write:

    w, h = 9, 7;
    cookies = [[0 for x in range(w)] for y in range(h)]

"""


class Array2D(object):
    def __init__(self, columns, rows, init_values):
        self.columms = columns
        self.rows = rows
        self.array = [[init_values for _ in range(columns)]
                      for _ in range(rows)]

    def __getitem__(self, x):
        return self.array[x]

    def __repr__(self):
        return "{0}".format(self.array)

    @property
    def columms(self):
        return self._columms

    @columms.setter
    def columms(self, value):
        self._columms = value

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value


if __name__ == "__main__":
    test = Array2D(2, 2, 0)
    test[1][1] = 5
    print(test)
    print(test[1][1])
