"""
Problem Statement:
You are tasked with creating a simple arithmetic calculator program in Python. Your program should prompt the user to enter two numbers and then ask for the type of arithmetic operation they want to perform. The available operations are addition (+), subtraction (-), multiplication (*), and division (/).

Your program should perform the selected operation on the two input numbers and display the result. If the user attempts to divide by zero, your program should handle this case and display an appropriate error message.

Write a Python program to implement the above functionality. Ensure that your program provides clear prompts and output messages to guide the user through the process.

Your program should follow the structure outlined in the provided code snippet. You are not allowed to use any external libraries or predefined functions for arithmetic operations.

"""

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
