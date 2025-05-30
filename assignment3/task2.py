import math

number = float(input("Enter a positive number: "))

if number <= 0:
     print("Please enter a number greater then 0.")
else:
    square_root = math.sqrt(number)
    logr = math.log(number)
    sine_value = math.sin(number)

print(f"Square root: {square_root}")
print(f"Logarithm: {logr}")
print(f"Sine (in radians): {sine_value}")

