"""
Problem Statement:

Write a Python program called "Temperature Converter" that prompts the user to enter a temperature in Celsius and converts it to Fahrenheit using a defined function.

Your program should include the following steps:
1. Define a function called celsius_to_fahrenheit that takes one parameter celsius representing the temperature in 2. Celsius. This function should return the equivalent temperature in Fahrenheit calculated using the formula (celsius * 9/5) + 32.
3. Prompt the user to input the temperature in Celsius.
4. Convert the Celsius temperature to Fahrenheit using the celsius_to_fahrenheit function.
5. Print the original Celsius temperature and the converted Fahrenheit temperature with two decimal places.

"""


def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Input temperature in Celsius
celsius = float(input("\nEnter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"\n{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.\n")
