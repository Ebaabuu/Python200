# @author Emaad Gafoor
def main():
    countyNames = ["Chase", "Crawford", "Ford", "Harper", "Kiowa", 
                   "McPherson", "Norton", "Republic", "Shawnee", "Wabaunsee"]
    
    countySeats = ["Cottonwood Falls", "Girard", "Dodge City", "Anthony", 
                   "Greensburg", "McPherson", "Norton", "Belleville", 
                   "Topeka", "Alma", ]
    
    countyPops = [2572, 38972, 34287, 5485, 2460, 
                  10038, 5459, 4674, 178909, 6877]
      
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty to insert: ").title()
    seat = input(f"{name} County seat: ")
    pop = int(input(f"{name} County population (digits only): "))
    
    ## ADD CODE 1
    indexForNewValue = findInsertionIndex(countyNames, name)
    countyNames.insert(indexForNewValue, name)
    countySeats.insert(indexForNewValue, seat)
    countyPops.insert(indexForNewValue, pop)

    print()  
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty requiring population adjustment: ").title()
    
    ## ADD CODE 2
    indexForInsertedValue = linearSearch(countyNames, name)
    if indexForInsertedValue >= 0:
        print(f"Current population: {countyPops[indexForInsertedValue]:,}")
        countyPops[indexForInsertedValue] = int(input(
            "New population (digits only): "))
    else:
        print(f"{name} County not found")
    

    print()    
    showCountyData(countyNames, countySeats, countyPops)


# showCountyData displays the data for the given counties
# @param countyNames The list of county names
# @param countySeats The list of county seats
# @param countyPops The list of county populations
def showCountyData(countyNames, countySeats, countyPops):
    for i in range(len(countyNames)):
        print(f"{countyNames[i]} County")
        print(f"  Seat: {countySeats[i]}")
        print(f"  Population: {countyPops[i]:,}")
        
# linearSearch searches for a given value in a list
# @param theList The list to search
# @param target The value to match
# @return The index of value if found or -1 if not found.
def linearSearch(theList, target) :
    for i in range(len(theList)) :
        if theList[i] == target :
            return i
    return -1


# findInsertionIndex finds the index where value is to be 
# inserted into the list
# @precondition The list of values is in increasing sorted order
# @param theList the list of values
# @param value The value to insert
# @return The located index
def findInsertionIndex(theList, value):
    counter = 0
    for i in theList:
        if value > i:
            counter += 1
    return counter

main()