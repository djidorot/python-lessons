"""
Problem Statement: Voting Eligibility Checker

You are tasked with creating a Python program that determines whether a person is eligible to vote based on their age and citizenship status.

Write a function called check_voting_eligibility that takes two parameters:

    age: an integer representing the age of the person.
    is_citizen_str: a string representing the citizenship status of the person. It can either be "yes" if the person is a citizen or "no" if the person is not a citizen.

The function should perform the following operations:

    Convert the is_citizen_str parameter to a boolean value. If the input is "yes", set is_citizen to True; otherwise, set it to False.
    Check if the person's age is greater than or equal to 18 and if they are a citizen.
    If both conditions are met, print "You are eligible to vote!".
    If either condition fails, print "Sorry, you are not eligible to vote.".

Additionally, the program should:

    Prompt the user to input their age and citizenship status.
    Call the check_voting_eligibility function with the provided inputs.

"""


def check_voting_eligibility(age, is_citizen_str):
    # Convert the input to a boolean value
    is_citizen = is_citizen_str.lower() == "yes"

    # Check voting eligibility and print the result
    if age >= 18 and is_citizen:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not eligible to vote.")


# Get user input for age and citizenship status
age = int(input("Enter your age: "))
is_citizen_str = input("Are you a citizen? (yes/no): ")

# Call the function with parameters
check_voting_eligibility(age, is_citizen_str)
