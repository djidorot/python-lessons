# Program 7: insert(), remove(), sort()

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

position = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))
numbers.insert(position, value)
print("After insert:", numbers)

remove_num = int(input("Enter number to remove: "))
if remove_num in numbers:
    numbers.remove(remove_num)
    print("After remove:", numbers)
else:
    print(remove_num, "not found in list.")

numbers.sort()
print("After sort:", numbers)
