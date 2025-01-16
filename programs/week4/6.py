# Program to convert Centigrade to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


input_temp = input("Enter temperature in Centigrade: ").strip()


if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
    celsius = float(input_temp[:-1])  
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{fahrenheit:.2f}F") 
else:
    print("Invalid input format. Please enter a number followed by 'C'.")
