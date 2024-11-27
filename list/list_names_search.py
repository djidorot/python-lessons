# Define a function to get names from user input
def get_names():
    # Initialize an empty list to store names
    names = []

    # Print an empty line for spacing
    print()

    # Start an infinite loop to keep asking for names
    while True:
        # Prompt the user to enter a name, or 'exit' to finish
        name = input("Enter a name (or type 'exit' to finish): ")

        # Check if the entered name is 'exit' (case-insensitive)
        if name.lower() == 'exit':
            # If 'exit' is entered, break out of the loop
            break

        # If 'exit' was not entered, add the name to the list
        names.append(name)

    # Print a line break for spacing
    print("\nNames entered:")

    # Loop through the list of names and print each one
    for name in names:
        print(name)

    # Prompt the user to search for a name
    search_name = input("\nEnter a name to search for: ")

    # Check if the search name is in the list of names
    if search_name in names:
        print(f"{search_name} was found in the list!")
    else:
        print(f"{search_name} was not found in the list.")

    # Print a final line break for clean output formatting
    print()


# Call the function to execute the code
get_names()
