def linear_search(vlist, srchval): # somewhat different from book
    """ (list, object) -> int
    Return the index of the first occurrence of value in lst, or return -1 if value is not in lst. >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
#Look at each item in list. If it equals the value you are looking for, stop.
    # linear_search_2.py
    index = 0
    for item in vlist:
        if item == srchval:
            return index # implicit break
        index += 1
        
    return -1
