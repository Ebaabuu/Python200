# @author First Last
import csv

def main():
    with open("KansasCountyData.csv", "r") as inFile:
        # Skip file header
        inFile.readline()
        
        # Compute the total population for Kansas as well as find
        # the smallest county
        (smallestCounty, seat, population) = inFile.readline().split(",")
        totalPopulation = smallestPopulation = int(population)
        for countyData in inFile:
            (name, seat, population) = countyData.split(",")
            countyPopulation = int(population)
            totalPopulation += countyPopulation
            if countyPopulation < smallestPopulation:
                smallestCounty = name
                smallestPopulation = countyPopulation
            
    # Display the total population and the smallest county
    with open("KansasSummary.txt", "w") as outFile:
        outFile.write(f"Kansas Population: {totalPopulation:,d}\n")
        outFile.write(f"{smallestCounty} is the smallest county with "
              f"{smallestPopulation:,d} residents\n")
        
    print("KansasSummary.txt created")
    
    
def mainWithCSV():
    with open("KansasCountyData.csv", "r") as inFile:
        csvReader = csv.reader(inFile, delimiter = ",")
        # Skip file header
        next(csvReader)
        
        # Compute the total population for Kansas as well as find
        # the smallest county
        (smallestCounty, seat, population) = next(csvReader)
        totalPopulation = smallestPopulation = int(population)
        for (name, seat, population) in csvReader:
            # (name, seat, population) = \
            #     countyData[0], countyData[1], countyData[2]
            countyPopulation = int(population)
            totalPopulation += countyPopulation
            if countyPopulation < smallestPopulation:
                smallestCounty = name
                smallestPopulation = countyPopulation
            
    # Display the total population and the smallest county
    with open("KansasSummary.txt", "w") as outFile:
        outFile.write(f"Kansas Population: {totalPopulation:,d}\n")
        outFile.write(f"{smallestCounty} is the smallest county with "
              f"{smallestPopulation:,d} residents\n")
        
    print("KansasSummary.txt created")
    
mainWithCSV()