# Define a function to collect names
def collect_names():
    # Initialize an empty list to store names
    names = []

    # Print an empty line for spacing
    print()

    # Start an infinite loop to keep asking for names
    while True:
        # Prompt the user to enter a name, 'clear' to reset the list, or 'exit' to finish
        name = input(
            "\nEnter a name (or type 'clear' to reset, 'exit' to finish): ")

        # Check if the entered name is 'exit' (case-insensitive)
        if name.lower() == 'exit':
            # If 'exit' is entered, break out of the loop
            break
        elif name.lower() == 'clear':
            # If 'clear' is entered, empty the list
            names.clear()
            print("List cleared.")
        else:
            # If neither 'exit' nor 'clear' was entered, add the name to the list
            names.append(name)

    # Print a line break for spacing
    print("\nNames entered:")

    # Loop through the list of names and print each one
    for name in names:
        print(name)

    # Print a final line break for clean output formatting
    print()


# Call the function to run the name collection program
collect_names()
