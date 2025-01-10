# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Define a list of additional names
additional_names = ['Alice', 'Bob', 'Charlie']

# Use extend() to add all the names from the additional_names list to the names list
names.extend(additional_names)

# Print the updated list of names
print(names)
