class Shape:
    def __init__(self):
        raise "생성자를 구현해주세요."
    def width(self):
        raise "넓이 함수를 구현해주세요. 넓이를 리턴하는 함수를 작성해주세요."
    def output_assistant(self):
        raise "출력 보조 함수를 구현해주세요. 출력 전 한마디를 입력해주세요."
    def print(self):
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
        self.output_assistant()
        print(f"넓이: {self.width()}")
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)


class Circle(Shape):
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius
    def output_assistant(self):
        print(f"원의 반지름은 {self.radius}")
    def width(self):
        return self.radius ** 2 * self.pi

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def output_assistant(self):
        print(f"정사각형의 한 변의 길이는 {self.length}")
    def width(self):
        return self.length ** 2

square = Square(10)
square.print()