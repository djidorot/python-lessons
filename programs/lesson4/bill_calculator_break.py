"""

"""


def calculate_total_cost(meal_cost, tip_percentage):
    tax_rate = 0.08
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * (tip_percentage / 100)
    return meal_cost + tax_amount + tip_amount


while True:
    try:
        meal_cost = float(input("\nEnter the cost of the meal: $"))
        if meal_cost < 0:
            print("Error: The meal cost must be a positive number.")
            continue

        tip_percentage = float(
            input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))
        if tip_percentage < 0:
            print("Error: The tip percentage must be a positive number.")
            continue

        break  # Exit the loop if valid inputs are received
    except ValueError:
        print("Invalid input. Please enter numeric values.")

total_cost = calculate_total_cost(meal_cost, tip_percentage)
print(
    f"\nThe total cost of the meal, including tax and tip, is: ${total_cost:.2f}\n")
