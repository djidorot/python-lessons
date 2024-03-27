"""
Requirements:
Implement a function called check_voting_eligibility() that performs the following steps:

Get user input for age and citizenship status.

Convert the input to appropriate data types (age as an integer and citizenship status as a boolean).

Check voting eligibility based on the following criteria:
If the user is 18 years old or older and is a citizen (responded with “yes”), the function should return the message: “You are eligible to vote!”

Otherwise, if the user does not meet both criteria (age < 18 or not a citizen), the function should return the message: “Sorry, you are not eligible to vote.”

Call the check_voting_eligibility() function to execute the operations.

"""

def check_voting_eligibility():
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


# Call the function to execute the operations
check_voting_eligibility()

