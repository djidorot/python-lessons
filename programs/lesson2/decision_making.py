"""
Problem Statement: Simple Calculator

You are tasked with creating a simple calculator program that performs basic arithmetic operations. The program should allow the user to choose from the following options:

1. Addition: Add two numbers.
2. Subtraction: Subtract one number from another.
3. Multiplication: Multiply two numbers.
4. Division: Divide one number by another (avoid division by zero).

The program should prompt the user to enter their choice (1, 2, 3, or 4) and then input the two numbers. Based on the user's choice, the program should display the result of the selected operation.

Requirements:
1. Display a menu with the available operations.
2. Accept the user's choice (1, 2, 3, or 4).
3. Prompt the user to input two numbers.
4. Perform the selected operation and display the result.
5. Handle division by zero (if applicable).

"""
print()
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

print()
choice = input("Enter choice (1/2/3/4): ")

print()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")
