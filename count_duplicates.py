def count_duplicates(dictionary):
    """ (dict) -> int

    Return the number of values that appear two or more times.

    >>> count_duplicates({'A': 1, 'B': 2, 'C': 1, 'D': 3, 'E': 1})
    1
    """

    duplicates = 0
    values = list(dictionary.values())

    for item in values:
        if values.count(item) >= 2:
            duplicates = duplicates + 1
            occurrences = values.count(item)
            for x in range(occurrences):
                values.remove(item)

    return duplicates
