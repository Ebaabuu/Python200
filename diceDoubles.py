# @author Emaad Gafoor
from random import randint
NUM_DIE_SIDES = 6

# Get the number of dice rolls
diceRolls = int(input("Enter the number of dice rolls: "))

# Roll the dice and both count and display the number of doubles
numDoubles = 0
for i in range(diceRolls):
    # Generate and store two dice values
    die1 = randint(1, NUM_DIE_SIDES)
    die2 = randint(1, NUM_DIE_SIDES)
    
    # Display the dice and how if/how many doubles there are
    print(f"{die1}, {die2}", end = "")
    if die1 == die2:
        numDoubles += 1
        print(" Double!", end = "")
    print()
    
# Display the number of doubles rolled
print(f"\n{numDoubles} double(s) rolled.")