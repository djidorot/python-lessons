# Program 4: append(), count(), sort()

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

new_num = int(input("Enter a number to append: "))
numbers.append(new_num)
print("After append:", numbers)

search_num = int(input("Enter number to count: "))
print("Count:", numbers.count(search_num))

numbers.sort()
print("After sort:", numbers)
