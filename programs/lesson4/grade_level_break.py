"""

"""

def determine_grade(age):
    if age < 0:
        print("\nInvalid age\n")
    elif age < 6:
        print("\nYou are too young for school\n")
    elif age < 12:
        print("\nYou are in primary school\n")
    elif age < 15:
        print("\nYou are in middle school\n")
    elif age < 18:
        print("\nYou are in high school\n")
    else:
        print("\nYou are in college or beyond\n")


while True:
    try:
        age = int(input("\nEnter your age: "))
        determine_grade(age)
    except ValueError:
        print("\nPlease enter a valid number.")

    continue_prompt = input("\nDo you want to enter another age? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        break




