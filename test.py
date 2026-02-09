def initial_list():
    """
    Continuously ask the user for names and build a list.
    Stops when the user types 'done' (case-insensitive).
    Returns the completed list of names.
    """
    names = []

    while True:
        name = input("Enter a name and type 'done' when you're done: ")

        # Stop condition: if user types 'done', do NOT add it to the list
        if name.strip().lower() == "done":
            break

        # Add the name to the list
        names.append(name)

    return names


# Build the initial list
names = initial_list()

# Ask the user what they want to do next
choice = input(
    "Do you want to add a value or remove by index and return the updated list? (add/pop): "
).strip().lower()

if choice == "add":
    # Get the new name and add it to the list
    name_to_add = input("Enter the name you want to add: ")
    names.append(name_to_add)

    print("Name added.")
    print("Final list:", names)

elif choice == "pop":
    # If the list is empty, popping doesn't make sense
    if not names:
        print("The list is empty. Nothing to remove.")
    else:
        # Ask for the index to remove
        index = int(
            input(f"Enter the index to remove (0 to {len(names) - 1}): "))

        # Validate the index to avoid crashing
        if index < 0 or index >= len(names):
            print("Invalid index. No item removed.")
        else:
            # Remove the item at the index and store it
            removed_value = names.pop(index)

            print(f"Removed value: {removed_value}")

            # ✅ This is the "latest list after the specific index is removed"
            print("Updated list:", names)

            # If you need to "return" it from a function, you'd do:
            # return names

else:
    print("Invalid choice. Please type 'add' or 'pop'.")
