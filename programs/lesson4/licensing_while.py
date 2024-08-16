def check_license_eligibility(age):
    if age >= 18:
        print("\nCongratulations! You are eligible for a driver's license.\n")
    elif age >= 16:
        print("\nYou are eligible for a learner's permit.\n")
    else:
        print("\nSorry, you are not eligible for a driver's license yet.\n")


# Loop to continuously prompt the user for their age
while True:
    age_input = input("Please enter your age: ")

    if age_input.isdigit():
        age = int(age_input)
        if age > 0:
            check_license_eligibility(age)
            break  # Exit the loop after a valid input is processed
        else:
            print("Please enter a positive age.")
    else:
        print("Please enter a valid age as a number.")
