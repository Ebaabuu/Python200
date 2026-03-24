# @author Emaad Gafoor
# Creates a County object to store a county's name, seat, and population
class County:
    def __init__(this, newName = "", newSeat = "", newPopulation = 0):
        this.setName(newName)
        this.setSeat(newSeat)
        this.setPopulation(newPopulation)
        
    def setName(this, newName):
        this.name = newName
        return this
    def getName(this):
        return this.name
    
    def setSeat(this, newSeat):
        this.seat = newSeat
        return this
    def getSeat(this):
        return this.seat
    
    def setPopulation(this, newPopulation):
        this.population = newPopulation
        return this
    def getPopulation(this):
        return this.population
    
    def __str__(this):
        return f"{this.getName()},{this.getSeat()},{this.getPopulation()}"