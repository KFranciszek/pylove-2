def cezar(word, move):
    '''
    Wykorzystując dwie nowe wbudowane
    char() ord()
    ord("a")
    97
    chr(98)
    b
    funkcje zaimplementuj szyfr cezara, który jako drugi parametr będzie
    brał przesunięcie.
    Przykłady szyfr cezaraz o parametrze 3 podmieni każd literka alfabetu
    na trzecią z kolei np A na D a Z na C.
    >>> cezar("abc", 2)
    cde
    >>> cezar("abc", -2)
    yza
    >>> cezar("ABC", 2)
    CDE
    >>> cezar("AaB", -2)
    YyZ
    >>> cezar("a12", 2)
    c12

    Pamiętaj żeby znaki inne niż litery nie zmieniać.
    uwzględnij dodatkowo wielkie litery
    '''
    new_word = ''
    for letter in word:
        if letter.isalpha():
            place = ord(letter)
            place += move

            if letter.isupper():
                if place > ord('Z'):
                    place -= 26
                elif place < ord('A'):
                    place += 26
            elif letter.islower():
                if place > ord('z'):
                    place -= 26
                elif place < ord('a'):
                    place += 26
            new_word += chr(place)
        else:
            new_word += letter
    print(new_word)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
