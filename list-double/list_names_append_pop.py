# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    name = input("Enter a name (or type 'done' to finish): ")  # Get user input
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

# Remove the last name added using pop()
if names:  # Check if the list is not empty to avoid an error
    removed_name = names.pop()
    print(f"Removed last name: {removed_name}")

# Print the updated list of names
print("Updated list of names:", names)
