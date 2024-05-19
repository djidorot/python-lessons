"""
Problem Statement:

Suppose we have a decimal number, 37.45. We want to increase it by 6.25%. Write a Python program that calculates the result after applying this percentage increase and displays it rounded to two decimal places.

Task:

Multiply the decimal number 37.45 by 1.0625 (which represents the percentage increase).
Round the result to two decimal places.

Expected Output: The final result should be displayed as 39.79.
"""

from decimal import Decimal
print(f"{Decimal('37.45') * Decimal('1.0625'):.2f}")
