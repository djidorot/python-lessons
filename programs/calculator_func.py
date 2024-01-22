

def perform_arithmetic_operations():
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


# Call the function to execute the code
perform_arithmetic_operations()
