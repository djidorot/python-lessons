"""
https://www.w3schools.com/python/ref_func_input.asp
"""

# Rectangle

# Input the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Check if it's a square or not
if length == width:
    shape = "square"
else:
    shape = "rectangle"

# Display the results
print(f"The area of the {shape} is {area}")
