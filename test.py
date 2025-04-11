# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Make a copy of the list before clearing
names_copy = names.copy()

# Clear the original list
names.clear()

# Print the copied list (before clearing)
print("Copied list of names:", names_copy)

# Print the original list (after clearing)
print("Original list after clearing:", names)
