class Student:
    def __init__(self, math):
        self.math = math
class StudentList:
    def __init__(self):
        self.__list = []
    def append(self, element):
        if type(element) != Student:
            raise TypeError("Student를 전달해주세요.")
        self.__list.append(element)
    def sum(self):
        output = 0
        for element in self.__list:
            output += element.math
        return output
    def average(self):
        return self.sum() / len(self.__list)
    
studentlist = StudentList()
studentlist.append(Student(100))
studentlist.append(Student(20))
print(studentlist.sum())
print(studentlist.average())