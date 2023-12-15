distance = float(input("How far is your trip? "))
if distance <= 200:
    price = 0.50 * distance
else:
    price = 0.45 * distance
# or
# price = 0.50 * distance if distance <= 200 else 0.45 * distance
print(f"You're about to start a {distance}km trip.")
print(f"The price of your ticket will be R${price:.2f}.")
