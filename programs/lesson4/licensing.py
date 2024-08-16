"""
Problem Statement:
You are tasked with developing a Python program to determine a person's eligibility for obtaining a driver's license based on their age. Your program should include a function called check_license_eligibility(age) which takes an integer parameter age representing the age of the person. The function should print a message indicating whether the person is eligible for a driver's license, a learner's permit, or if they are not eligible yet.

Your program should prompt the user to input their age and then call the check_license_eligibility() function to determine their eligibility based on the provided age.

Write a Python script that implements the above requirements. Ensure that your code follows proper coding conventions and includes appropriate comments to explain the functionality of each section. Test your program with different age inputs to verify its correctness.

"""

"""
Requirements
Write a function check_license_eligibility(age) that takes an integer age as its argument and prints one of the following messages:

If the user is 18 years old or older, print: "Congratulations! You are eligible for a driver's license."
If the user is 16 or 17 years old, print: "You are eligible for a learner's permit."
If the user is under 16 years old, print: "Sorry, you are not eligible for a driver's license yet."
Prompt the user to enter their age using the input function. Ensure that the input is converted to an integer.

Call the check_license_eligibility function with the user's age as its argument to display the appropriate message.

"""


def check_license_eligibility(age):
    if age >= 18:
        print("\nCongratulations! You are eligible for a driver's license.\n")
    elif age >= 16:
        print("\nYou are eligible for a learner's permit.\n")
    else:
        print("\nSorry, you are not eligible for a driver's license yet.\n")


# Ask the user for their age
age = int(input("\nPlease enter your age: "))
check_license_eligibility(age)
