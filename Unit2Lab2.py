# This program converts a long jump given in
# centimeters to feet and inches
# @author Emaad Gafoor

# Get the athelet's name and distance jumped
firstName = input("Long jumper's first name: ")
lastName = input("Long jumper's last name: ")
distanceCM = float(input("Distance jumeped (cm): "))

# Convert distance to feet and inches
CMS_PER_INCH = 2.54
INCHES_PER_FEET = 12

totalInches = distanceCM / CMS_PER_INCH
findFeet = totalInches // INCHES_PER_FEET
inchesInFeet = totalInches - (findFeet * INCHES_PER_FEET)

print (f"\n{firstName[0]:}. {lastName} jumped \
{findFeet:,.0f}' {inchesInFeet:,.1f}\"")
