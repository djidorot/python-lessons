"""
Problem Statement:
You are tasked with creating a Python script to perform basic arithmetic operations on two numbers, num1 and num2. The script should calculate the following:

Addition of num1 and num2.
Subtraction of num2 from num1.
Multiplication of num1 and num2.
Division of num1 by num2.
Modulus of num1 divided by num2.
Exponentiation of num1 raised to the power of num2.

Use the given values:
num1 = 10
num2 = 3

Your script should print the results of each operation in the following format:

Addition: {num1} + {num2} = {addition_result}
Subtraction: {num1} - {num2} = {subtraction_result}
Multiplication: {num1} * {num2} = {multiplication_result}
Division: {num1} / {num2} = {division_result}
Modulus: {num1} % {num2} = {modulus_result}
Exponentiation: {num1} ** {num2} = {exponentiation_result}

Implement the Python script and verify that it produces the correct results.


"""

# Arithmetic Operators Program

# Hardcoded values for two numbers
num1 = 10
num2 = 3

# Performing basic arithmetic operations
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2
modulus_result = num1 % num2
exponentiation_result = num1 ** num2

# Printing the results
print(f"Addition: {num1} + {num2} = {addition_result}")
print(f"Subtraction: {num1} - {num2} = {subtraction_result}")
print(f"Multiplication: {num1} * {num2} = {multiplication_result}")
print(f"Division: {num1} / {num2} = {division_result}")
print(f"Modulus: {num1} % {num2} = {modulus_result}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation_result}")
