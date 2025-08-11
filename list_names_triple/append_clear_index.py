# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    # Get user input
    name = input(
        "\nEnter a name (or type 'done' to finish, 'clear' to reset): ")
    if name.lower() == 'done':  # Exit condition
        break
    elif name.lower() == 'clear':  # Clear the list
        names.clear()
        print("List cleared!")
    else:
        names.append(name)  # Add the name to the list

# Print the updated list of names with index
print("\nFinal list of names:")
for index, name in enumerate(names):
    print(f"{index}: {name}")
