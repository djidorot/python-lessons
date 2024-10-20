"""

"""

names = []

print()
while True:
    name = input("Enter a name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    names.append(name)

print("\nNames entered:")
for name in names:
    print(name)

print()
