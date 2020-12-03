# wenn Pfade genommen werden, dann kann man auch die einzelnen Klassen weglassen
import arctic, pyramid, swamp, atlantis 

# das ist sehr sinnfrei.
# TODO: ändern in Pfade
# z.B. scenes = [["pfad/zu/arctic.json", "pfad/zu/atlantis.json"] ... ]
scenes = [[arctic.Arctic(), atlantis.Atlantis()],
          [pyramid.Pyramid(), swamp.Swamp()]]


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

