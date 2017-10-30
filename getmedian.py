# getmedian.py

def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8]) # sorted 2,2,4,5,7,8,9,9,9
    7
    >>> median([2, 9, 9, 9, 2, 4, 5, 8]) # sorted 2,2,4,5,8,9,9,9
    6.5
    '''
    copy = sorted(pool)
    nvals = len(copy)
    if nvals % 2 == 1:
        return copy[(nvals - 1) // 2]
    else:
        return (copy[nvals//2 - 1] + copy[nvals//2]) / 2

if __name__ == '__main__': # test function only when called alone
    import doctest
    doctest.testmod(verbose=True)
