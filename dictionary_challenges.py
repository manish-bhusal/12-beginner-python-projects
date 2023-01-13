# Challenge No. 1
# Create a dictionary called student that contains the keys "name", "age", and "courses". Assign the corresponding values to these keys. Then, print the name of the student.

# Creating the dictionary
student = {
    "name": "Manish",
    "age": 20,
    "courses": ["Python", "Java", "Git and GitHub", "JavaScript"]
}

# Printing the name of the student
print(student.get("name"))

# Challenge No. 2
# Create a dictionary called employee that contains the keys "name", "age", and "position". Assign the corresponding values to these keys. Then, use the items() method to access the key-value pairs of the dictionary, and print them.

# Creating the dictionary
employee = {
    "name": "Manish", "age": 20, "position": "Developer"
}

# Accessing key-value pairs of the dictionary using for loop
for key, value in employee.items():
    print(key, value)

# Challenge No. 3
# Create a dictionary called phone_numbers that contains the keys "John", "Jane", and "Bob". Assign phone numbers as the corresponding values to these keys. Then, use the del statement to remove the key-value pair of the "Jane" and print the dictionary.

# Creating the dictionary
phone_numbers = {"John": "+1234567890",
                 "Jane": "+0987654321", "Bob": "+1029384756"}

# Removing the key-value pair of the "Jane"
del phone_numbers["Jane"]

# Printing the dictionary
print(phone_numbers)


# Challenge No. 4
# Create a dictionary called book_store that contains the keys "book_name", "author", and "price". Assign the corresponding values to these keys. Then, use the setdefault() method to set the value of the key "discount" to 10 if it's not already present, and print the dictionary.

# Creating the dictionary
book_store = {"book_name": "Harry Potter",
              "author": "J.K. Rowling", "price": 20.99}

# Setting the value of the key "discount" to 10 if it's not already present
book_store.setdefault("discount", 10)

# You could also use an if-else statement to check if the key "discount" is present in the dictionary, and add it if it's not:
if "discount" not in book_store:
    book_store["discount"] = 10

# Printing the dictionary
print(book_store)
