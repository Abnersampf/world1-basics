title = " Arithmetic Operators "
print(f"{title:=^40}")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
integer_division = number1 // number2
rest_of_division = number1 % number2
exponentiation = number1 ** number2

print(f"{' Result ':-^40}")

print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division:.2f}")
print(f"{number1} // {number2} = {integer_division}")
print(f"{number1} % {number2} = {rest_of_division}")
print(f"{number1} ** {number2} = {exponentiation}")

print("-" * 40)

print("This is one print", end=" ")
print("And this is another one\nand i'm part of the second print")