import random
import string

# User input
letters = int(input("How many letters do you want in your password? "))
numbers = int(input("How many numbers do you want in your password? "))
special_characters = int(
    input("How many special characters do you want in your password? "))

# Lists of characters to choose from
ascii_letters = list(string.ascii_letters)
digits = list(string.digits)
punctuations = list(string.punctuation)

# Using list comprehension to generate a list of random letters
random_letters = [random.choice(ascii_letters) for _ in range(letters)]

# Using list comprehension to generate a list of random numbers
random_numbers = [random.choice(digits) for _ in range(numbers)]

# Using list comprehension to generate a list of random special characters
random_characters = [random.choice(punctuations)
                     for _ in range(special_characters)]

# Concatenate all the lists to make a single list
password_list = random_letters + random_numbers + random_characters

# Shuffle the list
random.shuffle(password_list)

# join all the elements in password_list and assign the result to final_password
final_password = "".join(password_list)

# print the final password
print(f"Your password is {final_password}.")
