# This program outputs a season given a user-entered month.
# @author First Last

again = "Y"
while (again == "Y"):
    
    # Get the month
    print("Enter a numeric month and I will display the season.")
    month = int( input("Month: ") )
    
    # Display corresponding season
    if ( month == 12 or month == 1 or month == 2 ):
        print("winter")
    elif ( 3 <= month <= 5 ):
        print("spring")
    elif ( 6 <= month <= 8 ):
        print("summer")
    elif ( 9 <= month <= 11 ):
        print("fall")
    else:
        print("I'm sorry, an invalid month was entered.")
      
    # Ask the user whether to enter another month 
    again = input("\nEnter another month (Y or N)? ").upper()
    while again not in "YyNn":
        again = input("Enter another month (Y or N)? ").upper()
        
print("Have a good day!")