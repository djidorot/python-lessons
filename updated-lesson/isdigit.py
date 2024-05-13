"""
isdigit() is a method in Python that checks whether all characters in a string are digits. It returns True if all characters in the string are digits and there is at least one character, otherwise, it returns False.

Here's an example:
"""
string1 = "12345"
string2 = "abc123"
string3 = "123 456"

print(string1.isdigit())  # Output: True
print(string2.isdigit())  # Output: False
print(string3.isdigit())  # Output: False

"""
In this example, string1 consists only of digits, so isdigit() returns True. string2 contains alphabetic characters, so isdigit() returns False. string3 contains a space, so isdigit() also returns False.
"""
