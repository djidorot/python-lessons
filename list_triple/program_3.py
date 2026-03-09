def manage_names(names_list):
    """
    Manages a list by allowing user input to add, clear, or finish input.
    Supports adding multiple names separated by commas.
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
            # Using extend() if user enters multiple names separated by commas
            if ',' in name:
                # Split input into names, strip whitespace, and extend the list
                multiple_names = [n.strip() for n in name.split(',')]
                names_list.extend(multiple_names)  # <-- extend() is used here
                print(f"Added multiple names: {multiple_names}")
            else:
                names_list.append(name)
                print(f"Added: {name}")


# Create an empty list
names = []

# Call the function
manage_names(names)

# Print the updated list of names
print("\nFinal list of names:")
print(names)
