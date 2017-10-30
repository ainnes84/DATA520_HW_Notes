def dict_interest(dictionary1, dictionary2):
    """ (dict, dict) - > dict

    Return a dictionary that contains only the key/value pairs found in both of the
    orignal dictionaries.

    >>> dict_interest({'a': 1, 'b': 2, 'c': 3},{'c': 4, 'b': 2, 'c': 3})
    {'b': 2, 'c': 3}
    """

    intersect = {}

    for (key, value) in dictionary1.items():
        if key in dictionary2 and value == dictionary2[key]:
            intersect[key] = value

    return intersect
