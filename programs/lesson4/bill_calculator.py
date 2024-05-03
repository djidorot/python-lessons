
"""
Problem Statement:

You are tasked with developing a Python program to calculate the total cost of a meal, including tax and tip. Your program should prompt the user to enter the cost of the meal and the desired tip percentage, and then calculate and display the total cost.

Here are the requirements for your program:

1. Prompt the user to input the cost of the meal as a floating-point number.
2. Prompt the user to input the desired tip percentage as an integer. For example, if the user wants to leave a 15% tip, they should input '15'.
3. Calculate the total cost of the meal, including an 8% tax and the tip provided by the user.
4. Ensure that the tip percentage entered by the user is valid. If the tip percentage is less than 0, display an error message and prompt the user to enter a valid tip percentage.
5. Display the total cost of the meal, including tax and tip, rounded to two decimal places.

Your task is to implement the calculate_total_cost function, which takes the cost of the meal and the tip percentage as arguments, and returns the total cost of the meal. Additionally, you need to write the code to prompt the user for input, call the calculate_total_cost function, and display the total cost of the meal.

"""


def calculate_total_cost(meal_cost, tip_percentage):
    tax_rate = 0.08
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * (tip_percentage / 100)
    return meal_cost + tax_amount + tip_amount


meal_cost = float(input("\nEnter the cost of the meal: $"))
tip_percentage = float(input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

total_cost = calculate_total_cost(meal_cost, tip_percentage)
print(f"\nThe total cost of the meal, including tax and tip, is: ${total_cost:.2f}\n")


