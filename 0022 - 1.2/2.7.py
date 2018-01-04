import json

with open('py1.2zd.json') as file:
    data = json.load(file)
    ships = []
    ships_unknown = []
    for item in data:
        name = item['name']
        cost = item['cost_in_credits']
        if cost!= "unknown":
            ships.append({"name": name, "cost": int(cost)})
        else:
            ships_unknown.append({"name": name, "cost": cost})
    ships.sort(key=lambda k: k["cost"])
    all_ships = ships + ships_unknown

    with open('shipsfile', 'a') as file:
        for ship in all_ships:
            file.writelines("{} kosztuje {} credits\n".format(ship['name'], ship['cost']))


