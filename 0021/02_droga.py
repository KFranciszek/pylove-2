def droga(t, a, vs=0):
    '''
    Napisz funkcję, która policzy drogę pokonaną przez samochód w czasie t i
    przyspieszeniu a z opcjonalną prędkością początkową, domyślnie równą 0.
    >>> droga(5, 5)
    62.5
    >>> droga(10, 10, vs=100)
    1500.0
    '''

    result = vs*t + (a * (t ** 2))/2
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
