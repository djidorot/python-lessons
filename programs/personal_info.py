"""
Save the File:
Save the file with an appropriate name and a .py extension, for example, personal_info_program.py.

Run the Program:
Run the program by executing the file in your Python environment.

Follow Prompts:
The program will prompt you to enter your name, age, city, and occupation. Follow the prompts and enter the requested information.

Review Output:
After entering the information, the program will display the collected details. Review the output to ensure it shows the correct information.

Customize the Program (Optional):
Optionally, you can customize the program:
Add more input prompts for additional information.
Modify the output format.

Experiment with additional features based on what you've learned.
"""

# Personal Information Program

# Get user input for personal information
print()
print("Personal Information - Part 1")


def personal_info1():
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    occupation = input("Enter your occupation: ")

    # Display the collected information
    print("\nPersonal Information:")
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)
    print("Occupation: ", occupation)


print()


def personal_info2():
    print("Personal Information - Part 2")

    # Get user input for personal information
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    occupation = input("Enter your occupation: ")

    # Display the collected information
    print("\nPersonal Information:")
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)
    print("Occupation: ", occupation)


personal_info2()


"""
FUNCTION

xplaining this task to students, you can break it down as follows:

Task: Personal Information Program

Objective:
Create a simple Python program that collects and displays personal information. The program should utilize functions for better organization and readability.

Step 1: Collecting Information Function
Create a function called get_personal_information.
Inside this function, use the input function to collect the user's name, age, city, and occupation.
Return these values as a tuple.

Step 2: Displaying Information Function
Create a function called display_personal_information that takes the collected information as arguments.
Inside this function, use print statements to display the user's personal information.

Step 3: Combining Functions
Call the get_personal_information function to collect the user's information and store it in a variable (e.g., user_info).
Call the display_personal_information function, passing the collected information as arguments using the * unpacking operator.

# Personal Information Program

def collect_and_display_information():
    # Get user input for personal information
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    occupation = input("Enter your occupation: ")

    # Display the collected information
    print("\nPersonal Information:")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Occupation:", occupation)

# Call the function
collect_and_display_information()



"""
