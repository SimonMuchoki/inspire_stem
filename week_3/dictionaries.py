# dictionaries are key value pairs that are muteable uses curly bracets
#key value pair


my_laptop = {"make":"HP","color":"grey","weight":"1.2","year":"2023"}

my_laptop["color"] = "red"
my_laptop["year"] = "2019"


for key,value in my_laptop.items():
          print(key)
          print(value)
          print("\t")

print(my_laptop["make"])
print(my_laptop["color"])
print(my_laptop["year"])


my_laptop["size"] = "600mm x 700mm"
print(my_laptop)

del my_laptop["color"]
print(my_laptop)


siz_laptop = my_laptop.copy
print(siz_laptop)


