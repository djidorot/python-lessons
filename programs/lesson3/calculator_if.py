"""
Problem Statement: Simple Calculator Program

You are tasked with creating a simple calculator program in Python. The program should display a menu with the following options:

Addition
Subtraction
Multiplication
Division
Exit

The program should prompt the user to enter their choice by inputting a number from 1 to 5. Based on the user's choice, the program should perform the corresponding arithmetic operation on two numbers entered by the user.

If the user selects addition (option 1), the program should ask the user to input two numbers and then display the result of adding them.

If the user selects subtraction (option 2), the program should ask the user to input two numbers and then display the result of subtracting the second number from the first.

If the user selects multiplication (option 3), the program should ask the user to input two numbers and then display the result of multiplying them.

If the user selects division (option 4), the program should ask the user to input two numbers. If the second number is zero, the program should display an error message saying "Cannot divide by zero!". Otherwise, it should display the result of dividing the first number by the second.

If the user selects exit (option 5), the program should display a farewell message and terminate.

If the user inputs an invalid option (anything other than 1 to 5), the program should display a message saying "Invalid input. Please enter a valid option."

Your task is to implement this calculator program in Python using the provided code structure as a guide. Ensure that your program behaves as described above and handles input validation appropriately.
"""

print("Welcome to Simple Calculator")

# Display menu
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

# Take input from the user
choice = input("Enter choice (1/2/3/4/5): ")

# Check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
elif choice == '5':
    print("Thank you for using Simple Calculator. Goodbye!")
else:
    print("Invalid input. Please enter a valid option.")
