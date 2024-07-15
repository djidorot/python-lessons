"""

"""


def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


while True:
    try:
        # Input temperature in Celsius
        celsius = float(
            input("\nEnter temperature in Celsius (or type 'q' to quit): "))

        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)

        # Display the result
        print(
            f"\n{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.\n")
    except ValueError:
        # Check if user wants to quit
        user_input = input("\nType 'q' to quit or 'c' to continue: ").lower()
        if user_input == 'q':
            print("Goodbye!")
            break
        elif user_input == 'c':
            continue
        else:
            print("Invalid input. Please try again.")


