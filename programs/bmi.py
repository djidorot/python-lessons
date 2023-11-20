h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kilograms: "))

BMI = w / (h ** 2)

if BMI < 18.5:
    print("Your BMI is", BMI, "which means you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print("Your BMI is", BMI, "which means you are normal.")
elif BMI >= 25 and BMI < 30:
    print("Your BMI is", BMI, "which means you are overweight.")
else:
    print("Your BMI is", BMI, "which means you are obese.")
