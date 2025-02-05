# Define a function to collect names
def collect_names():
    names = []  # Initialize an empty list
    while True:
        # Get user input
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':  # Exit condition
            break
        names.append(name)  # Add the name to the list
    return names  # Return the list of names


# Main program
# Call the function to collect names from the user
names = collect_names()

# Define a list of additional names
additional_names = ['Alice', 'Bob', 'Charlie']

# Use extend() to add all the names from the additional_names list to the names list
names.extend(additional_names)

# Print the updated list of names
print("Updated list of names:", names)
