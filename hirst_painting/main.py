import colorgram as cg

color_list = []
for color in cg.extract("hirst.jpg", 30):
    color_list.append(tuple(color.rgb))

print(color_list)
