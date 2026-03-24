# @author Emaad Gafoor

# Get a numeric month
Print("Enter a numeric month and I will display the season.")
month = int(input("Month: "))

# Display the corresponding season
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Fall")
else: 
    print("An invalid month was entered.")