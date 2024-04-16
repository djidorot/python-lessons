"""

"""


def check_license_eligibility(age):
    if age >= 18:
        print("Congratulations! You are eligible for a driver's license.")
    elif age >= 16:
        print("You are eligible for a learner's permit.")
    else:
        print("Sorry, you are not eligible for a driver's license yet.")


# Ask the user for their age
age = int(input("Please enter your age: "))
check_license_eligibility(age)
