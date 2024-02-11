class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

# Creating an instance of the Calculator class
calculator = Calculator()

# Performing calculations
print("Addition:", calculator.add(5, 3))          # Output: 8
print("Subtraction:", calculator.subtract(8, 2))   # Output: 6
print("Multiplication:", calculator.multiply(4, 7))# Output: 28
print("Division:", calculator.divide(10, 2))       # Output: 5.0
print("Division by zero:", calculator.divide(8, 0)) # Output: Error: Cannot divide by zero


