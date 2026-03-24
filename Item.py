# Class Item represents an item with a name and a price
# @author Emaad Gafoor
class Item:
    def __init__(self, newName = "", newPrice = 0):
        self.setName(newName)
        self.setPrice(newPrice)
    
    def setName(self, newName):
        self.name = newName
        return self
    def getName(self):
        return self.name
    
    def setPrice(self, newPrice):
        self.price = newPrice if newPrice > 0 else 0
        return self
    def getPrice(self):
        return self.price
    
    def __str__(self):
        return f"Name: {self.getName()}, Price: ${self.getPrice():,.2f}"
        
if __name__ == "__main__":
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