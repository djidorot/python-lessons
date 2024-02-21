"""
Enter Numbers:

The program will prompt you to enter the first number. Input a numerical value and press Enter.
Next, you will be prompted to enter the second number. Input another numerical value and press Enter.

Comparison Result:
The program will compare the two numbers and display one of the following messages:
"{num1} is greater than {num2}"
"{num1} is equal to {num2}"
"{num1} is less than {num2}"
"The numbers are not directly comparable."

Continue or Stop:
After displaying the comparison result, the program will ask if you want to compare more numbers.
Type 'yes' to continue or 'no' to exit the program.

Repeat as Desired:
If you choose to continue, the program will prompt you to enter two new numbers, and the process will repeat.
If you choose to stop by entering 'no', the program will terminate.


Enter the first number: 10
Enter the second number: 5
10.0 is greater than 5.0
Do you want to compare more numbers? (yes/no): yes
Enter the first number: 8
Enter the second number: 8
8.0 is equal to 8.0

Do you want to compare more numbers? (yes/no): no

"""

while True:
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Compare the two numbers
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 == num2:
        print(f"{num1} is equal to {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print("The numbers are not directly comparable.")

    # Ask the user if they want to continue
    user_input = input("Do you want to compare more numbers? (yes/no): ").lower()

    # Check if the user wants to continue or not
    if user_input != 'yes':
        break  # Exit the loop if the user enters anything other than 'yes'
