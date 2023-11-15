
"""
https://www.programiz.com/python-programming/break-continue
"""

# Ticket price constants
TICKET_PRICE = 100
FREE_TICKET_AGE_LIMIT = 3

# Initialize total price
total_price = 0

# Loop to input ages and calculate total price
for i in range(5):
    age = int(input(f"Enter age of passenger {i + 1}: "))

    # Check if the passenger is under 3 years old (ticket is free)
    if age < FREE_TICKET_AGE_LIMIT:
        print(f"Passenger {i + 1}: Ticket is free")
    else:
        total_price += TICKET_PRICE
        print(f"Passenger {i + 1}: ${TICKET_PRICE}")

# Print the total ticket price
print(f"Total ticket price for the passengers: ${total_price}")
