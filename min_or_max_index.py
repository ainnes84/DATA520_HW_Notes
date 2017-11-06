def min_or_max_index (List, Decision):
    """ (list, bool) -> tuple of (object, int)

    Return the minimum or maximum item and its index depending on if the
    Boolean statement is True or False.

    >>> min_or_max_index(['green','red','blue','green','red','green','blue','green','blue','green','blue',
    'red','blue','red','green','green','green','green'], True)
    ('blue', 2)
    >>> min_or_max_index(['green','red','blue','green','red','green','blue','green','blue','green','blue',
    'red','blue','red','green','green','green','green'], False)
    ('red', 1)
    """

    index = 0
    value = List[0]

    if Decision:
        for x in range(1, len(List)):
            if List[x] < value:
                index = x
                value = List[x]
    else:
        for x in range(1, len(List)):
            if List[x] > value:
                index = x
                value = List[x]

    return (value, index)
        
                
