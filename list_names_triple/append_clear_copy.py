def process_names(name_list):
    # Use a while loop to add names to the list
    while True:
        # Get user input
        name = input("\nEnter a name (or type 'done' to finish): ")
        if name.lower() == 'done':  # Exit condition
            break
        name_list.append(name)  # Add the name to the list

    # Make a copy of the list before clearing
    name_list_copy = name_list.copy()

    # Clear the original list
    name_list.clear()

    # Print the copied list (before clearing)
    print("Copied list of names:", name_list_copy)

    # Print the original list (after clearing)
    print("Original list after clearing:", name_list)


# Create an empty list and call the function
names = []
process_names(names)
