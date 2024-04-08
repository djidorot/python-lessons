"""
Problem Statement: Arithmetic Operations

Objective:
The objective of this exercise is to practice performing basic arithmetic operations on two numbers.

Task:
Write a Python program that takes two numbers as input from the user and performs the following arithmetic operations:

Addition
Subtraction
Multiplication
Division

Requirements:
Define a function called perform_arithmetic_operations that takes two parameters: num1 and num2.
Inside the function, perform the following arithmetic operations:
    Calculate the sum of num1 and num2.
    Calculate the difference between num1 and num2.
    Calculate the product of num1 and num2.
    Calculate the division of num1 by num2.

Display the results of each operation in a user-friendly format.
Ensure that the division operation does not result in a division by zero error.
Outside the function, prompt the user to input two numbers.
Call the perform_arithmetic_operations function with the user-provided numbers as arguments.

"""


def perform_arithmetic_operations(num1, num2):
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


# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function with user input as arguments
perform_arithmetic_operations(num1, num2)
