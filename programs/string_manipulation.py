"""
User Input:

The program starts by prompting the user to enter a sentence using the input() function. The entered sentence is stored in the variable user_input.
String Manipulations:

The program performs several string manipulations on the user_input variable:
upper_case: Converts the user's input to uppercase using the .upper() method.
lower_case: Converts the user's input to lowercase using the .lower() method.
input_length: Calculates and stores the length (number of characters) of the user's input using the len() function.
title_case: Capitalizes the first letter of each word in the user's input using the .title() method.
Searching for a Word:

The program then prompts the user to enter a word to search for within the original input using another input() statement. The entered word is
stored in the search_word variable.
It checks if the search_word is present in the user_input using the in keyword and stores the result in the word_found variable.
Finding the Position:

If the search_word is found in the user_input, the program finds and stores the position (index) of the first occurrence of the search_word
within the user_input using the .find() method. If the word is not found, it sets word_position to -1.
Displaying Results:

Finally, the program displays the following results:
The original user input.
The user input converted to uppercase.
The user input converted to lowercase.
The length of the user input.
The user input in title case.
Whether the search_word was found in the user input and, if found, its position within the input.
"""

# Get user input
user_input = input("Enter a sentence: ")

# Convert the input to uppercase and lowercase
upper_case = user_input.upper()
lower_case = user_input.lower()

# Calculate the length of the input
input_length = len(user_input)

# Capitalize the first letter of each word in the input
title_case = user_input.title()

# Check if a specific word is present in the input
search_word = input("Enter a word to search for: ")
word_found = search_word in user_input

# Find the position of a specific word in the input
if word_found:
    word_position = user_input.find(search_word)
else:
    word_position = -1

# Display the results
print("\nOriginal Input: " + user_input)
print("Uppercase: " + upper_case)
print("Lowercase: " + lower_case)
print("Length of Input: " + str(input_length))
print("Title Case: " + title_case)

if word_found:
    print(f"'{search_word}' found at position {word_position}.")
else:
    print(f"'{search_word}' not found in the input.")
