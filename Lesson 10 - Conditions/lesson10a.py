"""time = int(input("How old is your car? "))
if time <= 3:
    print("New car")
else:
    print("Old car")
print("--End--")"""

time = int(input("How old is your car? "))
print("New car" if time <= 3 else "Old car")
print("--End--")