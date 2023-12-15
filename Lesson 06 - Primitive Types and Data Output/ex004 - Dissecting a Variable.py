n = input('Type anything: ')
color_blue = '\033[34m'
reset = '\033[m'
print(f'The type of \"{n}\" is: {type(n)}')
print(f'{n} is made just of spaces? {color_blue}{n.isspace()}{reset}')
print(f'{n} is a number? {color_blue}{n.isnumeric()}{reset}')
print(f'{n} is alphabetic? {color_blue}{n.isalpha()}{reset}')
print(f'{n} is alphanumeric? {color_blue}{n.isalnum()}{reset}')
print(f'{n} is uppercase? {color_blue}{n.isupper()}{reset}')
print(f'{n} is lowercase? {color_blue}{n.islower()}{reset}')
print(f'{n} is capitalized? {color_blue}{n.istitle()}{reset}')
