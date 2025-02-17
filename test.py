# Create an empty list
names = []

# Use a while loop to add names to the list
while True:
    # Get user input
    name = input("\nEnter a name (or type 'done' to finish): ")
    if name.lower() == 'done':  # Exit condition
        break
    names.append(name)  # Add the name to the list

    # Display how many times the current name appears in the list
    print(f"The name '{name}' has been entered {names.count(name)} times.")

# Print the updated list of names
print("Final list of names:", names)
print()
