"""

"""

names = []

name = input("Enter a name (or type 'exit' to finish): ")
names.append(name)

name = input("Enter another name (or type 'exit' to finish): ")
names.append(name)

name = input("Enter another name (or type 'exit' to finish): ")
names.append(name)

# ... you would continue this for as many names as you want to input

print("Names entered:")
for name in names:
    if name.lower() != 'exit':
        print(name)
