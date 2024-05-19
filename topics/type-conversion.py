"""
Use the input() function to prompt the user for their name. Store the input in a variable called name.

Use the input() function again to prompt the user for their age, but this time store it as a string in a variable called age_str.

Convert the age_str variable into an integer and store it in a new variable called age. You can use the int() function for this conversion.

Print a blank line to create some separation in the output.

Use the print() function to display a message to the user that includes their name and age. You can use an f-string (formatted string)
for this, as shown in the example.
"""

# Get user input for name and age
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Convert age_str to an integer
age = int(age_str)

print()
# Display a message with the user's name and age
print(f"Hello, {name}! You are {age} years old.")


# Modify
# Get user input for name, age, phone number, and birthday
name = input("Enter your name: ")
age_str = input("Enter your age: ")
phone_number_str = input(
    "Enter your phone number (numeric only, without spaces or dashes): ")
birthday = input("Enter your birthday (e.g., MM/DD/YYYY): ")

# Convert age_str and phone_number_str to integers
age = int(age_str)
phone_number = int(phone_number_str)

print()
# Display a message with the user's information
print(f"Hello, {name}! You are {age} years old.")
print(f"Your phone number is: {phone_number}")
print(f"Your birthday is: {birthday}")
