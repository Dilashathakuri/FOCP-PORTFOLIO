# Dictionary to store country-capital pairs
countries_and_capitals = {}


def get_country_input():
    return input("Enter the name of a country (or 'exit' to terminate): ").strip().lower()


while True:
    
    country = get_country_input()
    
   
    if country == 'exit':
        print("Goodbye!")
        break
    
    
    if country in countries_and_capitals:
        print(f"The capital of {country.title()} is {countries_and_capitals[country]}.")
    else:
        
        capital = input(f"Please enter the capital city of {country.title()}: ").strip()
        countries_and_capitals[country] = capital
        print(f"Got it! The capital of {country.title()} is {capital}.")
