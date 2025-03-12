# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break

    position = input(
        "Enter position to insert the name or press Enter to add at the end: ")
    if position.isdigit():
        position = int(position)
        if 0 <= position <= len(names):
            names.insert(position, name)  # Insert at the specified position
        else:
            print(f"Invalid position. Adding '{name}' to the end.")
            names.append(name)
    else:
        names.append(name)  # Add to the end if no position is given

# Print the updated list of names
print(names)
