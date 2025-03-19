# Create an empty list
names = []
print()
# Use a while loop to add names to the list
while True:
    # Get user input
    name = input("Enter a name (or type 'done' to finish): ")
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Create a copy of the list
names_copy = names.copy()

# Print the original and copied lists
print("\nOriginal list:", names)
print("Copied list:", names_copy)
print()
