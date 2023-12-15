from random import randint
from time import sleep

color_blue = '\033[34m'
color_cyan = '\033[36m'
color_red = '\033[31m'
color_yellow = '\033[33m'
reset_color = '\033[m'

number = randint(0, 5)
print(f"""{color_cyan}CPU:{color_blue}
- I'll think of a number from 0 to 5. Try to gess it...
- What number did i think of?{reset_color}
""")

sleep(0.5)

print(color_yellow + "YOU:" + color_red)
attempt = int(input("- "))

print(reset_color + "\nPROCESSING...\n")
sleep(2)

print(color_cyan + "CPU:" + color_blue)
if attempt == number:
    print("- CONGRATULATIONS! You beat me!")
else:
    print(f"- YOU MISSED IT! I thought of number {number} and not {attempt}!")
print(reset_color, end='')
