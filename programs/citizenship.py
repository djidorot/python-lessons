
"""
Input Collection:
The script begins by collecting two pieces of information from the user: their age and citizenship status.

Boolean Conversion:
The script then converts the citizenship status input to a boolean value (True if "yes", False otherwise).

Voting Eligibility Check:
The main logic of the script is to check if the person is eligible to vote based on their age (at least 18 years) and citizenship status.

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
