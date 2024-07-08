"""
"""


def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


while True:
    # Input temperature in Fahrenheit
    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Display the result
    print(
        f"\n{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.\n")

    # Check if the user wants to continue
    continue_choice = input(
        "Do you want to convert another temperature? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        break

print("Goodbye!")
