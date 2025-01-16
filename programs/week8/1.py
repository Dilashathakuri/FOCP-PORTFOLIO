import sys

def nl_command(file_name):
    try:
        
        with open(file_name, 'r') as file:
            
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:>6}\t{line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <file_name>")
    else:
       
        file_name = sys.argv[1]
        nl_command(file_name)
