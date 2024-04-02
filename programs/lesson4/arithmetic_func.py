"""
Problem Statement: Basic Arithmetic Operations

You are tasked with writing a Python program to perform basic arithmetic operations on two numbers. Your program should include functions for addition, subtraction, multiplication, division, exponentiation, and modulo operations.

Your task is to complete the provided Python script by implementing the required functions and testing them with given values.

Instructions:

Define the following functions:
    addition(a, b): Returns the sum of two numbers.
    subtraction(a, b): Returns the difference between two numbers.
    multiplication(a, b): Returns the product of two numbers.
    division(a, b): Returns the result of dividing the first number by the second number.
    exponentiation(a, b): Returns the first number raised to the power of the second number.
    modulo(a, b): Returns the remainder when the first number is divided by the second number.

Test each function with the provided values:
    a = 5
    b = 3
    
"""


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def exponentiation(a, b):
    return a ** b


def modulo(a, b):
    return a % b


# Test the functions
a = 5
b = 3

result_addition = addition(a, b)
print("Addition:", result_addition)

result_subtraction = subtraction(a, b)
print("Subtraction:", result_subtraction)

result_multiplication = multiplication(a, b)
print("Multiplication:", result_multiplication)

result_division = division(a, b)
print("Division:", result_division)

result_exponentiation = exponentiation(a, b)
print("Exponentiation:", result_exponentiation)

result_modulo = modulo(a, b)
print("Modulo:", result_modulo)
