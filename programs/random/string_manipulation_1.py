"""
str.upper() and str.lower():
These methods convert a string to all uppercase or all lowercase letters, respectively.
"""
text = "The quick brown fox"
print("The quick brown fox - default text\n")
upper_text = text.upper()  # Converts to uppercase
lower_text = text.lower()  # Converts to lowercase
print(upper_text)  # Output: "HELLO, WORLD!"
print(lower_text)  # Output: "hello, world!"
print()


"""
str.find() and str.index():
These methods search for a substring within a string and return the index of the first occurrence.
str.find() returns -1 if not found, while str.index() raises an exception.
"""

index1 = text.find("quick")  # Returns index of 'quick'
index2 = text.find("lazy")   # Returns -1 (not found)
print(index1)  # Output: 4
print(index2)  # Output: -1
print()


"""
str.title():
Capitalizes the first letter of each word in the string.
"""

title_text = text.title()
print(title_text)  # Output: "This Is A Title"
