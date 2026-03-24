from Item import Item
tent = Item("Tent", 79.99)
flashlight = Item("Flashlight", 25)
print(tent)
print(flashlight)

tent.setPrice(-30)
print(tent)

item = Item()
print(item)
item.setName("Sleeping Bag").setPrice(67.50)
print(item)