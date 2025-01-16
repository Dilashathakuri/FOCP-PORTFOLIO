import sys


if len(sys.argv) != 3:
    print("Usage: python 2.py <file1> <file2>")
    sys.exit(1)

file1, file2 = sys.argv[1], sys.argv[2]

try:
    
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    
    if content1 == content2:
        print("The files are the same.")
    else:
        print("The files are different.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
