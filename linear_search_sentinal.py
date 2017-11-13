def linear_search_sentinal(lst, value):
    """ (list, object) -> int

    Return the index of the last occurence of value in lst, or return -1
    if value is not in lst.

    >>> linear_search_while([2, 5, 1, -3], 5)
    1
    >>> linear_search_while([2, 4, 2], 2)
    2
    >>> linear_search_while([2, 5, 1, -3], 4)
    -1
    >>> linear_search_while([], 5)
    -1
    """

    lst.insert(0, value)

    i = len(lst) - 1

    while lst[i] != value:
        i = i - 1

    lst.pop(0)

    if i == 0:
        return -1
    else:
        return i - 1
