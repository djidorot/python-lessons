"""
Problem Statement:

Create a Python program that determines whether a person is eligible to vote based on their age and citizenship status. The program should repeatedly prompt the user to input their age and citizenship status (yes/no). If the user inputs "exit" at any point, the program should terminate.

The program should check if the age input is a valid integer and if the citizenship status input is either "yes" or "no". If the inputs are valid, the program should determine if the person is eligible to vote (age 18 or older and a citizen). If eligible, it should print "You are eligible to vote!" Otherwise, it should print "Sorry, you are not eligible to vote."

Your task is to refactor the given program by encapsulating its main functionality within a function named check_voting_eligibility(). Upon completion, create a problem statement, including the code template and task description, for a Python programming assignment for students.

"""


def check_voting_eligibility():
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


# Call the function to execute the program
check_voting_eligibility()


