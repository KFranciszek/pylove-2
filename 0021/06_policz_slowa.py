def policz_slowa(word):
    '''
    Napisz funkcję, która policzy słowa w tekście. Każde słowo jest oddzielone spacją.
    Przykład działania
    >>> policz_slowa("Ala ma kota")
    3
    >>> policz_slowa("Pies psu niedzwiedziem, bo tak")
    5
    '''

    words_num = len(word.split())
    print(words_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
