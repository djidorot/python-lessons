"""

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


# Number of operations to perform
n = int(input("Enter the number of operations you want to perform: "))

for _ in range(n):
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the type of operation
    operator = input("Enter the operator (+, -, *, /): ")

    # Perform operation using the function
    result = perform_operation(num1, num2, operator)
    if result is not None:
        print(f"Result: {num1} {operator} {num2} = {result}")
