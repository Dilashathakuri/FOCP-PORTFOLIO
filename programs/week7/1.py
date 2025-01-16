# Function to return sorted list of unique letters in a string
def unique_sorted_letters(input_string):
    
    unique_letters = sorted(set(input_string.lower()))
    
    
    return unique_letters


input_string = "Dilasha"
result = unique_sorted_letters(input_string)
print(result) 
