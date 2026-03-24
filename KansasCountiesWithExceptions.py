# @author First Last
import sys
import csv

def main():
    # Open the file and skip the header
    inFile = open("KansasCountyData.txt", "r")
    inFile.readline()
    
    # Determine the total population
    totalPopulation = 0
    smallestCounty = ""
    smallestCountyPopulation = sys.maxsize 
    for line in inFile:
        countyData = line.split(",")
        totalPopulation += int(countyData[2])
        
        # Check if lower population
        if (int(countyData[2]) < smallestCountyPopulation):
            smallestCounty = countyData[0]
            smallestCountyPopulation = int(countyData[2])
    inFile.close()
    
    # Store the total population
    outFile = open("KansasTotalPopulation.txt", "w")
    outFile.write(f"Kansas population: {totalPopulation:,d}\n")
    outFile.write(f"{smallestCounty} is the smallest county with "
                  f"{smallestCountyPopulation:,d} residents")
    outFile.close()


def mainWithCsv():
    try:
        # Open the file and skip the header
        with open("KansasCountyData.txt", "r") as inFile:
            csvReader = csv.reader(inFile, delimiter = ",")
            next(csvReader)
        
            # Determine the total population
            totalPopulation = 0
            smallestCounty = ""
            smallestCountyPopulation = sys.maxsize
            for line in csvReader:
                totalPopulation += int(line[2])
            
                # Check if lower population
                if (int(line[2]) < smallestCountyPopulation):
                    smallestCounty = line[0]
                    smallestCountyPopulation = int(line[2])
    except Exception as exc:
        if "inFile" in locals():
            inFile.close()
        print(exc)
        sys.exit()
    
    # Store the total population
    with open("KansasSummary.txt", "w") as outFile:
        outFile.write(f"Kansas population: {totalPopulation:,d}\n")
        outFile.write(f"{smallestCounty} is the smallest county with "
                      f"{smallestCountyPopulation:,d} residents")
    print("File processing complete")
mainWithCsv()
