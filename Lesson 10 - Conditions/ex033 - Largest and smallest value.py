number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

# 7, 2, 4
# 7, 4, 2

# 2, 7, 4
# 4, 7, 2

# 2, 4, 7
# 4, 2, 7

highest_number = number1
lowest_number = number1

if number2 > highest_number:
    highest_number = number2
if number3 > highest_number:
    highest_number = number3
print(f"The highest value entered was {highest_number}")

if number2 < lowest_number:
    lowest_number = number2
if number3 < lowest_number:
    lowest_number = number3
print(f"The lowest value entered was {lowest_number}")
