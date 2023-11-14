
# Concatenation:
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World


# Repetition:
str1 = "Hello"
result = str1 * 3
print(result)  # Output: HelloHelloHello


# Indexing:
my_string = "Python"
print(my_string[0])  # Output: P
print(my_string[2])  # Output: t


# Slicing:
my_string = "Python"
sub_string = my_string[1:4]
print(sub_string)  # Output: yth


# String Length:
my_string = "Hello, World!"
length = len(my_string)
print(length)  # Output: 13


# String Methods:
my_string = "   Hello, World!   "
print(my_string.upper())         # Output: HELLO, WORLD!
print(my_string.strip())         # Output: Hello, World!
print(my_string.replace('o', 'a'))  # Output:   Hella, Warld!


# Formatting Strings:
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Alice and I am 25 years old.

print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.


# String Interpolation (f-strings):
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.


# Example Program
# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# String Repetition
str3 = "Python"
repeated_str = str3 * 3
print("Repetition:", repeated_str)

# String Indexing
my_string = "Python"
print("Indexing:", my_string[0])  # Output: P

# String Slicing
sub_string = my_string[1:4]
print("Slicing:", sub_string)  # Output: yth

# String Length
length = len(my_string)
print("Length:", length)  # Output: 6

# String Methods
sample_string = "   Hello, World!   "
print("Uppercase:", sample_string.upper())
print("Stripped:", sample_string.strip())
print("Replaced:", sample_string.replace('o', 'a'))

# String Formatting
name = "Alice"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatting:", formatted_string)

# String Interpolation (f-strings)
interpolated_string = f"My name is {name} and I am {age} years old."
print("Interpolation:", interpolated_string)
