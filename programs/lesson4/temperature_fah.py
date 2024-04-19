"""
Problem Statement:

Write a Python program called "Temperature Converter" that prompts the user to enter a temperature in Fahrenheit and converts it to Celsius using a defined function.

Your program should include the following steps:
1. Define a function called fahrenheit_to_celsius that takes one parameter fahrenheit representing the temperature in Fahrenheit. This function should return the equivalent temperature in Celsius calculated using the formula (fahrenheit - 32) * 5/9.
2. Prompt the user to input the temperature in Fahrenheit.
3. Convert the Fahrenheit temperature to Celsius using the fahrenheit_to_celsius function.
4. Print the original Fahrenheit temperature and the converted Celsius temperature with two decimal places.

"""


def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# Input temperature in Fahrenheit
fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print(f"\n{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.\n")
