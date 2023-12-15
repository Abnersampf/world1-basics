number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2
color_red = '\033[31m'
reset_color = '\033[m'
print('The sum of', color_red + number1 + reset_color, 'and', color_red +
      number2 + reset_color, 'is', color_red + number1 + number2 + reset_color)
