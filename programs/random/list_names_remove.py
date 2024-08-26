"""
"""


def main():
    names = []
    print()
    while True:
        name = input(
            "Enter a name (or type 'done' to finish, or 'remove' to delete a name): ")
        if name.lower() == 'done':
            break
        elif name.lower() == 'remove':
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

    print(f"\nYou entered {len(names)} names.")
    print("The names you entered are:")
    for name in names:
        print(name)


main()
