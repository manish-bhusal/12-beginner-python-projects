class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        return self.first_number / self.second_number


# Get the first number from user
first_number = float(input("Enter the first number: "))

# Get the operator from user
operator = input("Enter the operator (+, -, *, /): ")

# Get the second number from user
second_number = float(input("Enter the second number: "))

# Create an instance of the Calculator class
calculator = Calculator(first_number, second_number)

# Perform the operation based on the operator
if operator == "+":
    result = calculator.add()
elif operator == "-":
    result = calculator.subtract()
elif operator == "*":
    result = calculator.multiply()
elif operator == "/":
    result = calculator.divide()
else:
    print("Invalid operator")
    result = None

# Print the result
if result is not None:
    print("Result:", result)
