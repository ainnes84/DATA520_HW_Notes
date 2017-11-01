# binary_search1.py
def binary_search(L, v):
    """ (list, object) -> int
    Return the index of the first occurrence of value in L, or return
    -1 if value is not in L.
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1) # first one
    0
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4) # twice; get first
    2
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 5) # in middle
    4
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10) # last one
    7
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3) # smaller than all
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 11) # larger than all
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 2) # not in list, but value between others
    -1
    >>> binary_search([], -3) # empty list
    -1
    >>> binary_search([1], 1) # list size = 1
    0
    """
    # Multiple test cases because many situations can arise, as above
    # Mark the left and right indices of the unknown section. (whole list)
    i = 0
    j = len(L) - 1

    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1

# doctest with verbose = True
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
