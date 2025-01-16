# Function to remove the last character from a string
def remove_last_character(text):
    if len(text) > 1:
        return text[:-1]  # Returns the string excluding the last character
    return text  # Returns the string unchanged if it has 1 or fewer characters

# Test the function
input_text = input("Enter a string: ")
result = remove_last_character(input_text)
print("Result:", result)
