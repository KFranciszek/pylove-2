# 2.1	Wczytaj plik i stwórz słownik w którym kluczem będzie imię (i
# nazwisko) a wartością będzie słownik z kluczami kolor oczu i wzrost
# Przykład: {"Yoda": {"height": 66, "eyes": "brown"}}
import os, sys
with open(os.path.join(sys.path[0], 'py1.2'), 'r') as file:
    data = file.readlines()
    people = {}
    for item in data:
        name = item[item.rfind('.')+1:item.rfind(' has')].rstrip()
        eyes = item[item.rfind('has ')+4:item.rfind('and')].rstrip()
        height = item[item.rfind('is')+2:item.rfind('cm')-1].rstrip()
        people.update({name:{"height": int(height), "eyes": eyes}})

    print(people)
