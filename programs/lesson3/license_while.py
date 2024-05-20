"""
Requirements:

Input Validation:
- The program should prompt the user to enter their age.
- If the input is not a positive integer, the program should display an error message and prompt the user again.
- This process should continue until the user enters a valid age (a positive integer).

Age Check:
- If the user's age is 18 or older, the program should display: "Congratulations! You are eligible for a driver's license."
- If the user's age is between 16 and 17 (inclusive), the program should display: "You are eligible for a learner's permit."
- If the user's age is less than 16, the program should display: "Sorry, you are not eligible for a driver's license yet."

"""


# Ask the user for their age until they enter a valid number
age = 0
while age <= 0:
    age_input = input("Please enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        if age <= 0:
            print("Age must be greater than 0. Please try again.")
    else:
        print("Invalid input. Please enter a valid number.")

# Check if the user is eligible for a driver's license
if age >= 18:
    print("Congratulations! You are eligible for a driver's license.")
elif age >= 16:
    print("You are eligible for a learner's permit.")
else:
    print("Sorry, you are not eligible for a driver's license yet.")
