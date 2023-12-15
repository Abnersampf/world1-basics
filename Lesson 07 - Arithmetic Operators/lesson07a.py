print(f"5 % 2 == {5 % 2}") # output: 1
"""
-5 |_2_
_4_| 2
 1 |
"""
print(f"5 // 2 == {5 // 2}") # output: 2
"""
 5 |_2_
 4 | 2
   |
"""
print(f"5 / 2 == {5 / 2}") # output: 2.5
"""
-5  |_2_
_4__| 2.5
-10 |
_10_|
  0
"""
print(f"5 ** 2 == {5 ** 2}") # output: 25
"""
order of precedence:
1st - () (parenthesis)
2nd - ** (power)
3rd - * (multiplication), / (division), // (integer division), % (rest of division)
4th - + (adition), (subtraction)
"""
degree_celsius = float(input('Enter the temperature (°C): '))
degree_fahrenheit = degree_celsius * 9 / 5 + 32
print(f"{degree_celsius}°C is {degree_fahrenheit}°F")
# you can use 'base ** exponent' or 'pow(base, exponent)'
print(f"4 + pow(9, 2) * 5 == {4 + pow(9, 2) * 5}") # output: 409
print(f"4 + 9 ** 2 * 5 == {4 + 9 ** 2 * 5 }") # output: 409
