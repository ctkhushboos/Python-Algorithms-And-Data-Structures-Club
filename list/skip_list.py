"""
    A skip list S consists of series of sorted linked lists
    {L0, ..., Ln}, layered hierarchicaly and each layer L stores a subset
    of items in layer L0 in incremental order. The items in layers {L1, ... Ln}
    are chosen at random based on a coin flipping function with probability 1/2

    For traversing, every item in a layer hold references to the node below
    and the next node.

    This layers serve as express lanes to the layer underneath them,
    effectively making fast O(log n) searching possible by skipping lanes and
    reducing travel distance and in worse case searching degrades to O (n)
    as expected with regular linked list.
"""

if __name__ == '__main__':
    pass
