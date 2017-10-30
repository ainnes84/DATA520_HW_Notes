def convert_fuel(fuel, amount):
    """
    convert_fuel(str, number) -> float

    Take either MPG or liters per 100km and convert it to the other form.

    >>> convert_fuel('mpg',41)
    6.889756097560976 liters per 100km
    
    >>> convert_fuel('mpg', 45)
    6.277333333333334 liters per 100km
    
    >>> convert_fuel('mpg', 50)
    5.6496 liters per 100km
    
    >>> convert_fuel('liters per 100km', 5)
    47.0428 mpg
    
    >>> convert_fuel('liters per 100km', 2)
    117.607 mpg
    
    >>> convert_fuel('liters per 100km', 10)
    23.5214 mpg
    """

    boo = False
    if fuel == 'mpg':
        amount = (282.48 / amount)
        print (amount, 'liters per 100km')
        boo = True
    elif fuel == 'liters per 100km':
        amount = (235.214 / amount)
        print (amount, 'mpg')
        boo = True
    elif boo == False:
        print ("Please us fuel as 'mpg' or 'liters per 100km'")
