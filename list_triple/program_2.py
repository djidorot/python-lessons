# Program 3: extend(), remove(), reverse()

fruits = input("Enter fruits separated by space: ").split()
more_fruits = input("Enter more fruits to extend: ").split()

fruits.extend(more_fruits)
print("After extend:", fruits)

remove_item = input("Enter fruit to remove: ")
if remove_item in fruits:
    fruits.remove(remove_item)
    print("After remove:", fruits)
else:
    print(remove_item, "not found in list.")

fruits.reverse()
print("After reverse:", fruits)
