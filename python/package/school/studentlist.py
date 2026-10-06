class StudentList:
    def __init__(self) -> None:
        self._list = []
    def append(self, student):
        self._list.append(student)
    def print(self):
        for student in self._list:
            print(student.sum())