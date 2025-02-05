# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Create a copy of the names list
names_copy = names.copy()

# Print the updated list of names and its copy
print("Original list:", names)
print("Copied list:", names_copy)
