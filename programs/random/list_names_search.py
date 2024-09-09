"""
"""


names = []

# Input names until 'exit' is entered
while True:
    name = input("Enter a name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    names.append(name)

# Print the entered names
print("Names entered:")
for name in names:
    print(name)

# Search for a name in the list
search_name = input("Enter a name to search: ")

# Check if the name exists in the list
if search_name in names:
    print(f"{search_name} is in the list.")
else:
    print(f"{search_name} is not in the list.")
