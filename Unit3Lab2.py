# This program computes taxes for three different
# tax brackets and marital status.
# @author Emaad Gafoor

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25
RATE1_SINGLE = 8000.0
RATE2_SINGLE = 32000.0 # Greater than 32000 = RATE3
RATE1_MARRIED = 16000.0
RATE2_MARRIED = 64000.0 # Greater than 64000 = RATE3


# Read income and marital status
income = float(input("Please enter your income: $"))
maritalStatus = input("Please enter s for single, m for married: ").lower()

# Compute taxes due.
tax1 = 0 # tax due at first tax bracket income level
tax2 = 0 # tax due at second tax bracket income level
tax3 = 0 # remaining tax due if exceeding the seccond bracket income

if maritalStatus == "s" or maritalStatus == "m": 
    
    if maritalStatus == "s":
        if income <= RATE1_SINGLE:
            tax1 = RATE1 * income
            
        elif (income > RATE1_SINGLE and income <= RATE2_SINGLE):
            tax1 = RATE1 * RATE1_SINGLE
            tax2 = RATE2 * (income - RATE1_SINGLE)
            
        else:
            tax1 = RATE1 * RATE1_SINGLE
            tax2 = RATE2 * (RATE2_SINGLE - RATE1_SINGLE)
            tax3 = RATE3 * (income - RATE2_SINGLE)
            

    else:
        if income <= RATE1_MARRIED:
            tax1 = RATE1 * income
            
        elif (income > RATE1_MARRIED and income <= RATE2_MARRIED):
            tax1 = RATE1 * RATE1_MARRIED
            tax2 = RATE2 * (income - RATE1_MARRIED)
            
        else:
            tax1 = RATE1 * RATE1_MARRIED
            tax2 = RATE2 * (RATE2_MARRIED - RATE1_MARRIED)
            tax3 = RATE3 * (income - RATE2_MARRIED)
            
    totalTax = tax1 + tax2 + tax3
    
    # Display the tax
    print(f"The tax is ${totalTax:,.2f}")
    
    # Displays error for incorrect input
else: 
    print("Unrecognized marital status")