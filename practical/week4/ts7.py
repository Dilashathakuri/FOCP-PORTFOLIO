
def someFunc(x, y, z):
    
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"z is {z}")

print("Call 1:")
someFunc(y=2, z=3, x=1)

print("\nCall 2:")
someFunc(z=3, x=1, y=2)

print("\nCall 3:")
someFunc(x=1, y=2, z=3)

print("\nCall 4:")
someFunc(z=3, y=2, x=1)
