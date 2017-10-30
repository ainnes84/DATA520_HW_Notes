def convert_to_celsius(fahrenheit, degrees):
    """ (number) -> float

    Return the number of Celsius degrees equal to fahrenheit
    with 1 decimal place

    >>> convert_to_celsius(67, 53)

    """
    return round(float(format(([fahrenheit - 32.00) * 5.00 / 9.00, '2f'])))
                       
