"""
Problem Statement:

You are tasked with creating a Python program called "Age to Grade Converter". Your program should prompt the user to enter their age. Based on the entered age, the program will determine the appropriate academic stage the user is likely in and print the corresponding message.

Here are the guidelines for the program:

1. Prompt the user to enter their age.
2. Check if the entered age is valid (i.e., non-negative).
3. Use if/elif/else statements to determine the appropriate academic stage based on the age:
    a. If the age is less than 0, print "Invalid age".
    b. If the age is less than 6, print "You are too young for school".
    c. If the age is between 6 and 11 (inclusive), print "You are in primary school".
    d. If the age is between 12 and 14 (inclusive), print "You are in middle school".
    e. If the age is between 15 and 17 (inclusive), print "You are in high school".
    f. If the age is 18 or above, print "You are in college or beyond".

4. Execute the program and test it with different ages to ensure it provides the correct output.

"""

# Get the age from the user
age = int(input("Enter your age: "))

# Determine the grade based on age
if age < 0:
    print("Invalid age")
elif age < 6:
    print("You are too young for school")
elif age < 12:
    print("You are in primary school")
elif age < 15:
    print("You are in middle school")
elif age < 18:
    print("You are in high school")
else:
    print("You are in college or beyond")
