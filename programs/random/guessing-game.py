"""
Guessing Game Number in Python

Description:

Create a simple Python program for a guessing game. The program generates a random number between 1 and 100 (or use a fixed number of your choice) that the user has to guess. The program should use input, while loops, and if statements.

Instructions:

Initialize a secret number (either randomly generated or fixed).
Display a welcome message and instructions to the user.
Use a while loop to repeatedly prompt the user for guesses until they guess correctly.
Inside the loop, use an if statement to compare the user's guess with the secret number and provide feedback (too low, too high, or correct).
Track the number of attempts.
Once the user guesses correctly, print a congratulatory message along with the secret number and the number of attempts.

"""

# Set a fixed secret number
secret_number = 42

print("Welcome to the Guessing Game Number!")
print("Try to guess the number between 1 and 100.")

# Initialize variables
attempts = 0
guess = None

while guess != secret_number:
    # Get user input
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(
            f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
