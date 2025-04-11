"""

"""


def main():
    names = []
    print()
    while True:
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        names.append(name)

    print(f"\nYou entered {len(names)} names.")
    print("The names you entered are:")
    for name in names:
        print(name)


main()
