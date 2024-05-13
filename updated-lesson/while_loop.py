"""
In Python, a "while" loop is a control flow statement that allows you to repeatedly execute a block of code as long as a specified condition is true. It consists of a condition followed by an indented block of code. The code inside the block will be executed repeatedly until the condition evaluates to False.

Here's the basic syntax of a while loop in Python:
"""

condition = "Boolean"

while condition:
    # Code block to be executed while the condition is true
    # This block will be repeated until the condition becomes false
    pass

# For example, a simple while loop that counts from 1 to 5 could look like this:
count = 1
while count <= 5:
    print(count)
    count += 1

"""
In this example, the loop will execute as long as the condition count <= 5 is true. The variable count starts at 1, and with each iteration, it is incremented by 1 until it reaches 6. Once count becomes 6, the condition count <= 5 becomes false, and the loop terminates.
"""


# Example Program
# Initialize variables
total = 0
number = 0

# Keep asking for numbers until a negative number is entered
while number >= 0:
    # Ask the user for input
    number = int(input("Enter a number (enter a negative number to stop): "))

    # Check if the number is positive
    if number >= 0:
        total += number  # Add the positive number to the total

# Print the sum of all positive numbers entered
print("The sum of all positive numbers entered is:", total)
