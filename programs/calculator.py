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

# Calculator 1


def calculator1():
    print()
    print("Calculator 1")
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    division_result = num1 / num2

    # Display the results
    print()
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    print(f"Division: {num1} / {num2} = {division_result}")


# Calculator 2
def calculator2():
    print()
    print("Calculator 2")
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    division_result = num1 / num2

    # Display the results
    print()
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    print(f"Division: {num1} / {num2} = {division_result}")


"""
Inside the main function, prompt the user to choose between Calculator 1 and Calculator 2 by displaying a menu with options.

Take user input to select either Calculator 1 or Calculator 2.

Based on the user's choice, call the corresponding calculator function (calculator1 or calculator2).

After displaying the results from the chosen calculator, ask the user if they want to perform another calculation.

If the user wants to perform another calculation, repeat steps 1-4. If not, end the program with a friendly goodbye message.
"""


def main():
    while True:
        print("Choose a Calculator:")
        print("1. Calculator 1")
        print("2. Calculator 2")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            calculator1()
        elif choice == '2':
            calculator2()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        another_calculation = input(
            "Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Goodbye!")
            break


main()
