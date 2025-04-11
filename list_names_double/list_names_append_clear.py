# # Create an empty list
# names = []

# # Use a while loop to add names to the list
# while True:
#     # Get user input
#     name = input(
#         "\nEnter a name (or type 'done' to finish, 'clear' to reset): ")
#     if name.lower() == 'done':  # Exit condition
#         break
#     elif name.lower() == 'clear':  # Clear the list
#         names.clear()
#         print("List cleared!")
#     else:
#         names.append(name)  # Add the name to the list

# # Print the updated list of names
# print(names)

##########################

def manage_names(names_list):
    """
    Manages a list by allowing user input to add, clear, or finish input.
    :param names_list: List to store names
    """
    while True:
        name = input(
            "\nEnter a name (or type 'done' to finish, 'clear' to reset): ")
        if name.lower() == 'done':
            break
        elif name.lower() == 'clear':
            names_list.clear()
            print("List cleared!")
        else:
            names_list.append(name)


# Create an empty list
names = []

# Call the function
manage_names(names)

# Print the updated list of names
print(names)
