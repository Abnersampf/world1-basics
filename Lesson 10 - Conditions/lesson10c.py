grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
average = (grade1 + grade2) / 2
print(f"Your average was: {average:.2f}")
if average >= 7:
    print("Approved!")
else:
    print("Failed!")
# or
# print("Approved!" if average >= 7 else "Failed!")
