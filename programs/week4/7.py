# Program to read 6 temperatures and display the max, min, and mean
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatures = []


for i in range(6):
    input_temp = input(f"Enter temperature {i+1} in Centigrade: ").strip()
    
   
    if input_temp[-1].upper() == 'C' and input_temp[:-1].replace('.', '', 1).isdigit():
        celsius = float(input_temp[:-1])  
        fahrenheit = celsius_to_fahrenheit(celsius) 
        temperatures.append(fahrenheit)
    else:
        print("Invalid input format. Please enter a number followed by 'C'.")
        break


if len(temperatures) == 6:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    
    print(f"\nMax temperature: {max_temp:.2f}F")
    print(f"Min temperature: {min_temp:.2f}F")
    print(f"Mean temperature: {mean_temp:.2f}F")
