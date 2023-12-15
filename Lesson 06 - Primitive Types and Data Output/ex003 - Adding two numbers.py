number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
sum = number1 + number2
color_pink = '\033[35m'
reset_color = '\033[m'
print('The sum of', color_pink, number1, reset_color, 'and', color_pink,
      number2, reset_color, 'is', color_pink, number1 + number2, reset_color)
