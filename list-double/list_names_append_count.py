# Create an empty list
names = []

# Use a while loop to add names to the list
print()
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Print the updated list of names
print("Names entered:", names)

# Print the count of names
print("Total number of names entered:", len(names))
print()
