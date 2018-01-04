from operator import itemgetter
from countries_list import countries

def most_borders():
    ''' Korzystając w ze ściągniętego pliku z bazą krajów.
    Znajdź kraj, który graniczy z największą ilością innych krajów (borders)
    i wyświetl jego nazwę oraz ilość granic
    >>> most_borders()
    ['China', 16]
    '''
    borders = []
    for country in countries:
        borders.append([country["name"]["common"], len(country["borders"])])
    print(sorted(borders, key=itemgetter(1), reverse=True)[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
