from functools import reduce

print("********** Calculator Grade - On-line **********")


class CalcGrades:
    def __init__(self, student, subject, grades):
        self.student = student
        self.subject = subject
        self.grades = grades

    def media_grades(self):
        return reduce(lambda x, y: x + y, self.grades) / len(self.grades)


student = input("Inform your name: ")
subject = input("Inform the subject name: ")
num_grade = 0
list_grades = []
while num_grade < 4:
    grades = float(input("Inform all your 4 grades: "))
    list_grades.append(grades)
    num_grade += 1

obj = CalcGrades(student, subject, list_grades)
student_mean_grade = obj.media_grades()

if student_mean_grade < 7:
    print("Aluno", student, ", voce foi REPROVADO. Sua media em", subject,
          "foi", student_mean_grade)
else:
    print("PARABENS!!")
    print("Aluno", student, ", voce foi APROVADO. Sua media em", subject,
          "foi", student_mean_grade)
