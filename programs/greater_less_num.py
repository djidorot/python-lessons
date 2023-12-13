"""
This Python program allows a user to input two numbers, and then it compares these numbers to determine whether the
first number is greater than, equal to, or less than the second number. It uses if/else statements and logical
operators to perform the comparison and provides the appropriate output based on the result. It's a simple
example of how to take user input, use conditional statements, and display results in Python.
"""

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is less than {num2}")
