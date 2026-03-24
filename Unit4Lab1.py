# This program obtains the user's bank account balance and
# calculates the balance after checks are withdrawn.
# @author Emaad Gafoor

# Get balance info
balance = float(input("Please enter a balance: $"))
checkAmount = 1

# Continually subtract from balance with user-prompted values
while balance > 0 and checkAmount > 0:
    checkAmount = float(input("\nCheck amount (0 or negative to end): $"))
    if checkAmount > balance: # Prevent checks from bouncing
        print("Warning: Check will bounce. No transaction occured.")
    elif checkAmount > 0: # Set sentinal value as non-positive input
        balance-=checkAmount
        print(f"Current balance: ${balance:,.2f}")
print(f"\nFinal balance: ${balance:,.2f}")