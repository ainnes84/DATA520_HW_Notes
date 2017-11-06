def min_index(List):
    """ (list) -> (object, int)

    Return a tuple containing the minimum value in the list and that value's index.

    >>> min_index(['green','red','blue','green','red','green','blue','green','blue','green'
    ,'blue','red','blue','red','green','green','green','green'])
    ('blue', 2)
    """

    index = 0
    minimum = List[0]

    for x in range(1, len(List)):
        if List[x] < minimum:
            index = x
            minimum = List[x]

    return (minimum, index)
