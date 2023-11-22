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
