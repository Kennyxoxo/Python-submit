#Get input from user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplaction = num1 * num2

# Check for division by zero
if num2 != 0:
    division = num1/num2
else:
    division = "Cannot divide by zero"

#Display results
print(f"\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplaction: {num1} * {num2} = {multiplaction}")
print(f"Division: {num1} / {num2} = {division}")