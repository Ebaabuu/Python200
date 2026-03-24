# This program displays the corrosponding damage
# report depending on the inputted wind speed.
# @author Emaad Gafoor

# Innitializes constant variables to gauge damage
# caused by wind speeds greater than or equal to value
EF_5 = 200
EF_4 = 166
EF_3 = 133
EF_2 = 111
EF_1 = 86
EF_0 = 65

# Get the user's wind speed
windSpeed = int(input("Wind Speed (MPH): "))

# Display the sequence
if windSpeed > EF_5:
    print("EF-5: Destruction of all infrastructure.")
elif windSpeed >= EF_4:
    print("EF-4: Homes leveled, cars thrown around.")
elif windSpeed >= EF_3:
    print("EF-3: Entire stories of homes and buildings" + 
          " destroyed, trains overturned, cars lifted off the ground.")
elif windSpeed >= EF_2:
    print("EF-2: Torn off roofs, mobile homes destroyed, " +
    "large trees uprooted.")
elif windSpeed >= EF_1:
    print("EF-1: Roofs stripped, mobile homes overturned, " + 
          "exterior home damage.")
elif windSpeed >= EF_0:
    print("EF-0: Some damage to roofs, siding, and tree branches.")
else: 
    print("Likely not a tornado.")