# This program displays the highest tax rate
# given a randomly generated income
# @author Emaad Gafoor
from random import randint
def main():
    income = randint(0,600000)
    print(f"A 2023 income of ${income:,} for a single status")
    print("person reaches the " + 
          f"{getHighestIncomeTaxRate(income)}% tax bracket.")
    
# getHighestIncomeTaxRate determines the highest
# tax rate for an income
# @param income The taxabe income
# @precondition income >= 0
# @return The highest income tax rate
def getHighestIncomeTaxRate(income):    
    if income > 578125:
        income = 37
    elif income > 231250:
        income = 35
    elif income > 182100:
        income = 32         
    elif income > 95375:
        income = 24
    elif income > 44725:
        income = 22
    elif income > 11000:
        income = 12
    else:
        income = 10      
    return income

main()