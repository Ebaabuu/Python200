# This program outputs a season given a user-entered month.
# @author Emaad Gafoor

def main():
    print("Enter a numeric month and I will display the season.")
    again = "Y"
    while (again == "Y"):
        # Get the month
        month = int( input("Month: ") )
        displaySeason(month)
        print()
        
        # Enter another month?
        again = "-"
        while (again not in "YyNn"):
            again = input("Enter another month (Y or N)? ").upper()
    print("Have a good day!")
 
# displaySeason displays the season corresponding to a given numeric month
# @param month The given numeric month
def displaySeason(month):
    if ( month in [1, 2, 12]):
        print("winter")
    elif ( 3 <= month <= 5 ):
        print("spring")
    elif ( 6 <= month <= 8 ):
        print("summer")
    elif ( 9 <= month <= 11 ):
        print("fall")
    else:
        print("I'm sorry, an invalid month was entered.")    

main()