"""
Problem Statement:

Write a Python program that determines a student's eligibility for a driver's license or learner's permit based on their age. Your program should prompt the user to enter their age. If the age provided is 18 or above, the program should display a message congratulating the student on being eligible for a driver's license. If the age provided is 16 or above but less than 18, the program should inform the student that they are eligible for a learner's permit. If the age provided is below 16, the program should notify the student that they are not yet eligible for a driver's license.

Your program should continuously prompt the user for their age until a valid age (a positive integer) is entered. Ensure that your program handles invalid inputs gracefully, providing clear instructions to the user on how to enter a valid age.

"""


def check_license_eligibility(age):
    if age >= 18:
        print("\nCongratulations! You are eligible for a driver's license.\n")
    elif age >= 16:
        print("\nYou are eligible for a learner's permit.\n")
    else:
        print("\nSorry, you are not eligible for a driver's license yet.\n")


# Ask the user for their age
while True:
    age_input = input("\nPlease enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        if age > 0:
            break
        else:
            print("Please enter a positive age.")
    else:
        print("Please enter a valid age as a number.")

check_license_eligibility(age)
