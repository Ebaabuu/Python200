# @author Emaad Gafoor

# Get the for loop values
start = int(input("Starting integer: "))
ending = int(input("Ending integer: "))
stepSize = int(input("Step Size: "))

if ( (ending < start and stepSize  > 0) or
     (ending > start and stepSize < 0)):
    print("Invalid step size.")
else:
    # Display the sequence generated
    for i in range(start, ending, stepSize):
        print(i, end = " ")
