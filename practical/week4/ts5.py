
def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        max = a
    else:
        max = b
    return max


result1 = findMax(10, 20)
print("The maximum of 10 and 20 is:", result1)

result2 = findMax(100, 50)
print("The maximum of 100 and 50 is:", result2)

result3 = findMax(-5, -10)
print("The maximum of -5 and -10 is:", result3)

result4 = findMax(0, 0)
print("The maximum of 0 and 0 is:", result4)

result5 = findMax(7.5, 7.6)
print("The maximum of 7.5 and 7.6 is:", result5)
