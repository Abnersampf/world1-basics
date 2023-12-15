salary = float(input("What is the employee's slaray? R$"))

if salary > 1250:
    new_salary = salary * 1.10
else:
    new_salary = salary * 1.15

print(f"Those who used to earn R${salary} now earn R${new_salary}.")
