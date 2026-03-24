# This program simulates a mini ATM by requesting actions from the user
# and calculating their current balance.
# @author Emaad Gafoor

def main():
    balance = 1500
    choice = ""
    
    # Continue requesting inputs from user until user inputs E or e
    while choice != "E":
        choice = (getMenuChoice())
        if choice == "W":
            balance = processWithdrawal(balance)
        elif choice == "B":
            print(f"Current balance: ${balance:,.2f}")
        elif choice == "D":
            balance = processDeposit(balance)
        print()
          
    print("Thank you for banking with us.")

# getMenuChoice presents a banking menu of choices
# @return The customer's menu choice as a single upper case letter
def getMenuChoice():
    print("====================")
    print("Enter W for Withdraw")
    print("Enter D for Deposit")
    print("Enter B for Balance")
    print("Enter E for Exit")
    print("====================")
    choice = input("Choice: ").upper()

    return choice

# processWithdrawal processes a customer's withdrawal
# @param balance The current balance
# @return The updated balance
def processWithdrawal(balance):
    withdrawal = float(input("Enter withdrawal amount: $"))  
    if withdrawal > balance:
        print("Insufficient funds.")        
    elif withdrawal <= 0:
        print("Improper withdraw amount entered.")    
    else:
        balance -= withdrawal
        print(f"Please take your ${withdrawal:,.2f}")
        
    return balance

# processDeposit processes a customer's deposit
# @param balance The current balance
# @return The updated balance
def processDeposit(balance):
    deposit = float(input("Enter deposit amount: $"))         
    if deposit <= 0:
        print("Improper deposit amount entered.")    
    else:
        balance += deposit
        print(f"${deposit:,.2f} deposited.")
        
    return balance

main()