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
