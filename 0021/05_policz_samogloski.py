def policz_samogloski(word):
    '''
    Napisz funkcję, która policzy wszystkie samogłoski w tekście. Przykład działania
    >>> policz_samogloski("Ala ma kota")
    5
    >>> policz_samogloski("Pies psu niedzwiedziem")
    9
    '''
    char_list = list(word.lower())
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for char in char_list:
        if char in samogloski:
            counter += 1
    print(counter)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
