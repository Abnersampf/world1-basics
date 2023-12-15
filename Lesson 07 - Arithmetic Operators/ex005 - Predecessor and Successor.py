num = int(input('Enter a number: '))
predecessor = num - 1
successor = num + 1
color_yellow = '\033[33m'
reset_color = '\033[m'
print(f'Analyzing the number {color_yellow}{num}{reset_color}, its', end='')
print(f'predecessor is {color_yellow}{predecessor}{reset_color} and', end='')
print(f'thesuccessor is {color_yellow}{successor}{reset_color}')
