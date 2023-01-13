import requests

# Define the endpoint for the API request
endpoint = "https://v2.jokeapi.dev/joke/Any"

# Make the API request and parse the response
response = requests.get(endpoint).json()


def joke():
    """
    This function returns the generated joke in string format.
    """
    if "setup" in response:
        # Extracting the setup and delivery from the response
        setup = response["setup"]
        delivery = response["delivery"]
        # returning the setup and delivery in string format
        return setup + "\n" + delivery
    else:
        # returning the joke
        return response["joke"]


# Storing the returned joke from the function in a variable
joke_str = joke()
# Printing the joke
print(joke_str)

# Taking user inputs
word_to_replace = input("Which word you want to replace? ")
final_word = input("Write a word for replacement: ")

# Replacing the word in the generated joke
new_joke = joke_str.replace(word_to_replace, final_word)
# Printing the new joke
print(new_joke)
