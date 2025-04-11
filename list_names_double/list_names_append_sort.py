# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Sort the list alphabetically
names.sort()

# Print the sorted list of names
print(names)
