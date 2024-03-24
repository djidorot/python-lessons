
"""
Follow the instructions below to complete the exercise:

Continuous Input:
Use a while True loop to create a continuous input mechanism.
Prompt the user to enter their age using input("Enter your age: ").
Prompt the user to enter their citizenship status using input("Are you a citizen? (yes/no): ").

Exit Mechanism:
Check if the user wants to exit the loop. If the user enters 'exit' for either age or citizenship status, print "Exiting the program." and break out of the loop.

Age Validation:
Check if the entered age is a valid integer using isdigit().
If it is a valid integer, convert it to an integer using int(age_str).

Citizenship Validation:
Check if the entered citizenship status is either 'yes' or 'no'.
Convert the input to a boolean value (True for 'yes', False for 'no').

Voting Eligibility Check:
Check if the age is 18 or older and the citizenship status is 'yes'.
Print "You are eligible to vote!" if the conditions are met.
Print "Sorry, you are not eligible to vote." if the conditions are not met.

Input Error Handling:
If the age input is not a valid integer, print "Invalid input for age. Please enter a valid age as a number."
If the citizenship status is not 'yes' or 'no', print "Invalid input for citizenship. Please enter 'yes' or 'no'."

Exiting the Loop:
If the input is valid and the eligibility is checked, break out of the loop.
"""


while True:
    # Get user input for age and citizenship status
    age_str = input("Enter your age: ")
    is_citizen_str = input("Are you a citizen? (yes/no): ")

    # Check if the user wants to exit the loop
    if age_str.lower() == 'exit' or is_citizen_str.lower() == 'exit':
        print("Exiting the program.")
        break

    # Check if age is a valid integer
    if age_str.isdigit():
        age = int(age_str)

        # Check if citizenship status is valid
        if is_citizen_str.lower() == "yes" or is_citizen_str.lower() == "no":
            is_citizen = is_citizen_str.lower() == "yes"

            # Check voting eligibility and print the result
            if age >= 18 and is_citizen:
                print("You are eligible to vote!")
            else:
                print("Sorry, you are not eligible to vote.")

            # Exit the loop if the input is valid
            break
        else:
            print("Invalid input for citizenship. Please enter 'yes' or 'no'.")
    else:
        print("Invalid input for age. Please enter a valid age as a number.")
