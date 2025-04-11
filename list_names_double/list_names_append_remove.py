# Create an empty list
names = []

# Use a while loop to add or remove names from the list
while True:
    # Get user input
    name = input(
        "Enter a name (type 'done' to finish, or 'remove' to delete a name): ")

    if name.lower() == 'done':  # Exit condition
        break
    elif name.lower() == 'remove':
        to_remove = input("Enter the name to remove: ")
        if to_remove in names:
            names.remove(to_remove)
            print(f"{to_remove} removed.")
        else:
            print(f"{to_remove} not found in the list.")
    else:
        names.append(name)  # Add the name to the list

# Print the updated list of names
print("Final list of names:", names)
