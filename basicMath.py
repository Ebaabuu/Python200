# This program gets two integers and displays their sum, product,
# difference, and quotient.
# @author Emaad Gafoor

# Get operands from the user
firstOperand = int(input("First positive integer: "))
secondOperand = int(input("Second positive integer: "))

# Display results of mathematical calculations

print("\nSum:", firstOperand + secondOperand)
print("Product:", firstOperand * secondOperand)
print("Difference:", firstOperand - secondOperand)
print(f"Quotient: {firstOperand / secondOperand:.2f}")