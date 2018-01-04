import urllib.request

def kraje_ameryki_pn():
    ''' Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie
    kraje w Ameryce Północnej. (Northern America).
    '''
    data = urllib.request.urlopen("http://dyba.it/countries.py").read()
    file = open('countries_list.py', 'wb')
    file.write(data)
    file.close()
    from countries_list import countries

    print("Northern American countries are:")
    for country in countries:
        if country["subregion"] == "Northern America":
            print(country["name"]["common"])

if __name__ == "__main__":
    import doctest
    doctest.testmod()

kraje_ameryki_pn()
