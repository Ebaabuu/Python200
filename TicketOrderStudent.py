# @author Emaad Gafoor

class TicketOrder:
    def __init__(self, custId = "", numTickets = 0, pricePerTicket = 0):
        self.setId(custId)
        self.setNumTickets(numTickets)
        self.setPricePerTicket(pricePerTicket)
        
    def setId(self, newCustId):
        self.custId = newCustId
    def getId(self):
        return self.custId
    
    def setNumTickets(self, newNumTickets):
        self.numTickets = newNumTickets
    def getNumTickets(self):
        return self.numTickets

    def setPricePerTicket(self, price):
        self.pricePerTicket = price
    def getPricePerTicket(self):
        return self.pricePerTicket
    
    def getOrderCost(self):
        return self.getNumTickets() * self.getPricePerTicket()
        
    def __str__(self):
        return f"{self.getId()},{self.getNumTickets()},${self.getPricePerTicket():,.2f}"
