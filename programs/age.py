
"""
Age to 100 Calculator

Objective: Write a Python program that takes the user's age as input, converts it to an integer, and calculates the year in which the user will turn 100 years old.

Instructions:

User Input: The program starts by prompting the user to enter their age. Use the input function to receive the age as a string.

Type Conversion: Convert the entered age from a string to an integer using the int function.

Year Calculation: The program assumes the current year is 2023 (you may need to update this). It calculates how many years are left until the user turns 100.

Display the Result: Add the calculated years to the current year to determine the year when the user will turn 100. Finally, print the result.

Run the Program: Execute the script and input your age when prompted. The program will output the year you will turn 100.

Experiment: Try running the program with different ages to observe how the result changes. Ensure to update the current_year variable with the actual current year.

Save Your Work: Save the Python file for future reference.

Feel free to explore and modify the program to enhance your understanding of Python variables, input, and type conversion. If you encounter any challenges or have questions, seek assistance. Happy coding!

"""
# Get user's age as input
user_age_str = input("Enter your age: ")

# Convert the user's age from string to integer
user_age = int(user_age_str)

# Calculate the year in which the user will turn 100 years old
current_year = 2023  # You may need to update this with the current year
years_until_100 = 100 - user_age
year_turn_100 = current_year + years_until_100

# Display the result
print(f"You will turn 100 years old in the year {year_turn_100}.")
