import urllib.request

data = urllib.request.urlopen("http://dyba.it/countries.py").read()
f = open('countries_list.py', 'wb')
f.write(data)
f.close()
from countries_list import countries

print("Countries not from Africa are:")
for c in countries:
    if c["region"] != "Africa":
        print(c["name"]["common"])
