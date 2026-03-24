# @author Emaad Gafoor
from random import randint

def main():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    low = int(input("Lowest potential value: "))
    high = int(input("Highest potential value: "))    
    
    matrix = getTable(rows, cols)
#    displayMatrix(matrix)
#    print()
    fillMatrix(matrix, low, high)
    displayMatrix(matrix)
    
    highestRow = findHighest(matrix)[0]
    highestCol = findHighest(matrix)[1]
    print(f"The highest value is {matrix[highestRow][highestCol]}" + 
          f" and is located at [{highestRow}][{highestCol}]")

# getTable creates a rows x cols table initialized to 0's
# @param rows The number of rows
# @param cols The number of columns
# @return the rectangular table
def getTable(rows, cols):
    table = []
    for row in range(rows):
        nextRow = [0] * cols
        table.append(nextRow)
    return table

# displayMatrix displays a matrix in table format with a cell width of 4
# @param matrix The matrix to display
def displayMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]:4d}", end = "")
        print()    

# fillMatrix fills a matrix with random integers in the range -10 through 10
# @param matrix The matrix to fill
# @param low The lowest allowed value
# @param high The highest allowed value
def fillMatrix(matrix, low, high):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = randint(low, high)

def findHighest(matrix):
    rowIndex = 0
    colIndex = 0
    highestValue = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > highestValue:
                highestValue = matrix[row][col]
                rowIndex = row
                colIndex = col
    return (rowIndex, colIndex)

main()