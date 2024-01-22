# Personal Info
# Function

# Personal Information Program

def collect_and_display_information():
    # Get user input for personal information
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    occupation = input("Enter your occupation: ")

    # Display the collected information
    print("\nPersonal Information:")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Occupation:", occupation)


# Call the function
collect_and_display_information()


##############

def collect_and_display_information(name, age, city, occupation):
    # Display the collected information
    print("\nPersonal Information:")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Occupation:", occupation)


# Get user input for personal information
user_name = input("\nEnter your name: ")
user_age = input("Enter your age: ")
user_city = input("Enter your city: ")
user_occupation = input("Enter your occupation: ")

# Call the function with user inputs as parameters
collect_and_display_information(
    user_name, user_age, user_city, user_occupation)
