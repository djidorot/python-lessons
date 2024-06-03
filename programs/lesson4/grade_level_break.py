"""

"""


def determine_grade(age):
    if age < 0:
        print("Invalid age")
    elif age < 6:
        print("You are too young for school")
    elif age < 12:
        print("You are in primary school")
    elif age < 15:
        print("You are in middle school")
    elif age < 18:
        print("You are in high school")
    else:
        print("You are in college or beyond")


while True:
    try:
        # Get the age from the user
        age = int(input("Enter your age: "))

        # If the age is invalid, print a message and continue to the next iteration
        if age < 0:
            print("Invalid age, please enter a positive number.")
            continue

        # Determine the grade based on age
        determine_grade(age)

        # Break the loop if a valid age is entered
        break
    except ValueError:
        # Handle non-integer input
        print("Invalid input, please enter a valid number.")
        continue
