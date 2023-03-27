# use student.py program to execute the class program

from student import student

student1 = student("Madan", "B.tech", 8.6, False)
student2 = student("Kiran", "B.tech", 7.6, True)

print(student1.name)
print(student1.gpa)
print(student1.is_on_probation)

print("")
print(student2.name)
print(student2.gpa)
