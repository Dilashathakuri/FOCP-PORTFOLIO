number = int(input("Enter the number for the times table: "))
if number < 0:
    number = abs(number)
    for i in range(12, -1, -1):
        print(f"{i} x {number} = {i * number}")
elif 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Number must be between 0 and 12 (or negative for reverse table).")
