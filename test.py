def initial_list():
    while True:
        name = input("Enter a name and type 'done' when you're done: ")
        names.append(name)
        if name.lower() == 'done':
            break


names = []

initial_list()

choices = input("Do you want to add or remove a certain value? (add/remove) ")

names.remove("done")

if choices == "add":
    name_to_add = input("Enter in the name you want to be added: ")
    names.append(name_to_add)
    input("Name added. ")
    input("Final list: ")
    print(names)

if choices == "remove":
    value = input("What value do you want removed? ")
    names.remove(value)

print("Value removed. ")
print("Final list: ")
print(names)
