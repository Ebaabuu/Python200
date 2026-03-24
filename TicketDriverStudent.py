# @author Emaad Gafoor
from TicketOrderStudent import TicketOrder

def main(): # MAIN MAY NOT BE MODIFIED -- except for the filename
    SERVICE_FEE_PER_TICKET = 0.25
    orders = getOrders("ticketOrders2.txt") # May change to ticketOrders2.txt
    print(f"Number of orders: {len(orders)}")
    print(f"Average cost per order: ${getAverageCostPerOrder(orders):,.2f}")
    print(f"Most expensive order:\n{getMostExpensiveOrder(orders)}")
    processServiceFee(orders, SERVICE_FEE_PER_TICKET)
    print("Orders after processing fee added: ")
    showOrders(orders)

# COMPLETED (may not be modifed)
# showOrders displays each ticket order on separate lines
# @param orders A list of ticket orders
def showOrders(orders):
    for order in orders:
        print(order)
        
# Define function getOrders here
def getOrders(filename):
    listOrders = []
    inFile = open(filename, "r")
    inFile.readline()
    for line in inFile:
        line = line.split(",")
        listOrders.append(TicketOrder(line[0], int(line[1]), float(line[2])))
    return listOrders

# Define function getAverageCostPerOrder here
def getAverageCostPerOrder(orders):
    totalCost = 0
    for order in orders:
        totalCost += order.getOrderCost()
    return totalCost / len(orders)


# Define function processServiceFee here
def processServiceFee(orders, serviceFee):
    for i in range(len(orders)):
        orders[i].setPricePerTicket(orders[i].getPricePerTicket() + serviceFee)

# Define function getMostExpensiveOrder here
def getMostExpensiveOrder(orders):
    highest = 0
    for i in range(len(orders)):
        if orders[i].getOrderCost() > orders[highest].getOrderCost():
            highest = i
    return orders[highest]

main()