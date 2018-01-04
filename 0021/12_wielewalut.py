from countries_list import countries

def many_currencies():
    ''' Korzystając w ze ściągniętego pliku z bazą krajów.
    Wyświetl wszystkie kraje, które mają więcej niż jedną walutę
    (currency) oraz wypisz te waluty.
    >>> many_currencies()
    [['Bolivia', ['BOB', 'BOV']], ['Bhutan', ['BTN', 'INR']], \
['Switzerland', ['CHE', 'CHF', 'CHW']], ['Chile', ['CLF', 'CLP']], \
['Cuba', ['CUC', 'CUP']], ['Western Sahara', ['MAD', 'DZD', 'MRO']], \
['Haiti', ['HTG', 'USD']], ['Lesotho', ['LSL', 'ZAR']], ['Namibia', \
['NAD', 'ZAR']], ['Panama', ['PAB', 'USD']], ['El Salvador', ['SVC', 'USD']], \
['Uruguay', ['UYI', 'UYU']], ['United States', ['USD', 'USN', 'USS']]]
    '''

    currencies = []
    for country in countries:
        if len(country["currency"]) > 1:
            currencies.append(
                [country["name"]["common"], country["currency"]]
            )
    print(currencies)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
