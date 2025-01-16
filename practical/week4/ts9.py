
def calcAve(*numbers):
   
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers) if len(numbers) > 0 else 0
