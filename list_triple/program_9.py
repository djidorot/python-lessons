# Program 9: count(), append(), clear()

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

search_num = int(input("Enter number to count: "))
print("Count:", numbers.count(search_num))

new_num = int(input("Enter number to append: "))
numbers.append(new_num)
print("After append:", numbers)

confirm = input("Do you want to clear the list? (yes/no): ").lower()
if confirm == "yes":
    numbers.clear()
    print("After clear:", numbers)
else:
    print("List not cleared:", numbers)
