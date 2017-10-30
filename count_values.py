def count_values(dictionary):
    """ (dict) -> int

    Return the number of unique values in a dictionary.

    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    """

    return len(set(dictionary.values()))
