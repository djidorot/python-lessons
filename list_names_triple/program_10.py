# Program 10: insert(), index(), remove()

fruits = input("Enter fruits separated by space: ").split()

position = int(input("Enter position to insert: "))
new_fruit = input("Enter fruit to insert: ")
fruits.insert(position, new_fruit)
print("After insert:", fruits)

search_fruit = input("Enter fruit to find index: ")
if search_fruit in fruits:
    print("Index of", search_fruit, "is", fruits.index(search_fruit))
else:
    print(search_fruit, "not found in list.")

remove_fruit = input("Enter fruit to remove: ")
if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print("After remove:", fruits)
else:
    print(remove_fruit, "not found in list.")
