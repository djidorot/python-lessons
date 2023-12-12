"""
User Input:

Prompt the user to enter a number using the input function.
Store the entered value in the variable user_input.
Data Conversion:

Convert user_input to a floating-point number using float() and store the result in the variable number.
Assume that the user will enter a numerical value. Handle cases where the input may not be numeric.
Number Classification:

Use an if/elif/else statement to check the type of the entered number:
If number is greater than 0, print "The entered number is positive."
If number is less than 0, print "The entered number is negative."
If neither condition is met, print "The entered number is zero."
Testing:

Test your program with different inputs, including positive numbers, negative numbers, and zero, to ensure it correctly classifies the entered number.
"""

# Get user input
user_input = input("Enter a number: ")

# Convert the input to a float (assuming the user enters a numerical value)
number = float(user_input)

# Check if the number is positive, negative, or zero
if number > 0:
    print("The entered number is positive.")
elif number < 0:
    print("The entered number is negative.")
else:
    print("The entered number is zero.")
