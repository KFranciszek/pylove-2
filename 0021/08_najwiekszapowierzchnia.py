from operator import itemgetter
from countries_list import countries

def biggest_country():
    '''
    Korzystając w ze ściągniętego pliku z bazą krajów.
    Znajdź kraj o największej powierzchni i wyświetl jego nazwę i powierzchnię.
    >>> biggest_country()
    ['Russia', 17098242]
    '''
    areas = []
    for country in countries:
        areas.append([country["name"]["common"], country["area"]])
    print(sorted(areas, key=itemgetter(1), reverse=True)[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
