
"""
Here's how the program works:

It prompts the user to enter their age using the input function, and the entered value is stored as a string in the variable age_str.

It then converts the string age_str to an integer using the int function, and the result is stored in the variable age.

The program calculates the year of birth by subtracting the user's age from the current year (2023 in this case) and stores it in the variable birth_year.

Finally, it prints the calculated birth year using the print function.

"""

# Get the user's age as input
age_str = input("Enter your age: ")

# Convert the age from string to integer
age = int(age_str)

# Calculate the year of birth (assuming the current year is 2023)
current_year = 2023
birth_year = current_year - age

# Display the result
print("You were born in the year:", birth_year)
