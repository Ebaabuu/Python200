# @author Emaad gafoor
def main():
     with open("KansasCountyData.txt", "r") as inFile:
          # Skip file header
          inFile.readline()
          
          # Compute the total population for Kansas as well as find
          # the smallest county
          totalPopulation = 0
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
     print(f"Kansas Population: {totalPopulation:,}")
     print(f"{smallestCounty} is the smallest county with "
           f"{smallestPopulation:,} residents")
    
main()