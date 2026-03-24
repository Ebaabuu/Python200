# @author Emaad Gafoor

from random import randint
def main():
    MAX_LIST_SIZE = 20
    LOW_VALUE = 1
    HIGH_VALUE = 50
    
    ## ADD CODE #1
    listSize = 0
    while (listSize > MAX_LIST_SIZE or listSize < 1):
        listSize = int(input(f"List size (1 - {MAX_LIST_SIZE:d})? "))
    
    ## ADD CODE #2
    data = []
    for i in range(listSize):
        data.append(randint(LOW_VALUE, HIGH_VALUE))
    
    ## ADD CODE #3
    data.sort()
    
    ## ADD CODE #4
    for i in data:
        print(i, end = " ")
    print()
    
    # Get an upper and lower bound for a range to display COMPLETED
    print("\nDisplay all values between what inclusive range?")
    lower = int(input("Lower bound: "))
    upper = int(input("Upper bound: "))
    
    ## ADD CODE #5
    for i in data:
        if i <= upper and i >= lower:
            print(i, end = " ")
main()