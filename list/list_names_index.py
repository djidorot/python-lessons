# Define a function to collect names and display them
def collect_and_display_names():
    # Create an empty list
    names = []

    # Use a while loop to add names to the list
    while True:
        # Get user input
        name = input("\nEnter a name (or type 'done' to finish): ")
        if name.lower() == 'done':  # Exit condition
            break
        names.append(name)  # Add the name to the list

    # Print the updated list of names with their index
    print("\nList of names with indices:")
    for index, name in enumerate(names):  # Use enumerate for index tracking
        print(f"Index {index}: {name}")


# Call the function
collect_and_display_names()
