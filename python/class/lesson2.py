class student:
	def __init__(self, name, korean, english, math, science):
		self.name = name
		self.korean = korean
		self.english = english
		self.math = math
		self.science = science
	def sum(self):
		return self.korean + self.english + self.math + self.science
	def average(self):
		return self.sum() / 4
	def print(self):
		print(self.name, self.sum(), self.average(), sep="\t")

class student_list:
    def __init__(self):
        self.students = []
    def add(self, student):
        self.students.append(student)
    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
	        student.print()

# main 코드
students = student_list()
students.add(student("인성", 87, 88, 98, 95))
students.add(student("구름", 92, 98, 97, 98))
students.add(student("별이", 76, 96, 95, 90))
students.print()