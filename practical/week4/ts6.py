
def multiplyValues(a, b=None):
    
    if b is None:
        return a * a
    else:
        return a * b


result1 = multiplyValues(5)  
print("Result of multiplyValues(5):", result1)

result2 = multiplyValues(3, 4)  
print("Result of multiplyValues(3, 4):", result2)

result3 = multiplyValues(7)  
print("Result of multiplyValues(7):", result3)

result4 = multiplyValues(2, 10)  
print("Result of multiplyValues(2, 10):", result4)

result5 = multiplyValues(0.5)  
print("Result of multiplyValues(0.5):", result5)
