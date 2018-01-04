def odwazniki(weight1, weight2):
    ''' Napisz funkcję, która znajdzie liczbę odważników o wadze A aby
    zrównoważyć szale wagi z odważnikami o wadze B. Przykład działania:
    >>> odwazniki(2, 8)
    4, 1
    >>> odwazniki(4, 6)
    3, 2'''

    if weight1 > weight2:
        first_val = weight1
    else:
        first_val = weight2
    while True:
        if ((first_val % weight1 == 0) and (first_val % weight2 == 0)):
            lcm = first_val
            break
        first_val += 1
    print("{}, {}".format(int(lcm/weight1), int(lcm/weight2)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
