import urllib.request
from countries_list import countries

def krajeniezafryki():
    ''' Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie
    kraje niebędące w Afryce (Africa).
    '''

    print("Countries not from Africa are:")
    for country in countries:
        if country["region"] != "Africa":
            print(country["name"]["common"])

krajeniezafryki()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
