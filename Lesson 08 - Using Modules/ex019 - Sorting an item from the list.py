from random import choice

student1 = input("First student: ")
student2 = input("Second student: ")
student3 = input("Third student: ")
student4 = input("Fourth student: ")

students_list = [student1, student2, student3, student4]

chosen_student = choice(students_list)

color_blue = '\033[34m'
reset_color = '\033[m'

print(f"The chosen student was {color_blue}{chosen_student}{reset_color}")
