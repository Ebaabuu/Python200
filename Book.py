# @author Emaad Gafoor
# Class Book represents a book with a number of pages
from Item import Item
class Book(Item):
    def __init__(this, newName = "", newPrice = 0, newNumPages = 0):
        super().__init__(newName, newPrice)
        this.setNumPages(newNumPages)
        
    def setNumPages(this, newNumPages):
        this.numPages = newNumPages if newNumPages > 0 else 0
        
    def getNumPages(this):
        return this.numPages
    
    def __str__(this):
        return f"{super().__str__()}, Number of Pages: {this.getNumPages()}"