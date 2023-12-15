full_name = input("Enter your full name: ").strip()

print("Analyzing your name...")
print(f"Your name in uppercase is {full_name.upper()}")
print(f"Your name in lowercase is {full_name.lower()}")

name_without_spaces = len(full_name) - full_name.count(" ")
# or
name_without_spaces2 = len(full_name.replace(" ", ""))
print(f"Your full name has {name_without_spaces2} letters")

first_name = full_name.split()[0]
# or
first_name2 = full_name[:full_name.find(" ") + 1]
print(f"Your first name is {first_name} and it has {len(first_name)} letters")
# or
# print(f"Your first name is {first_name} and it has {full_name.find(" ")} letters")