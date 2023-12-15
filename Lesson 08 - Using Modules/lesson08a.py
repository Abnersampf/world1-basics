from math import sqrt, factorial, ceil, floor, trunc

number = int(input("Enter a number to see some informations: "))

print(f"Square root of {number}: {sqrt(number):.2f}")
print(f"Factorial of {number}: {factorial(number)}")
print(f"Ceiling the number {number}: {ceil(number)}")
print(f"Rounding to the floor the number {number}: {floor(number)}")
print(f"Truncating the number {number}: {trunc(number)}")
