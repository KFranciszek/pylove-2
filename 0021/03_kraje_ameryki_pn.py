import urllib.request

data = urllib.request.urlopen("http://dyba.it/countries.py").read()
f = open('countries_list.py', 'wb')
f.write(data)
f.close()
from countries_list import countries

print("Northern American countries are:")
for c in countries:
    if c["subregion"] == "Northern America":
        print(c["name"]["common"])
