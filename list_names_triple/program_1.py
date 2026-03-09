# Program 1: append(), reverse(), sort()

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

new_num = int(input("Enter a number to append: "))
numbers.append(new_num)
print("After append:", numbers)

numbers.reverse()
print("After reverse:", numbers)

numbers.sort()
print("After sort:", numbers)
