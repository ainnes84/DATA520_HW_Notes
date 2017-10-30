def SuperFloatPow(x, y, z):
    """(number, number, number) -> float

    Return three numbers including float and the first number is taken to the second power
    then diveded by the third and the answer is the remainder.

    >>>SuperFloatPow(3.7, 4.5, 6.2)

    """
    return((x ** y) % z)
