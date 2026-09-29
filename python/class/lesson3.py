class Student:

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

    def __str__(self):
        return f"{self.name}\t{self.sum()}\t{self.average()}"

    def __eq__(self, diff_value):
        print("__eq__() 함수 호출")
        return self.sum() == diff_value.sum()

    def __ne__(self, diff_value):
        return self.sum() != diff_value.sum()

    def __gt__(self, diff_value):
        # type() == ... 대신 isinstance() 사용이 더 권장됩니다.
        if isinstance(diff_value, Student):
            return self.sum() > diff_value.sum()
        elif isinstance(diff_value, int):
            return self.sum() > diff_value
        else:
            raise TypeError("같은 자료형(Student)이나 정수(int)를 입력해주세요!")

    def __ge__(self, diff_value):
        return self.sum() >= diff_value.sum()

    def __lt__(self, diff_value):
        return self.sum() < diff_value.sum()

    def __le__(self, diff_value):
        return self.sum() <= diff_value.sum()


class StudentList:

    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
            student.print()

    def __str__(self):
        output = "이름\t총점\t평균\n"
        for student in self.students:
            output += f"{str(student)}\n"
        return output.strip()

    def clone(self):
        output = StudentList()
        for student in self.students:  # self.students로 수정됨
            output.add(student)
        return output

    def __add__(self, diff_value):
        output = self.clone()
        output.add(diff_value)
        return output


# main 코드
students = StudentList()
students += Student("인성", 87, 88, 98, 95)
students += Student("구름", 92, 98, 97, 98)
students.add(Student("별이", 76, 96, 95, 90))

print(students)