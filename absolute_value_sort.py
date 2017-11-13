def absolute_value_sort(lst):
    """ (list) -> NoneType

    Reorder the items in lst by magnitude.

    >>> absolute_value_sort([3, 4, 7, -1, 2, 5])
    [-1, 2, 3, 4, 5, 7]
    
    """
    
    for x in range(len(lst) - 1, 0, -1):
        for y in range(x):
            if abs(lst[y]) > abs(lst[y + 1]):
                temp = lst[y]
                lst[y] = lst[y + 1]
                lst[y + 1] = temp
            if abs(lst[y]) == abs(lst[y + 1]):
                if lst[y] > lst[y + 1]:
                    temp = lst[y]
                    lst[y] = lst[y + 1]
                    lst[y + 1] = temp
                else:
                    temp = lst[y + 1]
                    lst[y + 1] = lst[y]
                    lst[y] = temp
            if abs(lst[y]) == abs(lst[y - 1]):
                if lst[y] > lst[y - 1]:
                   temp = lst[y]
                   lst[y] = lst[y - 1]
                   lst[y - 1] = temp

if __name__=='__main__':
    lst = [3, 4, 7, -1, 2, 5]
    absolute_value_sort(lst)
    print(lst)
    
