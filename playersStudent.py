# @author Emaad Gafoor
from Player import Player

#Simple Test Driver (Completed)
def main():
    print("Default player test")
    defaultPlayer = Player()
    print(defaultPlayer)

    players = readData("players.txt")
    print("\nTest showHighWins with a default limit")
    showHighWins(players)

    print("\nTest showHighWins with a limit of 5")
    showHighWins(players, 5)

    print("\nTest reset")
    reset(players)
    showHighWins(players)   


# readData creates a list of players from a given file
# @param filename The file creating the players
# @return A list of players
def readData(fileName):
    players = []
    inFile = open(fileName, "r");

    for line in inFile:
        line = line.rstrip()
        (name, numWins) = line.split(",")

        # Add code to append a Player object with the above data to
        # above data to the players list
        players.append(Player(name, int(numWins)))


    inFile.close()

    # Add code to return the list of players
    return players

# showHighWins displays players with a given number of wins or greater
# @param players The list of players
# @param lowNumWins Display all wins >= lowNumWins. Default is 0   
def showHighWins(players, lowNumWins = 0):
    for player in players:
        if player.getNumWins() >= lowNumWins:
            print(player)

# reset sets the wins of all players to 0
# @param players The list of players   
def reset(players):
    for player in players:
        player.setNumWins(0)

main()