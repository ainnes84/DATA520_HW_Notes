def linear_search_for(lst, value):
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

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i

    return -1
        
