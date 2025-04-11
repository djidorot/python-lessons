# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    # Get user input
    name = input(
        "\nEnter a name (or type 'done' to finish, or 'pop' to remove the last name): ")
    if name.lower() == 'done':  # Exit condition
        break
    elif name.lower() == 'pop':  # Remove the last name if 'pop' is entered
        if names:  # Check if the list is not empty
            removed_name = names.pop()  # Remove the last name
            print(f"Removed: {removed_name}")
        else:
            print("The list is already empty, nothing to remove.")
    else:
        names.append(name)  # Add the name to the list

# Print the updated list of names
print(names)
