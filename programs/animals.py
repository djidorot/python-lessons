"""

Programming Exercise: Animal List Management

Objective: Practice basic list manipulation in Python.

Instructions:

Initialize List: The code provided initializes an empty list named animals. This list will be used to store the names of various animals.

Menu Options:
The program presents a menu to the user with the following options:
Option 1: Add an Animal
Option 2: Display Animals
Option 3: Exit

Add an Animal (Option 1):
If the user selects option 1, the program prompts the user to enter the name of an animal.
The entered animal's name is then added to the animals list.
A confirmation message is printed, indicating that the animal has been added to the list.

Display Animals (Option 2):
If the user selects option 2, the program checks if the animals list is empty.
If the list is empty, a message is printed, indicating that the list is empty.
If the list is not empty, the program prints the names of all animals in the list.

Exit (Option 3):
If the user selects option 3, the program prints a farewell message and exits the main program loop.

Invalid Choice:
If the user enters a choice other than 1, 2, or 3, the program prints an error message, prompting the user to enter a valid choice.

Your Task:
Run the provided code.
Interact with the program by choosing different options from the menu.
Add at least three different animals to the list.
Display the list of animals.
Exit the program.
"""

# Initialize an empty list to store animals
animals = []

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add an animal")
    print("2. Display animals")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        animal = input("Enter the name of the animal: ")
        animals.append(animal)
        print(f"{animal} has been added to the list.")

    elif choice == "2":
        if not animals:
            print("The list is empty.")
        else:
            print("List of animals:")
            for animal in animals:
                print(animal)

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
