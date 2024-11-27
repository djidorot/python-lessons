"""
Problem Statement:
Write a Python program that prompts the user to enter two numbers. The program should then compare the two numbers and print out one of the following statements based on the comparison:

If the first number is greater than the second number, print: "The first number is greater than the second number."
If the second number is greater than the first number, print: "The second number is greater than the first number."
If both numbers are equal, print: "Both numbers are equal."

Your program should utilize input statements to receive user input, if statements to perform the comparison, and print statements to display the result.
sample
"""

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparing the numbers
if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The second number is greater than the first number.")
else:
    print("Both numbers are equal.")
