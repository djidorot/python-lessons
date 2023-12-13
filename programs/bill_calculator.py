"""
Program Description: Restaurant Bill Calculator

This Python program is designed to help students create a restaurant bill calculator. The program takes user input for the cost
of a meal and the desired tip percentage, then calculates and displays the total cost of the meal, including tax and tip.

User Input:

The program uses input statements to get two pieces of information from the user:
The cost of the meal (meal_cost), which should be a floating-point number (e.g., 25.99).
The desired tip percentage (tip_percentage), which should be a number representing the tip percentage (e.g., 15 for 15%).
Input Validation:

The program checks if the entered tip percentage is valid (greater than or equal to 0). If the tip percentage is negative,
it displays an error message and prompts the user to enter a valid tip percentage.
Calculating the Total Cost:

If the tip percentage is valid, the program calculates the total cost, including tax and tip.
Output:

The program displays the calculated total cost with two decimal places using a formatted string and the print function.
"""

# Get user input for meal cost and tip percentage
meal_cost = float(input("Enter the cost of the meal: $"))
tip_percentage = float(
    input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

# Check if the tip percentage is valid (greater than or equal to 0)
if tip_percentage < 0:
    print("Please enter a valid tip percentage.")
else:
    # Calculate the total cost including tax and tip
    tax_rate = 0.08  # 8% tax rate
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * (tip_percentage / 100)
    total_cost = meal_cost + tax_amount + tip_amount

    print(
        f"The total cost of the meal, including tax and tip, is: ${total_cost:.2f}")
