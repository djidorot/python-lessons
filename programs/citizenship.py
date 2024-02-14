
"""
Problem Statement: Voting Eligibility Checker

You are tasked with creating a simple program that determines whether an individual is eligible to vote based on their age and citizenship status. The program should follow these rules:

Prompt the user to input their age.
Ask the user whether they are a citizen (with a “yes” or “no” response).
Convert the user’s input for citizenship status to a boolean value (True for “yes” and False for “no”).
Check if the user is at least 18 years old and a citizen.
If both conditions are met, display the message: “You are eligible to vote!”
Otherwise, display the message: “Sorry, you are not eligible to vote.”

Your task is to write the Python code that accomplishes the above requirements. Good luck! 🗳️

"""


# Get user input for age and citizenship status
age = int(input("Enter your age: "))
is_citizen_str = input("Are you a citizen? (yes/no): ")

# Convert the input to a boolean value
is_citizen = is_citizen_str.lower() == "yes"

# Check voting eligibility and print the result
if age >= 18 and is_citizen:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote.")
