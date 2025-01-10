def clarification(names):
    """Confirms deletion of the last name from the list."""
    clarify = input(
        f"Are you sure you want to delete {names[-1]}? (yes or no): ")
    if clarify.lower() == "yes":
        removed_name = names.pop()  # Removes the last name from the list
        print(f"{removed_name} has been deleted.")
    else:
        print("Okay, you may continue.")


def get_names2():
    """Handles name entry, deletion, and displaying the final list of names."""
    names = []
    while True:
        name = input(
            "Enter a name, type 'done' to finish or 'remove' to delete the last name from the list: ")
        if name.lower() == 'remove':
            if names:
                # Pass the names list to the clarification function
                clarification(names)
            else:
                print("No names to delete.")
        elif name.lower() == "done":
            print("\nFinal list of names:")
            for person in names:  # Avoid shadowing the input variable 'name'
                print(person)
            break
        else:
            names.append(name)  # Add the entered name to the list


# Run the corrected function
get_names2()
