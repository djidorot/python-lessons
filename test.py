"""
Problem Statement:

Create a Python program that determines whether a person is eligible to vote based on their age and citizenship status. The program should repeatedly prompt the user to input their age and citizenship status (yes/no). If the user inputs "exit" at any point, the program should terminate.

The program should check if the age input is a valid integer and if the citizenship status input is either "yes" or "no". If the inputs are valid, the program should determine if the person is eligible to vote (age 18 or older and a citizen). If eligible, it should print "You are eligible to vote!" Otherwise, it should print "Sorry, you are not eligible to vote."

Your task is to refactor the given program by encapsulating its main functionality within a function named check_voting_eligibility(). Upon completion, create a problem statement, including the code template and task description, for a Python programming assignment for students.

"""


def check_voting_eligibility():
    while True:
        pass
        # Your code here ....

        # Check if the user wants to exit the loop
        if age_str.lower() == 'exit' or is_citizen_str.lower() == 'exit':
            pass
            # Your code here ....

        # Check if age is a valid integer
        if age_str.isdigit():
            pass
            # Your code here ....

            # Check if citizenship status is valid
            if is_citizen_str.lower() == "yes" or is_citizen_str.lower() == "no":
                pass
                # Your code here ....

                # Exit the loop if the input is valid
                break
            else:
                pass
                # Your code here ....
        else:
            pass
            # Your code here ....

# Call the function to execute the program
check_voting_eligibility()
