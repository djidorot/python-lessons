def get_names():
    # Initialize an empty list to store names
    names = []

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

    # Sort the names alphabetically by first letter
    names.sort()

    # Reverse the sorted list
    names.reverse()

    # Print the names in reverse alphabetical order
    print("\nNames entered in reverse alphabetical order:")
    for name in names:
        print(name)


# Call the function to execute the code
get_names()
