class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__radius = radius
        self.__pi = 3.14
        
    @property
    def radius(self):
        return self.__radius
  
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__radius = value
		
    @property
    def circumference(self):
        return 2 * self.__pi * self.__radius
    
    @property
    def width(self):
        return self.__pi * (self.__radius ** 2)
    


# 위처럼 property를 붙이면 밑의 코드 실행 가능
circle = Circle(10)
circle.radius
circle.radius = 20
print(circle.circumference)
print(circle.width)