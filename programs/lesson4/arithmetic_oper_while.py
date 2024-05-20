"""
PROBLEM STATEMENT
You are tasked with creating a Python program that performs basic arithmetic operations on two user-provided numbers and allows the user to perform these operations repeatedly until they choose to stop. The program should include the following features:

1. Function Definition: Define a function named perform_arithmetic_operations that takes two parameters, num1 and num2, and performs the following operations:

- Addition
- Subtraction
- Multiplication
- Division

2. Display Results: The function should display the results of the arithmetic operations in a clear format.

3. User Input: The program should repeatedly prompt the user to enter two numbers.

4. Loop for Repeated Operations: After performing the arithmetic operations, the program should ask the user if they want to perform another operation. If the user types "yes", the program should prompt for new numbers and perform the operations again. If the user types "no", the program should display a goodbye message and exit.

5. Graceful Exit: Ensure that the program exits gracefully when the user decides not to continue.

REQUIREMENTS
1. Use a while loop to repeatedly prompt the user for input and perform the operations.
2. Use the input function to get user input and the float function to convert the input to floating-point numbers.
3. Use conditionals to determine whether to continue or exit the loop based on user input.
4. Handle division by zero appropriately by displaying an error message instead of crashing the program.
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


while True:
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call the function with user input as arguments
    perform_arithmetic_operations(num1, num2)

    # Ask user if they want to continue
    continue_choice = input(
        "Do you want to perform another operation? (yes/no): ").strip().lower()

    # Exit the loop if the user chooses 'no'
    if continue_choice != 'yes':
        print("Exiting the program.")
        break
