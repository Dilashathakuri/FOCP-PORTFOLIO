import sys
import shutil

def backup_file(file_path):
    """
    Creates a backup of the given file.
    :param file_path: Path to the file to be backed up.
    """
    try:
        # Generate backup file name
        backup_path = f"{file_path}.backup"

        # Copy file
        shutil.copy(file_path, backup_path)
        print(f"Backup created successfully: {backup_path}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: Could not create backup. Details: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_file.py <file_path>")
    else:
        backup_file(sys.argv[1])
