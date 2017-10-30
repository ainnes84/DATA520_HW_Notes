def convert_temperatures(temp, source, desired):
    """ (number, str, str) -> number

    Convert temp from source to the disired temperature scale.

    >>>convert_temperatures(0, 'Celsius', 'Kelvin')
    273.15
    >>>convert_temperatures(0, 'Celsius', 'Fahrenheit')
    32.0
    >>>convert_temperatures(0, 'Celsius', 'Rankine')
    491.66999999999996
    """
    if source == 'Kelvin':
        celsius = temp - 273.15
    elif source == 'Celsius':
        celsius = temp
    elif source == 'Fahrenheit':
        celsius = (temp - 32) * 5 / 9
    elif source == 'Rankine':
        celsius = (temp - 491.67) * 5 / 9
    elif source == 'Delisle':
        celsius = 100 - temp * 2 / 3
    elif source == 'Newton':
        celsius = temp * 100 / 33
    elif source == 'Reamur':
        celsius = temp * 5 / 4
    elif source == 'Romer':
        celsius = (temp - 7.5) * 40 / 21
    if desired == 'Kelvin':
        return celsius + 273.15
    elif desired == 'Celsius':
        return celsius
    elif desired == 'Fahrenheit':
        return celsius * 9 / 5 + 32
    elif desired == 'Rankine':
        return (celsius + 273.15) * 9 / 5
    elif desired == 'Delisle':
        return (100 - celsius) * 3 / 2
    elif desired == 'Newton':
        return celsius * 33 / 100
    elif desired == 'Reamur':
        return celsius * 4 / 5
    elif desired == 'Romer':
        return celsius * 21 / 40 + 7.5
