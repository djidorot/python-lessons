"""
Problem Statement:
You are tasked with writing a simple calculator program in Python that can perform basic arithmetic operations: addition, subtraction, multiplication, and division. The program should allow the user to perform multiple calculations in a single session until they choose to exit. The calculator should handle potential errors, such as division by zero, and invalid operator inputs.

Requirements:

Function Definition:
 - Define a function named perform_operation that takes three parameters: num1 (a float), num2 (a float), and operator (a string).
 - The function should perform the arithmetic operation specified by operator on num1 and num2.
 - Supported operators are +, -, *, and /.
 - If the operator is / and num2 is 0, the function should print an error message and return None.
 - If the operator is not one of the supported operators, the function should print an invalid operator message and return None.
 - The function should return the result of the operation for valid inputs.

User Interaction:
 - Continuously prompt the user to input two numbers and an operator.
 - Use the perform_operation function to calculate the result.
 - Print the result of each calculation.
 - After each calculation, ask the user if they want to perform another calculation. If the user inputs anything other than "yes", exit the program.

Error Handling:
 - Handle division by zero by printing an appropriate error message.
 - Handle invalid operator inputs by printing an appropriate error message.
"""


def perform_operation(num1, num2, operator):
    """
    Perform arithmetic operations based on the operator.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operator (str): The operator (+, -, *, /).

    Returns:
    float: The result of the operation.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        return None


while True:
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the type of operation
    operator = input("Enter the operator (+, -, *, /): ")

    # Perform operation using the function
    result = perform_operation(num1, num2, operator)
    if result is not None:
        print(f"Result: {num1} {operator} {num2} = {result}")

    # Ask the user if they want to perform another calculation
    continue_choice = input(
        "Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the calculator. Goodbye!")
        break


