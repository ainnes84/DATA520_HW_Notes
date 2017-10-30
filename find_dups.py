def find_dups(List):
    """ (list) -> set

    Return the number of duplicates from List.

    >>> find_dups([1, 2, 2, 3, 3, 4, 1, 4,])
    {1, 2, 3, 4}
    >>> find_dups([1, 2, 3, 4])
    set()
    """

    first_set = set()
    duplicate_set = set()

    for integers in List:
        initial_length = len(first_set)
        first_set.add(integers)
        end_length = len(first_set)
        if initial_length == end_length:
            duplicate_set.add(integers)

    return(duplicate_set)
