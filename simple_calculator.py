def calculator(first_number, operator, second_number):
    """
    This function takes in 3 arguments: first_number, operator and second_number
    and performs the operation based on the operator and returns the result.
    """
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
        return "Invalid operator"

    return result


# Get the first number from user
first_number = float(input("Enter the first number: "))

# Get the operator from user
operator = input("Enter the operator (+, -, *, /): ")

# Get the second number from user
second_number = float(input("Enter the second number: "))

# Call the calculator function and store the result
result = calculator(first_number, operator, second_number)

# Print the result
print("Result:", result)
