h = float(input("\nEnter your height in meters: "))
w = float(input("Enter your weight in kilograms: "))

BMI = w / (h ** 2)
BMI = round(BMI, 2)  # Round BMI to two decimal places

if BMI < 18.5:
    print(f"Your BMI is {BMI}, which means you are underweight.\n")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI}, which means you are normal.\n")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, which means you are overweight.\n")
else:
    print(f"Your BMI is {BMI}, which means you are obese.\n")
