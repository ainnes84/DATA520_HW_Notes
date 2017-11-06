def dutch_flag(colors):
    """ (list of str) -> list of str

    Returns colors rearranged so that the srings are in the color of the Dutch national
    flag.('Red','Green','Blue')

    >>> dutch_flag(['green','red','blue','green','red','green','blue','green','blue','green',
    'blue','red','blue','red','green','green','green','green'])

    ['red', 'red', 'red', 'red', 'green', 'green', 'green', 'green', 'green',
    'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue']
    """

    green = 0

    first_color = 0

    last_color = len(colors) - 1

    while first_color <= last_color:

        if colors[first_color] == 'red':
            colors[green], colors[first_color] \
                           = colors[first_color], colors[green]
            green += 1
            first_color += 1

        elif colors[first_color] == 'green':
            first_color += 1

        else:
            colors[first_color], colors[last_color] \
                                 = colors[last_color], colors[first_color]
            last_color -= 1

    print(colors)
