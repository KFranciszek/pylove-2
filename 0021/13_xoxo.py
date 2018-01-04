def xo_checker(word):
    '''
    Napisz funkcję, która sprawdzi, czy liczba znaków "x" i "o" w stringu jest
    taka sama i zwróci True/False.
    Jeśli string zawiera coś innego niż "x" lub "o", to wypisze błąd.
    >>> xo_checker("xoxoxoxoxoxo")
    True
    >>> xo_checker("xxxoooxxxxxxxo")
    False
    >>> xo_checker("xpd")
    "Illegal letters in text"
    '''

    char_list = list(word.lower())
    x_counter = 0
    o_counter = 0

    for char in char_list:
        if char == "x":
            x_counter += 1
        elif char == "o":
            o_counter += 1
        else:
            print("Illegal letters in text")
            return

    if x_counter == o_counter:
        print("True")
        return True
    else:
        print("False")
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
