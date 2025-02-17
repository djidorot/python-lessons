# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    action = input(
        "\nWould you like to add a name or insert at a specific position? (type 'add', 'insert', or 'done'): ").lower()

    if action == 'done':  # Exit condition
        break
    elif action == 'add':  # Add name to the end of the list
        name = input("Enter a name: ")
        names.append(name)  # Add the name to the list
    elif action == 'insert':  # Insert name at a specific position
        name = input("Enter a name: ")
        # Get position from user
        position = int(input(f"Enter the position (0 to {len(names)}): "))
        if 0 <= position <= len(names):  # Ensure position is valid
            # Insert the name at the specified position
            names.insert(position, name)
        else:
            print("Invalid position. Try again.")
    else:
        print("Invalid action. Please type 'add', 'insert', or 'done'.")

# Print the updated list of names
print(names)
