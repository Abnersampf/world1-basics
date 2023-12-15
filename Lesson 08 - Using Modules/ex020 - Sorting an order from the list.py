from random import shuffle

student1 = input("First student: ")
student2 = input("Second student: ")
student3 = input("Thrid student: ")
student4 = input("Fourth student: ")

students_list = [student1, student2, student3, student4]

shuffle(students_list)

print(f"The presentation order will be\n{students_list}")
