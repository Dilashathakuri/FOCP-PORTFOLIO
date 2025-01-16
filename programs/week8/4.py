import sys

# Ensure that exactly one file name is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python 4.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        # Read the entire file
        content = file.read()

        # Count lines
        line_count = content.count('\n') + 1 if content else 0  # Adding 1 for the last line if not empty

        # Count characters
        char_count = len(content)

    # Print the results
    print(f"Lines: {line_count}")
    print(f"Characters: {char_count}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
