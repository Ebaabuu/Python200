# This program displays a sphere diameter, surface area,
# and valume based upon a user-entered radius.
# @author Emaad Gafoor

import math

# Get the radius
radius = float(input("Sphere Diameter: "))

# Compute and display the diameter, surface area, and volume
diameter = 2 * radius # formula for diameter
surfaceArea = 4 * math.pi * pow(radius, 2) # formula for surface area
volume = 4 / 3 * math.pi * pow(radius, 3) # formula for volume

print(f"\nDiameter: {diameter:,.2f} units")
print(f"Surface area: {surfaceArea:,.2f} square units")
print(f"Volume: {volume:,.2f} cubic units")