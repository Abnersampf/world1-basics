from datetime import date

year = int(
    input("Which year do you want analyze? Enter 0 to analyze the current year: "))
# Leap year:
# - It's divisible by 4
# - It's not divisible by 100, but it's divisible by 400

if year == 0:
    year = date.today().year

color_red = '\033[31m'
color_green = '\033[32m'
reset_color = '\033[m'

print(f"The year {year}", end=" ")
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(color_green + "is a leap year" + reset_color)
else:
    print(color_red + "is not a leap year" + reset_color)
