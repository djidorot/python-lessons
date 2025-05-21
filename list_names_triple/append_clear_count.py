def manage_names(names_list):
    """
    Manages a list by allowing user input to add, clear, or finish input.
    :param names_list: List to store names
    """
    while True:
        name = input(
            "\nEnter a name (or type 'done' to finish, 'clear' to reset): ")
        if name.lower() == 'done':
            break
        elif name.lower() == 'clear':
            names_list.clear()
            print("List cleared!")
        else:
            names_list.append(name)
            print(f"Name added. Total names in the list: {len(names_list)}")


# Create an empty list
names = []

# Call the function
manage_names(names)

# Print the updated list of names
print("\nFinal list of names:")
print(names)
