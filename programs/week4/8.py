# Program to read temperatures and display the max, min, and mean
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatures = []


while True:
    input_temp = input("Enter temperature in Centigrade (e.g., 25C) or press Enter to stop: ").strip()
    
   
    if input_temp == "":
        break
 
    if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
        celsius = float(input_temp[:-1])  # Convert the numeric part to a float
        fahrenheit = celsius_to_fahrenheit(celsius)  # Convert to Fahrenheit
        temperatures.append(fahrenheit)
    else:
        print("Invalid input format. Please enter a number followed by 'C'.")


if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    
    print(f"\nMax temperature: {max_temp:.2f}F")
    print(f"Min temperature: {min_temp:.2f}F")
    print(f"Mean temperature: {mean_temp:.2f}F")
else:
    print("No valid temperatures entered.")
