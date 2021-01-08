# wenn Pfade genommen werden, dann kann man auch die einzelnen Klassen weglassen
import json, raetsel as r

scenes = [["arctic.json", "atlantis.json"],
          ["pyramid.json", "swamp.json"]]


temperature = float(input("Temperatur: "))
humidity = float(input("Luftfeuchtigkeit: "))

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

with open(cur_scenario, "r") as file:
    # Liste aller Rätsel in der Datei
    data = json.load(file)['raetsel']

    for raetsel in data:

        r1 = r.Puzzle(raetsel)

        print(r1)
    
