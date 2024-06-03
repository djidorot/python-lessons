"""
Problem Statement:

Write a Python program that prompts the user to enter their age and then determines their educational stage based on the following criteria:

    1. If the age is less than 0, print "Invalid age".
    2. If the age is less than 6, print "You are too young for school".
    3. If the age is between 6 and 11 (inclusive), print "You are in primary school".
    4. If the age is between 12 and 14 (inclusive), print "You are in middle school".
    5. If the age is between 15 and 17 (inclusive), print "You are in high school".
    6. If the age is 18 or older, print "You are in college or beyond".

Your program should define a function called determine_grade that takes an integer parameter age and implements the above logic to determine the educational stage. After defining the function, prompt the user to input their age and call the determine_grade function with the provided age.

Ensure that your program handles invalid input gracefully, such as non-integer values for age. If the user enters a non-integer value, your program should print "Invalid input. Please enter a valid age." and prompt the user to input their age again until a valid integer value is provided.

"""


def determine_grade(age):
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


# Get the age from the user
age = int(input("Enter your age: "))
determine_grade(age)
