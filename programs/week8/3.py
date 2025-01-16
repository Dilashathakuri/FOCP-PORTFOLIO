import sys

# Ensure there are exactly two command-line arguments
if len(sys.argv) != 3:
    print("Usage: python 3.py <search_string> <file_name>")
    sys.exit(1)

search_string, file_name = sys.argv[1], sys.argv[2]

try:
    # Open and read the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Iterate through each line and check if the search string is in the line
    for line_number, line in enumerate(lines, 1):
        if search_string in line:
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
