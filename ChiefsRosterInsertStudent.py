# @author Emaad Gafoor

def main():
    roster = getRoster()
    name = input("New player last name: ")
    index = findInsertionIndex(roster, name)
    
    # Insert the name into the list at the given index
    roster.insert(index, name)
    
    showRoster(roster)
    
# getRoster creates a list of KC Chiefs Roster names
# @return the list of names
def getRoster():
    roster = ["Allegretti","Anudike-Uzomah","Bell","Bolton","Butker",
              "Caliendo","Chenal","Coburn","Cochrane","Conner",
              "Cook","Danna","Dickerson","Edwards","Edwards-Helaire",
              "Farrell","Gabbert","Gay","Gray","Herring",
              "Humphrey","Jones-Cam","Jones-Chris","Jones","Karlaftis",
              "Kelce","Mahomes","McDuffie","McKinnon","Moore",
              "Morris","Niang","Nnadi","Pacheco","Reid",
              "Rice","Ross","Smith","Smith","Sneed",
              "Taylor","Thompson","Thuney","Toney","Townsend",
              "Tranquill","Valdes-Scantling","Washington","Watson-Jaylen",
              "Watson-Justin","Wharton","Williams","Winchester"]
    return roster

# findInsertionIndex finds the index where value is to be inserted
# into the list.
# @precondition The list of values is in increasing sorted order
# @param theList The list of values
# @param value the value to insert
# @return the located index
def findInsertionIndex(theList, value):
    """
    i = 0
    while (i < len(theList) and value > theList[i]):
        i += 1
    """
    for i in range(len(theList)):
        if value <= theList[i]:
            return i
    return len(theList)

# showRoster displays roster names in a column format
# @param roster The player roster
def showRoster(roster):
    NAMES_PER_LINE = 4
    nameCounter = 0
    for name in roster:
        nameCounter += 1
        print(f"{name:18s}", end = "")
        if nameCounter % NAMES_PER_LINE == 0:
            print()

main()