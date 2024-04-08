"""
Problem Statement: Personal Information Printer

You are tasked with creating a Python program that collects personal information from the user and prints it out. The program should prompt the user to input their name, age, and email address. Once the user provides this information, the program should display it in the following format:

Your Personal Information:
Name: [user's name]
Age: [user's age]
Email: [user's email]

Write a Python function called personal_info that takes three arguments: name, age, and email. The function should print the user's personal information as shown above.

Your task is to implement the personal_info function and test it by collecting input from the user and displaying their personal details.

"""


# Define a function named personal_info that takes three parameters: name, age, and email
def personal_info(name, age, email):
    # Print a message indicating that the personal information is being displayed
    print("Your Personal Information:")
    # Print the name parameter
    print("Name:", name)
    # Print the age parameter
    print("Age:", age)
    # Print the email parameter
    print("Email:", email)


# Get user input for name, age, and email
name_input = input("Enter your name: ")
age_input = input("Enter your age: ")
email_input = input("Enter your email: ")

# Call the personal_info function with the user-provided inputs as arguments
personal_info(name_input, age_input, email_input)
