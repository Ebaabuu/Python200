import random

def main():
    # Create a new empty dictionary that is assigned to a variable
    # named stateCaps
    stateCaps = {}
    
    # Fill stateCaps by calling getStateCaps with 
    # a file named StateCaps.txt and the dictionary
    getStateCaps("StateCaps.txt", stateCaps)
    
    # Loop to display the current states and their capitals
    # Match the output shown in the requirements
    for state in stateCaps:
        print(f"The capital of {state} is {stateCaps[state]}")
    
    # Prompt for and retrieve a new state and capital and then
    # place into the dictionary.
    # Match the prompts shown in the requirements
    state = input("\nEnter a new state: ")
    capital = input(f"Enter the capital of {state}: ")
    stateCaps[state] = capital
    
    # Display the states and their capitals sorted by state
    # Match the output shown in the requirements
    print()
    for state in sorted(stateCaps.keys()):
        print(f"The capital of {state} is {stateCaps[state]}")
        
    # Create a list named states that consists of only the states (keys)
    states = list(stateCaps.keys())
    
    # Uncomment the following statement as it will select a random 
    # state from the states list. 
    state = random.choice(states)
    
    # Display a question "What is the capital of <state>? " Where <state> is
    # replaced by the random state just selected.
    # Match the prompt shown
    capital = input(f"\nWhat is the capital of {state}? ")
    
    # Display whether or not the capital entered by the user is correct
    # If incorrect also state the name of the capital.
    # Match the output shown
    if capital == stateCaps[state]:
        print("Correct!")
    else:
        print(f"Incorrect. The capital is {stateCaps[state]}")
        
    # Call storeStesCaps to write the stateCaps dictionary back to the 
    # file named StateCaps.txt. 
    storeStateCaps("StateCaps.txt", stateCaps)
    
    print("Data file modified.")
    
    
# getStateCaps retrieves pairs of states and their capitals from file
# The assumed file format for each line is:
# State=Capital
# @param filename The name of the file to read
# @param stateCaps Empty dictionary that will store the state/capital pairs
def getStateCaps(filename, stateCaps) :
    inFile = open(filename, "r")
    
    for line in inFile :
        line = line.rstrip()
        (state, capital) = line.split("=")
        stateCaps[state] = capital
    
    inFile.close()
    
# storeStateCaps writes pairs of states and their capitals to file where each
# line is of the form, State=Capital
# @param filename The name of the file to write
# @param stateCaps Dictionary containing the state/capital pairs
def storeStateCaps(filename, stateCaps) :
    outFile = open(filename, "w")
    for (state, cap) in stateCaps.items():
        outFile.write(f"{state}={cap}\n")
    outFile.close()
        
main()