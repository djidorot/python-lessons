"""
The program starts by importing the math module to make mathematical functions available for use.

It then prompts you to enter two numbers. You should enter any numeric values when prompted.

Next, the program performs the following basic arithmetic operations on the entered numbers:

Addition: It adds the two numbers together and stores the result in addition_result.
Subtraction: It subtracts the second number from the first number and stores the result in subtraction_result.
Multiplication: It multiplies the two numbers together and stores the result in multiplication_result.
Division: It divides the first number by the second number and stores the result in division_result.

After performing these operations, the program displays the results for each operation, including the mathematical expression used
and the computed result.

Lastly, the program demonstrates operator precedence and the use of math functions. It calculates a more complex expression using parentheses,
addition, multiplication, and the math.sqrt function to compute the square root of the second number. The result is displayed along with the
expression used.

"""

import math

# Get user input for two numbers
print()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic arithmetic operations
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2

# Display the results
print()
print(f"Addition: {num1} + {num2} = {addition_result}")
print(f"Subtraction: {num1} - {num2} = {subtraction_result}")
print(f"Multiplication: {num1} * {num2} = {multiplication_result}")
print(f"Division: {num1} / {num2} = {division_result}")

# Demonstrate operator precedence and math functions
result = ((num1 + num2) * num1) / (math.sqrt(num2) + 1)
print()
print(
    f"Result of complex expression: (({num1} + {num2}) * {num1}) / (sqrt({num2}) + 1) = {result}")
print()
