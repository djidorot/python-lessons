"""

"""


def main():
    names = []
    print()
    while True:
        print("\nCurrent names:", ", ".join(names)
              if names else "No names entered yet.")
        choice = input(
            "Do you want to continue? Type 'yes' to continue or 'done' to finish: ").lower()

        if choice == 'done':
            break
        elif choice == 'yes':
            name = input(
                "Enter a name (or type 'remove' to delete a name): ").lower()
            if name == 'remove':
                if names:
                    remove_name = input("Enter the name you want to remove: ")
                    if remove_name in names:
                        names.remove(remove_name)
                        print(f"{remove_name} has been removed.")
                    else:
                        print(f"{remove_name} is not in the list.")
                else:
                    print("The list is empty, nothing to remove.")
            else:
                names.append(name)
        else:
            print("Invalid choice. Please enter 'yes' to continue or 'done' to finish.")

    print(f"\nYou entered {len(names)} names.")
    print("The names you entered are:")
    for name in names:
        print(name)


main()
