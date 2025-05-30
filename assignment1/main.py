#Get two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
if num2 == 0:
    divi = "Could not divide by zero."
else:
    divi = num1 / num2

#Results
print(f"\nAddition: {num1} + {num2} = {add}")
print(f"Subtraction: {num1} - {num2} = {sub}")
print(f"Multiplaction: {num1} * {num2} = {multiply}")
print(f"Division: {num1} / {num2} = {divi}")
