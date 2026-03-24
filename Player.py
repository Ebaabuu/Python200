from Person import Person

class Player(Person):
    def __init__(this, name = "", numWins = 0):
        super().__init__(name)
        this.setNumWins(numWins)
    
    def setNumWins(this, newNumWins):
        this.numWins = newNumWins
        
    def getNumWins(this):
        return this.numWins
    
    def __str__(this):
        return f"Name: {this.getName()}\n  Wins: {this.getNumWins()}"