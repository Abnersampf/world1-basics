number = int(input("Enter a number: ").strip())
# 1234
thousand = number // 1000
rest = number % 1000

hundread = rest // 100
rest = rest % 100

dozen = rest // 10
rest = rest % 10

unit = rest // 1

print(f"Analyzing the number {number}")
print(f"Unit: {unit}")
print(f"Dozen: {dozen}")
print(f"Hundread: {hundread}")
print(f"Thousand: {thousand}")