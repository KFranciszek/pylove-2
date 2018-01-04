import json

with open('py1.2.json', encoding='utf-8') as file:
    data = json.load(file)
    sw_women = []
    sw_men = []
    for person in data:
        name = person['name']
        gender = person['gender']
        if gender == "male":
            sw_men.append(name)
        elif gender == "female":
            sw_women.append(name)
    with open('sw_men', 'w', encoding='utf-8') as file1:
        file1.write(str(sw_men))
    with open('sw_women', 'w', encoding='utf-8') as file2:
        file2.write(str(sw_women))


