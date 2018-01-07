from countries_list import countries

def capital_city_with_w():
    '''
    Korzystając w ze ściągniętego pliku z bazą krajów.
    Wyświetl wszystkie kraje i ich stolice, jeśli stolica
    zaczyna się od litery W.
    >>> capital_city_with_w()
    [['Cocos (Keeling) Islands', 'West Island'], ['Curaçao', 'Willemstad'], \
['Namibia', 'Windhoek'], ['New Zealand', 'Wellington'], ['Poland', \
'Warsaw'], ['United States', 'Washington D.C.']]
    '''
    capital_cities = []
    for country in countries:
        for capital in country["capital"]:
            if capital[0] == "W":
                capital_cities.append(
                    [country["name"]["common"], country["capital"]]
                )
    print(capital_cities)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
