"""
Prompt the user to input two numbers.

Compare the numbers using conditional statements:

If the first number is greater than the second, print that the first number is greater.
If the numbers are equal, print that they are equal.

Otherwise, print that the first number is less than the second.

"""

# Get input from the user
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"\n{num1} is greater than {num2}\n")
elif num1 == num2:
    print(f"\n{num1} is equal to {num2}\n")
else:
    print(f"\n{num1} is less than {num2}\n")


