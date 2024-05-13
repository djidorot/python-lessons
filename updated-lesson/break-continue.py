
"""
https://www.programiz.com/python-programming/break-continue
"""

# Price of a single ticket
ticket_price = 100

# Input ages of passengers
passenger_ages = []
for i in range(5):
    age = int(input("Enter the age of passenger {}: ".format(i + 1)))
    passenger_ages.append(age)

# Calculate and output the total ticket price
total_price = 0
for age in passenger_ages:
    if age < 3:
        # Ticket is free for children under 3
        total_price += 0
    else:
        total_price += ticket_price

print("Total ticket price for {} passengers: ${}".format(
    len(passenger_ages), total_price))
