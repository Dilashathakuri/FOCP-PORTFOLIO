# Function to return letters that appear in at least one of the two words
def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower())) 


def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))  


def letters_in_either_not_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))  

word1 = "Dilasha"
word2 = "Thakuri"

print("Letters in either word:", letters_in_either(word1, word2))  
print("Letters in both words:", letters_in_both(word1, word2))    
print("Letters in either, but not both:", letters_in_either_not_both(word1, word2))
