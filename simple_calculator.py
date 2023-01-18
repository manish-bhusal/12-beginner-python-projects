# Get the first number from user
first_number = float(input("Enter the first number: "))

# Get the operator from user
operator = input("Enter the operator (+, -, *, /): ")

# Get the second number from user
second_number = float(input("Enter the second number: "))

# Perform the operation based on the operator
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    print("Invalid operator")
    result = None

# Print the result
if result is not None:
    print("Result:", result)
