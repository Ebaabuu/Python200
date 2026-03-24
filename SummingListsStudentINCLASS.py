# @author Emaad Gafoor
from random import randint
def main() :
    LOW = 1
    HIGH = 5
    LIST_SIZE = 10
    
    # INSERT code to create two empty lists named list1 and list2
    list1 = []
    list2 = []
    
    # INSERT code to loop LIST_SIZE times to append different random 
    # numbers in the range [LOW, HIGH] to list1 and to list2.
    # This is done in the same loop (NOT two separate loops)
    for i in range(LIST_SIZE):
        list1.append(randint(LOW,HIGH))
        list2.append(randint(LOW,HIGH))
        

    # INSERT code to show the data in each list by simply printing the 
    # list name. Match the output with a heading of List1: and List2:
    # (No need to loop)
    print(f"List1: {list1}")
    print(f"List1: {list2}")
 
    # INSERT code to create a third list named listSum that is the
    # same size as list1 and list2. It's values are initialized to 0
    listSum = [0] * LIST_SIZE
    
    # INSERT a loop to place the sum of each pair of elements in list1 and
    # list2 into listSum. append will not be used -- instead use an index
    # Example: list1    -> [5, 1, 2, 4, 3, 5, 4]
    #          list2    -> [4, 2, 2, 4, 1, 4, 3]
    #          listSum ->  [9, 3, 4, 8, 4, 9, 7]
    for i in range(LIST_SIZE):
        listSum[i] = list1[i] + list2[i]
    
    # Display Sum: and the contents of listSum by simply printing the name
    print(f"Sum: {listSum}")

main()