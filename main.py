import arctic, pyramid, swamp, atlantis

scenes = [[arctic.Arctic(), atlantis.Atlantis()],
          [pyramid.Pyramid(), swamp.Swamp()]]


temperature = float(input("Temperatur: "))
humidity = float(input("Luftfeuchtigkeit: "))

if temperature > 20.0:
    temperature = 1
else: 
    temperature = 0

if humidity > 20.0:
    humidity = 1
else: 
    humidity = 0


cur_scenario = scenes[temperature][humidity]

print(cur_scenario)

