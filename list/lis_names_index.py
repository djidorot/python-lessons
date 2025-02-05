# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    # Get user input
    name = input("\nEnter a name (or type 'done' to finish): ")
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Print the updated list of names with their index using index()
for name in names:
    print(f"Index {names.index(name)}: {name}")
