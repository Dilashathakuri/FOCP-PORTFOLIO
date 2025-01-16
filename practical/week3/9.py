names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]

# Checking if "Eric" is in the list
print("Eric" in names)  # True because "Eric" is in the list

# Checking if "Mark" is in the list
print("Mark" in names)  # False because "Mark" is not in the list


names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]

# Checking if "Mark" is NOT in the list
print("Mark" not in names)  # True because "Mark" is not in the list

# Checking if "Terry" is NOT in the list
print("Terry" not in names)  # False because "Terry" is in the list



message = "Hello there, my name is John"

# Checking if "nam" is in the message (substring check)
print("nam" in message)  # True because "nam" is a substring of "name" in the string

# Checking if "hello" is in the message (case-sensitive check)
print("hello" in message)  # False because "hello" is not found (case mismatch)
