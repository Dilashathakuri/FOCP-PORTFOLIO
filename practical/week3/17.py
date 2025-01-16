numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0

for num in numbers:
    if num > 100:
        print("Value greater than 100 found, stopping loop.")
        break
    total += num
    print("Running total:", total)
else:
    # This block executes only if the loop didn't break
    print("All numbers processed.")
