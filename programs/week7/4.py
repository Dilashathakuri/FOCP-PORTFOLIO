from collections import Counter

# Function to perform frequency analysis and return the 6 most common letters
def frequency_analysis(message):
    
    message = message.lower()
    
    
    letter_counts = Counter(char for char in message if char.isalpha())  
    
   
    most_common = letter_counts.most_common(6)
    
    
    print("The 6 most common letters are:")
    for letter, count in most_common:
        print(f"'{letter}': {count}")


message = "This is a simple example to analyze frequency analysis of letters."
frequency_analysis(message)
