# Program 11: append(), pop(), reverse()

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

new_num = int(input("Enter number to append: "))
numbers.append(new_num)
print("After append:", numbers)

pop_index = int(input("Enter index to pop: "))
if 0 <= pop_index < len(numbers):
    removed = numbers.pop(pop_index)
    print("Removed:", removed)
    print("After pop:", numbers)
else:
    print("Invalid index.")

numbers.reverse()
print("After reverse:", numbers)
