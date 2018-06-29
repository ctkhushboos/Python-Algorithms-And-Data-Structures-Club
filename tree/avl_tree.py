"""
    https://www.geeksforgeeks.org/practice-questions-height-balancedavl-tree/

    if there are n nodes in AVL tree,
    minimum height of AVL tree is floor(log2n).

    If there are n nodes in AVL tree, maximum height can’t exceed 1.44*log2n.

    if height of AVL tree is h, maximum number of nodes can be 2h+1 – 1.

    Minimum number of nodes in a tree with height h can be represented as:
    N(h) = N(h-1) + N(h-2) + 1 for n>2 where N(0) = 1
    N(1) = 2.

    The complexity of searching, inserting and deletion in AVL tree is O(log n)

"""


class Node(object):
    pass
