"""
Problem Statement: Personal Information Collector

You are tasked with creating a Python program that collects and displays personal information from a user. The program should prompt the user for the following details:

Name: The user's full name.
Age: The user's age.
Hobbies: A list of the user's hobbies or interests.
Favorite Sport: The user's preferred sport.
Favorite Place: The place the user enjoys the most.
Favorite Foods: A list of the user's favorite foods.
Country to Visit: The country the user would like to visit.

The program should then display the collected information in a clear and organized format.

"""

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age
age = input("How old are you? ")

# Ask the user for their hobbies
hobbies = input("What are your hobbies? ")

# Ask the user for their favorite sports
sports = input("What is your favorite sport? ")

# Ask the user for their favorite place
place = input("What is your favorite place? ")

# Ask the user for their favorite foods
foods = input("What are your favorite foods? ")

# Ask the user for a country they would like to visit
country_to_visit = input("Which country would you like to visit? ")

# Print out the collected information
print("\n\nHere is the information you provided:")
print("Name:", name)
print("Age:", age)
print("Hobbies:", hobbies)
print("Favorite Sport:", sports)
print("Favorite Place:", place)
print("Favorite Foods:", foods)
print("Country to Visit:", country_to_visit)
