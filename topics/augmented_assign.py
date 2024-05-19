# total = 0

# for number in [1, 2, 3, 4, 5]:
#     total += number  # add number to total and store in number

# total


# Exercise 2
"""
Problem Statement: Suppose we want to find the sum of all positive integers from 1 to 1,000,000 (inclusive). Write a program or calculate the result manually.

Task: Find the sum of all positive integers from 1 to 1,000,000.

Solution: The sum of these integers is 500,000,500,000.
"""

total = 0

for number in range(1000001):
    total = total + number

print(total)
