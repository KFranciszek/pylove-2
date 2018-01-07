# 2.3*Zapisz średni wzrost postaci dla każdego z kolorów w osobnych
# linijkach w formie:
# Średni wzrost osób z kolorem oczu blue wynosi 123,12 cm.

import os
import sys

with open(os.path.join(sys.path[0], 'py1.2'), 'r') as file:
    data = file.readlines()
    people = []
    for item in data:
        name = item[item.rfind('.')+1:item.rfind(' has')].rstrip()
        eyes = item[item.rfind('has ')+4:item.rfind('and')].rstrip()
        height = item[item.rfind('is')+2:item.rfind('cm')-1].rstrip()
        people.append({ name: {"height": int(height), "eyes": eyes}})

    # get list of colors
    # print(people)
    colors = []
    for person in people:
        person_name = person[list(person.keys())[0]]
        colors.append(person_name['eyes'])
    unique_colors = list(set(colors))
    print(unique_colors)

    people_by_color = []
    for color in unique_colors:
        summup = 0
        height_sum = 0
        for person in people:
            person_name = person[list(person.keys())[0]]
            if person_name['eyes'] == color:
                summup += 1
                height_sum += person_name['height']
                avg = height_sum/summup
                if any(color in vals for vals in people_by_color) == True:
                    people_by_color[people_by_color.index(color)] = { color: {"sum": summup, "avg": avg}}
                else:
                    people_by_color.append({ color: {"sum": summup, "avg": avg}})
    print(people_by_color)

    # print(people)
