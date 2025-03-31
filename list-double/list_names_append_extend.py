# Create an empty list
names = []

# Use a while loop to add names to the list
temp_names = []  # Temporary list to collect names
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    temp_names.append(name)  # Add the name to the temporary list

# Extend the main list with the collected names
names.extend(temp_names)

# Print the updated list of names
print(names)
