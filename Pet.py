# @author Emaad Gafoor

class Pet:
    def __init__(self, newName = "", newWeight = 0):
        self.setName(newName)
        self.setWeight(newWeight)
        
    def setName(self, newName):
        self.name = newName
        return self
    def getName(self):
        return self.name
    
    def setWeight(self, newWeight):
        if newWeight > 0:
            self.weight = newWeight
        else:
            self.weight = 0
        # self.weight = newWeight if newWeight > 0 else 0
        
        return self
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return f"Name: {self.getName()}, Weight: {self.getWeight():.1f} lbs"