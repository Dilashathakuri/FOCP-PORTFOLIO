import sys
import string

# Ensure that exactly one file name is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python 5.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]

# Load the dictionary (you can replace this with a more extensive dictionary file)
# Example of simple words; in a real-world case, you would load a large dictionary.
dictionary = set([
    "hello", "this", "is", "a", "sample", "file", "text", "spell", "checker", "python"
])

# Function to clean and extract words
def extract_words(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    return words

try:
    with open(file_name, 'r') as file:
        content = file.read()

        # Extract words from the content
        words_in_file = extract_words(content)

        # Find words not in the dictionary
        misspelled_words = [word for word in words_in_file if word not in dictionary]

        # Print the misspelled words
        if misspelled_words:
            print("Misspelled words:")
            for word in misspelled_words:
                print(word)
        else:
            print("No misspelled words found.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
