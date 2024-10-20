# Define the main function
def main():
    # Initialize an empty list to store names
    names = []

    # Print an empty line for spacing (optional)
    print()

    # Infinite loop to keep prompting the user for input
    while True:
        # Prompt the user to enter a name, or type 'done' to finish, or 'remove' to delete a name
        name = input(
            "Enter a name (or type 'done' to finish, or 'remove' to delete a name): ")

        # If the user enters 'done', exit the loop
        if name.lower() == 'done':
            break

        # If the user enters 'remove', prompt to remove a name from the list
        elif name.lower() == 'remove':
            # Check if the list contains any names
            if names:
                # Prompt the user to enter the name they want to remove
                remove_name = input("Enter the name you want to remove: ")

                # If the entered name exists in the list, remove it
                if remove_name in names:
                    names.remove(remove_name)
                    # Confirmation message
                    print(f"{remove_name} has been removed.")

                # If the name is not in the list, inform the user
                else:
                    print(f"{remove_name} is not in the list.")
            # If the list is empty, inform the user there's nothing to remove
            else:
                print("The list is empty, nothing to remove.")

        # If the user enters a valid name, add it to the list
        else:
            names.append(name)

    # After the loop ends, print how many names were entered
    print(f"\nYou entered {len(names)} names.")

    # Print all the names the user entered
    print("The names you entered are:")

    # Loop through each name in the list and print it
    for name in names:
        print(name)


# Call the main function to execute the program
main()
