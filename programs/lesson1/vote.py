"""
Problem Statement:

Write a Python program that takes the user's age as input and determines if they are old enough to vote. If the user's age is less than 18, the program should print "You are not old enough to vote." If the user's age is 18 or older, the program should print "You are old enough to vote."

Your task is to:

    Prompt the user to enter their age.
    Convert the input to an integer.
    Use an if statement to check if the age is less than 18.
    If the age is less than 18, print "You are not old enough to vote."
    If the age is 18 or older, print "You are old enough to vote."

"""


# Take user input for age
age = int(input("Enter your age: "))

# Check if the age is old enough to vote
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")
