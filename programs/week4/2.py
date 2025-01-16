# Function to count uppercase and lowercase letters
def count_case_letters(text):
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    return uppercase_count, lowercase_count

# Test the function
input_text = input("Enter a string: ")
upper, lower = count_case_letters(input_text)

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
