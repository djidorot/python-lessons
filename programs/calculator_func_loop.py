"""
Problem Statement: Arithmetic Operations Program

You are tasked with creating a Python program to perform basic arithmetic operations on two numbers entered by the user. Your program should allow the user to input two numbers repeatedly until they decide to quit. Upon receiving the numbers, the program should display the sum, difference, product, and division of the two numbers.

Instructions:

Implement a Python function named perform_arithmetic_operations that accomplishes the following:

Inside a while loop, continuously prompt the user to enter the first number. If the user enters 'q', the loop should terminate, and the program should end.

If the input is a valid number, prompt the user to enter the second number.
Perform the following arithmetic operations:

    Addition (sum)
    Subtraction (difference)
    Multiplication (product)
    Division (division)

Display the results of each operation to the user.
Call the perform_arithmetic_operations function to execute the program.

Example:
Enter the first number (or 'q' to quit): 5
Enter the second number: 3
Sum: 5.0 + 3.0 = 8.0
Difference: 5.0 - 3.0 = 2.0
Product: 5.0 * 3.0 = 15.0
Division: 5.0 / 3.0 = 1.6666666666666667

Enter the first number (or 'q' to quit): 8
Enter the second number: 2
Sum: 8.0 + 2.0 = 10.0
Difference: 8.0 - 2.0 = 6.0
Product: 8.0 * 2.0 = 16.0
Division: 8.0 / 2.0 = 4.0

Enter the first number (or 'q' to quit): q

"""


def perform_arithmetic_operations():
    while True:
        # Get user input for two numbers
        num1 = float(input("Enter the first number (or 'q' to quit): "))
        if num1 == 'q':
            break
        num2 = float(input("Enter the second number: "))

        # Perform arithmetic operations
        sum_result = num1 + num2
        difference_result = num1 - num2
        product_result = num1 * num2
        division_result = num1 / num2

        # Display the results
        print(f"Sum: {num1} + {num2} = {sum_result}")
        print(f"Difference: {num1} - {num2} = {difference_result}")
        print(f"Product: {num1} * {num2} = {product_result}")
        print(f"Division: {num1} / {num2} = {division_result}")


# Call the function to execute the code
perform_arithmetic_operations()
