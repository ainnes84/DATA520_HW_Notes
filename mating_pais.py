def mating_pairs(males, females):
    """ (set, set) -> set of tuples

    Return a set of tuples where each tuple contains one male and one female.

    >>>mating_pairs({'Andrew', 'Steve', 'Carl'},{'Kayla', 'Hannah', 'Janet'})
    {('Andrew', 'Janet'), ('Carl', 'Kayla'), ('Steve', 'Hannah')}
    """

    pairs = set()
    number_gerbils = len(males)

    for i in range(number_gerbils):
        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)

    return pairs
