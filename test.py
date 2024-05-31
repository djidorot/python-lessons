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
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the type of operation
    operator = input("\nEnter the operator (+, -, *, /): ")

    # Perform operation using the function
    result = perform_operation(num1, num2, operator)
    if result is not None:
        print(f"Result: {num1} {operator} {num2} = {result}\n")

    # Ask the user if they want to perform another calculation
    continue_choice = input(
        "\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("\nExiting the calculator. Goodbye!\n")
        break
