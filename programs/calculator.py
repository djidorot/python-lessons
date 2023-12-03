"""
User Input: The program begins by using the input function to prompt the user to enter two numbers.
The float function is then used to convert the user's input into floating-point numbers, which allows for decimal values.

Arithmetic Operations: After obtaining the two input numbers (num1 and num2), the program performs four basic arithmetic operations on them:

Sum: It calculates the sum of num1 and num2 and stores the result in the variable sum_result.

Difference: It calculates the difference between num1 and num2 and stores the result in the variable difference_result.

Product: It calculates the product of num1 and num2 and stores the result in the variable product_result.

Division: It calculates the division of num1 by num2 and stores the result in the variable division_result.
Note that this division operation assumes that num2 is not zero (no division by zero check is included in this simple example).

Display Results: Finally, the program uses the print function to display the results of the arithmetic operations.
It uses formatted strings (f-strings) to create descriptive output messages that include the values of the
variables and the results of each operation. The results are shown for all four operations: sum, difference, product, and division.

When you run this program, it will prompt you to enter two numbers, perform the specified arithmetic calculations,
and then display the results in a clear and organized manner.
"""


# Get user input for two numbers
num1 = float(input("Enter the first number: "))
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
