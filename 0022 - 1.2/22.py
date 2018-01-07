# '''
# 2.2 Zapisz wszystkie osoby wyższe niż 200 cm do pliku hero_200_plus a
# resztę do pliku hero_short.
# '''

import os, sys

with open(os.path.join(sys.path[0], 'py1.2'), 'r') as file:
    data = file.readlines()
    people_higherthan200 = {}
    people_rest = {}
    for item in data:
        name = item[item.rfind('.')+1:item.rfind(' has')].rstrip()
        height = item[item.rfind('is')+2:item.rfind('cm')-1].rstrip()
        if int(height) > 200:
            people_higherthan200.update({name:{"height": int(height)}})
            with open(os.path.join(sys.path[0], 'hero_200_plus'), 'w') as file2:
                file2.write(str(people_higherthan200))
        else:
            people_rest.update({name:{"height": int(height)}})
            with open(os.path.join(sys.path[0], 'hero_short'), 'w') as file3:
                file3.write(str(people_rest))

    print(people_higherthan200)
    print(people_rest)
