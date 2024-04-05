# Get user input
"""
Problem Statement: User Input Collector
You are tasked with creating a Python program that collects user input and displays the information gathered. The program should prompt the user for the following details:

Name: The user's name.
Age: The user's age.
Hobbies: A list of the user's hobbies (separated by commas).
Favorite Place: The user's favorite place.
Favorite Books: A list of the user's favorite books (separated by commas).

The program should then print out the collected information in a clear and organized format.

Output:
What is your name? John Doe
How old are you? 25
What are your hobbies? Reading, hiking, cooking
What is your favorite place? Beach
What are your favorite books? "To Kill a Mockingbird", "1984", "Pride and Prejudice"

Name: John Doe
Age: 25
Hobbies: Reading, hiking, cooking
Favorite Place: Beach
Favorite Books: "To Kill a Mockingbird", "1984", "Pride and Prejudice"


"""


print()
name = input("What is your name? ")
age = input("How old are you? ")
hobbies = input("What are your hobbies? ")
favorite_place = input("What is your favorite place? ")
books = input("What are your favorite books? ")

# Print the collected information
print("\nName:", name)
print("Age:", age)
print("Hobbies:", hobbies)
print("Favorite Place:", favorite_place)
print("Favorite Books:", books)
print()
