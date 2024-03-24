"""
Program Description: Even/Odd Number Checker

Objective:
Create a Python program that takes a range of numbers from the user and determines whether each number within that range is even or odd.

Instructions:

Prompt the user to enter a starting number and an ending number.
Validate that the ending number is greater than the starting number. If not, display an error message.
If the input is valid, use a for loop to iterate through the numbers in the specified range (inclusive of both the starting and ending numbers).
For each number in the range, use an if statement and the modulo operator (%) to check if the number is even or odd.
Print the result, indicating whether each number in the range is even or odd.

Example Output:

Enter the starting number: 5
Enter the ending number: 10
5 is odd.
6 is even.
7 is odd.
8 is even.
9 is odd.
10 is even.

"""

# Get the range of numbers from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Validate that the ending number is greater than the starting number
if end <= start:
    print("Error: Ending number must be greater than the starting number.")
else:
    # Iterate through the numbers in the range
    for number in range(start, end + 1):
        # Check if the number is even or odd
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
