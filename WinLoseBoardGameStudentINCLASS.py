from random import randint
def main():
    NUM_ROWS_COLS = 10
    board = []
    addDimensions(board, NUM_ROWS_COLS)
    
    # Establish the win probability
    winProbability = int(input("Probability of winning (10 - 90)? "))
    setBoard(board, winProbability)

    # Get the row and column location
    row = int(input(f"Winning row location (1 - {NUM_ROWS_COLS}): "))
    col = int(input(f"Winning column location (1 - {NUM_ROWS_COLS}): "))
    
    # Display whether or not the game was won (ADD CODE)
    if board[row - 1][col - 1] == "W":
        print("Winner!")
    else:
        print("Loser!")
    
    displayBoard(board)
    
# addDimensions creates storage for a rows x cols game board initialized to L's
# @param board The location of the board
# @param numRowsCols The number of rows and columns for a square board
def addDimensions(board, numRowsCols):
    for row in range(numRowsCols):
        nextRow = ["L"] * numRowsCols
        board.append(nextRow)


# displayBoard displays a game board
# @param board The board to display
def displayBoard(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f"{board[row][col]:2s}", end = "")
        print()    

# setBoard places W's into random board squares (cells) based upon the
# probability of wins sent
# @param board The game board to fill
# @param winProbability Percentage of the board that will contains W's
# @precondition Each board cell currently contains an L
def setBoard(board, winProbability):
    numWins = 0
    totalWins = winProbability / 100 * (len(board) * len(board[0]))
    
    # Put the W's into the board
    while (numWins < totalWins):
        row = randint(0,len(board) - 1)
        col = randint(0,len(board[0]) - 1)
        if (board [row][col] == "L"):
            board[row][col] = "W"
            numWins += 1

main()
