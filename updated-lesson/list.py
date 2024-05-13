"""
In Python, a list is a built-in data structure used to store a collection of items. It's a mutable, ordered sequence of elements, meaning you can change its content, and the elements in a list maintain their order. Lists are versatile and can contain elements of different types, such as integers, strings, or even other lists.

You can create a list using square brackets [] and separating the elements with commas. Here's an example:
"""

my_list = [1, 2, 3, 4, 5]


"""
You can access elements in a list using indexing. Indexing starts from 0, so my_list[0] would give you the first element (1 in this case), my_list[1] would give you the second element (2), and so on.

Lists also support slicing, which allows you to access a subset of elements. For example, my_list[1:4] would give you a sublist containing elements from index 1 to 3 ([2, 3, 4]).

Lists offer various methods for adding, removing, and manipulating elements. Some common methods include append(), extend(), insert(), remove(), pop(), index(), count(), sort(), and reverse(). These methods make lists very flexible and powerful for managing collections of data in Python.
"""

# Example Program
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("Elements in the list:")
for element in my_list:
    print(element)

# Adding elements to the list
my_list.append(6)
print("After appending 6:", my_list)

# Removing an element
my_list.remove(3)
print("After removing 3:", my_list)

# Accessing a subset using slicing
print("Sublist from index 1 to 3:", my_list[1:4])

# Finding index of an element
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)

# Counting occurrences of an element
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)
