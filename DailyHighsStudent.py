# @author Emaad Gafoor
# This program allows a user to process daily high tempuratures froma file 
# in a standard format. Each line in the file is of the format: MonthName, 
# day1High, day2High, ..., dayNHigh
import sys

def main():
    # Create empty lists named dailyHighs and months
    dailyHighs = []
    months = []

    # Call getDailyHighs with "2022DailyHighsKC.csv" and the lists.
    # To test a different file, 2022DailyHighsKC-Partial.csv may also be used.
    getDailyHighs("2022DailyHighsKC.csv", months, dailyHighs)
    EXIT = "5"
    choice = "0"
    # Present user with menu choices until they decide to exit
    while (choice != EXIT):

        choice = getMenuChoice()
        print()
        
        # Process each menu choice
        if (choice == "1"): 
            # See the description/requirements document for the code to insert
            # to get the value for monthIndex
            monthIndex = -1
            while monthIndex < 0:
                month = input("Month? ")
                try:
                    monthIndex = months.index(month)
                except:
                    print(f"{month} not recognized.")
            
            # Call getAverageHigh and display the returned average to 1 digit
            # of precision followed by F. Precede this with a header
            # of "Average High: ". See the sample runs.
            averageHigh = getAverageHigh(monthIndex, dailyHighs)
            print(f"Average High: {averageHigh:.1f}F")
            
        elif (choice == "2"):
            print("Show temperatures within what range? ")
            low = int(input("Lower bound: "))
            high = int(input("Upper bound: "))
            # Insert a call to showTempsInRange
            showTempInRange(low, high, dailyHighs, months)
            
        elif (choice == "3"):
            overUnder = int(input("Over/Under temperature? "))
            # Insert code to get the tuple returned from a call to getOverUnder.
            # Then, display the tuple data in the format shown
            under, equal, over = getOverUnder(overUnder, dailyHighs)
            print(f"There are temperatures {under} below, {equal} equal to," + 
                  f" and {over} above {overUnder}F.")
            
        elif (choice == "4"):
            filename = input("Name of file to create? ")
            # If the filename does not end with .html or .htm then concatenate
            # (apppend) .html to the file name. Hint: use the endsWith method
            # to determine if it ends with .html or .htm
            # Then, insert a call to createWebPageStats with the filename
            if not (filename.endswith(".html") or (filename.endswith(".htm"))):
                filename += ".html"
            createWebPageStats(filename, months, dailyHighs)  
        print()

# getMenuChoice presents and menu and gets the user's choice
# @return choice The user's choice
def getMenuChoice():
    print("(1) Show average daily high for a given month.")
    print("(2) Show daily high temperatures within a given range.")
    print("(3) Show over/under statistics for a given temperature.")
    print("(4) Store statistics as Web page.")
    print("(5) Exit.")
    choice = input("Choice? ")
    return choice
    

# getDailyHighs reads temperature data from a file in a specified format.
# Each line (record) consists of the month name followed by the highs for
# each day in the month. All fields in the record are comma-separated.
# @param filename The name of the file from which temperatures are read
# @param months An empty list to be filled with months
# @param dailyHighs An empty list that will become a two-dimensonal list.
#                   Each row will hold a list of temperatures for a month.
def getDailyHighs(filename, months, dailyHighs):
    try:
        inFile = open(filename, "r")
        for line in inFile:
            line = line.rstrip()
            line = line.split(",")
            months.append(line[0])
            dailyHighs.append(line[1:])
        inFile.close()
                    
    except Exception as exc:
        print(exc)
        print("Application Exit")
        if ("inFile" in locals()):
            inFile.close()        
        sys.exit()
            
    for i in range(len(dailyHighs)):
        for j in range(len(dailyHighs[i])):
            try:
                dailyHighs[i][j] = int(dailyHighs[i][j])
            except Exception as exc:
                print(exc)
                print("Application Exit")
                sys.exit()

# getAverageHigh determines the average daily high for a given month
# @param monthIndex The index of the given month
# @param dailyHighs A two-dimensional list of annual temperatures
# @return The average daily high
def getAverageHigh(monthIndex, dailyHighs):
    average = sum(dailyHighs[monthIndex])/len(dailyHighs[monthIndex])
    return average

# showTempInRange shows temperatures lying within a given range in
# a table format.
# @param lowerBound The inclusive lower bound for the temperatures
# @param upperBound The inclusive upper bound for the temperatures
# @param dailyHighs A two-dimensional list of annual temperatures
# @param months A list containing the months.
def showTempInRange(lowerBound, upperBound, dailyHighs, months):
    print(f"{'Day':<10}", end = "")
    for i in range(1,32):
        print(f"{i:>3}", end="")
    print()
    for row in range(len(dailyHighs)):
        print(f"{months[row]:<10}", end = "")
        for col in range(len(dailyHighs[row])):
            if lowerBound <= dailyHighs[row][col] <= upperBound: 
                print(f"{dailyHighs[row][col]:>3}", end = "")
            else:
                print(f"{'*':>3}", end = "")
        print()

# getOverUnder counts the number of temperatures below, equal to, and
# above a given temperature
# @param overUnder The over/under value that splits the counts
# @param dailyHighs A two-dimensional list of annual temperatures
def getOverUnder(overUnder, dailyHighs):
    totalUnder = 0
    totalEqual = 0
    totalOver = 0
    for row in dailyHighs:
        for col in row:
            if col > overUnder:
                totalOver += 1
            elif col < overUnder:
                totalUnder += 1
            else:
                totalEqual += 1
    return (totalUnder, totalEqual, totalOver)

# createWebpageStats stores each month with its lowest high and highest high
# to a Web page file
# @param filename The name of the file
# @param months A list containing the months. 
# @param dailyHighs A two-dimensional list of annual temperatures 
def createWebPageStats(filename, months, dailyHighs):
    ROW_COLORS = ("lightsteelblue", "beige") # Use different colors if desired.
    PAGE_BEGIN = '<html>\n' + \
        '<head>\n' + \
        '    <meta charset="utf-8">\n' + \
        '    <title>2022 Temperatures</title>\n' + \
        '</head>\n' + \
        '<body>\n' + \
        '<table style = "border-spacing:1px;">\n' + \
        '  <tr style = "background-color:lightgray">\n' + \
        '    <td>Month</td>\n' + \
        '    <td>Lowest Daily High</td>\n' + \
        '    <td>Highest Daily High</td>\n' + \
        '  </tr>\n'
    
    # Insert code to open filename for writing, and then write PAGE_BEGIN to
    # that file
    outFile = open(filename,"w")
    outFile.write(PAGE_BEGIN)
    
    # Insert one loop that processes one month (one row in the html table)
    # each iteration. See the discussion in the description/requirements doc
    for i in range(len(dailyHighs)):
        lowestDailyHigh = min(dailyHighs[i])
        highestDailyHigh = max(dailyHighs[i])
        
        color = ROW_COLORS[i % 2]
        
        outFile.write(f' <tr style = "background-color:{color};text-align:center;">\n' + \
                      f' <td>{months[i]}</td>\n' + \
                      f' <td>{lowestDailyHigh}</td>\n' + \
                      f' <td>{highestDailyHigh}</td>\n' + \
                      ' </tr>\n')

    # Insert code to write PAGE_END to file. Then, close the file and display
    # to the user that the file was created. You will need to output the name
    # of the file when mathching the output.
    PAGE_END = '</table>\n</body>\n</html>'
    print(f"{filename} created.")
    outFile.close()
    
main()