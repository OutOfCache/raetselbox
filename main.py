# wenn Pfade genommen werden, dann kann man auch die einzelnen Klassen weglassen
import json, raetsel as r
import display
import random

scenes = [["arctic.json", "atlantis.json"],
          ["pyramid.json", "swamp.json"]]


#temperature = float(input("Temperatur: "))
#humidity = float(input("Luftfeuchtigkeit: "))

# für Demozwecke
temperature = random.random() * 100
humidity = random.random() * 100

# schwellwerte, an denen es von 0 zu 1 ändert
temp_switch = 20.0
hum_switch = 20.0

if temperature > temp_switch:
    temperature = 1
else:
    temperature = 0

if humidity > hum_switch:
    humidity = 1
else:
    humidity = 0


cur_scenario = scenes[temperature][humidity]

print(cur_scenario)

puzzles = []    # enthält alle Rätsel in dem Szenario

with open(cur_scenario, "r") as file:
    # Liste aller Rätsel in der Datei
    data = json.load(file)['raetsel']

    for raetsel in data:

        puzzles.append(r.Puzzle(raetsel))

        # print(r1)

cur_puzzle = 0

while cur_puzzle < len(puzzles):
    if puzzles[cur_puzzle].puzzle_ask():
        cur_puzzle += 1
    
