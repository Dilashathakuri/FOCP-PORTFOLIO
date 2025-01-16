import sys

def process_temperatures(temps):
    if not temps:
        print("No temperatures provided.")
        return
    
    try:
        numbers = [float(temp) for temp in temps]
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
        print(f"Mean: {sum(numbers) / len(numbers)}")
    except ValueError:
        print("Error: All inputs must be numbers.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_temps.py <temp1> <temp2> ...")
    else:
        process_temperatures(sys.argv[1:])
#python "d:\Dilasha\python\process_temp.py" 25.0 30.5 18.2 21.9
