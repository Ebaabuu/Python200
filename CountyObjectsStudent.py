# The program allows a user to query information about counties
# in a given state.
# @author Emaad Gafoor

# Insert the required import statement
from County import County

def main(): # main is completed and may not be modified
    counties = []
    
    # Get the state
    state = input("Get county data for which state: ")
    getCountyData(state, counties)
    
    # Contine to allow the user to process statistical information.
    EXIT = "4"
    choice = "0"
    while (choice != EXIT):
        print("(1) Show statistical summary")
        print("(2) Show counties within a given population range")
        print("(3) Show counties beginning with a certain letter")
        print("(4) Exit")
        choice = input("Choice? ")
        
        if (choice == "1"):
            showStatSummary(state, counties)
        elif (choice == "2"):
            print("Show counties with what population range? ")
            low = int(input("Lower bound: "))
            high = int(input("Upper bound: "))
            showPopulationRange(low, high, counties)
        elif (choice == "3"):
            letter = input("Show counties beginning with which letter? ")          
            showCountySubset(letter.upper(), counties)
        print()

# getCountyData reads county data from a given state's file.
# @param state The name of the state for which data is to be read
# @param counties Will be filled with County objects that hold a name,
# seat, and population
def getCountyData(state, counties):
    fileName = state + "CountyData.txt"
    try:
        inFile = open(fileName, "r")
        inFile.readline() # Skip Header Line
        for line in inFile:
            line = line.rstrip().split(",")
            countyData = County(line[0], line[1], int(line[2]))
            counties.append(countyData)
        inFile.close()
            
    except Exception as exc:
        if "inFile" in locals():
            inFile.close()
        print(exc)
        exit()

# showStatSummary displays the state population, the number of counties, and
# the average county population.
# @param state The name of the state
# @param counties A list of county objects for a state
def showStatSummary(state, counties): # (3)
    totalCounties = len(counties)
    # Insert code to compute the total population that is stored into a
    # variable named totalPopulation
    totalPopulation = 0
    for i in range(totalCounties):
        totalPopulation += counties[i].getPopulation()
    
    print(f"Statistics for {state}:")
    print(f"State population: {totalPopulation:,d}")
    print(f"Number of counties: {totalCounties:,d}")
    print("Average county population: " + 
          f"{totalPopulation/totalCounties:,.0f}")

# showPopulationRange shows county information for those county populations
# within a given population range.
# @param lowerBound The inclusive lower bound for the range
# @param upperBound The inclusive upper bound for the range
# @param counties A list of County objects for a state    
def showPopulationRange(lowerBound, upperBound, counties):
    for county in counties:
        if lowerBound < county.getPopulation() < upperBound:
            print(county)

# showCountySubset shows county information for those county names
# beginning with a given letter. 
# @param letter The first letter to match
# @param counties A list of County objects for a state
def showCountySubset(letter, counties):
    for county in counties:
        if county.getName()[0] == letter.upper():
            print(county)

main()