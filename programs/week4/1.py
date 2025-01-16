# Function to validate if the number is in the range 0 to 100
def is_in_range(number):
    return 0 <= number <= 100


test_number = int(input("Enter a number: "))
if is_in_range(test_number):
    print("The number is in the range 0 to 100.")
else:
    print("The number is outside the range.")
