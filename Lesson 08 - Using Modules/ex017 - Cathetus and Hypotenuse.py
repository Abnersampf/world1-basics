"""from math import sqrt

opposite_side = float(input("Length of the opposite side: "))
adjacent_side = float(input("Length of the adjacent side: "))
# hypotenuse² = opposite_side² + adjacent_side²
hypotenuse = sqrt(pow(opposite_side, 2) + pow(adjacent_side, 2))
print(f"The hypotenuse will be {hypotenuse:.2f}")"""

from math import hypot

opposite_side = float(input("Length of the opposite side: "))
adjacent_side = float(input("Length of the adjacent side: "))
hypotenuse = hypot(opposite_side, adjacent_side)
print(f"The hypotenuse will be {hypotenuse}")