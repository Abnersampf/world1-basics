"""city = input("Enter a city name: ").strip().lower()
print(city.startswith("santo"))"""
# or
"""city = input("Enter a city name: ").strip().lower()
print("santo" in city)"""
# or
city = input("Enter a city name: ").strip().lower()
print(city[:5] == "santo")