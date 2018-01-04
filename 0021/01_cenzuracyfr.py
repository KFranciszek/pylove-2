def cenzura_cyfr(incoming):
    ''' Napisz funkcję, która zamieni wszystkie cyfry na "#" w tekście (stringu)
    >>> cenzura_cyfr("password12345")
    password#####
    >>> cenzura_cyfr("a1a ma k0ta")
    a#a ma k#ta
    '''

    char_list = list(str(incoming))
    cyfry = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for idx, char in enumerate(char_list):
        if char in cyfry:
            char_list[idx] = "#"
    print(''.join(char_list))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
