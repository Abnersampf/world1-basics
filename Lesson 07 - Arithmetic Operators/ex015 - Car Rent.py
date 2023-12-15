#R$60 day and R$0,15 per km driven
color_green = '\033[32m'
reset_color= '\033[m'
days = int(input('How many days rented: '))
distance = int(input('How many kilometers: '))
price = (60 * days) + (0.15 * distance)
print(f'The total to be paid is R${color_green}{price}{reset_color}')