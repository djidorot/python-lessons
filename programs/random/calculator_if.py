# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the type of operation
operator = input("Enter the operator (+, -, *, /): ")

# Perform arithmetic operations based on the operator
if operator == '+':
    result = num1 + num2
    print(f"Sum: {num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Difference: {num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"Product: {num1} * {num2} = {result}")

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Division: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter +, -, *, or /.")
