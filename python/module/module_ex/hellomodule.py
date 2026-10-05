class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError()
        self.__PI = 3.14
        self.__radius = radius
    def width(self):
        return self.__radius ** 2 * self.__PI
    def circumference(self):
        return self.__radius * 2 * self.__PI


print("# hellomodule.py")
print(__name__)
if __name__ == "__main__":
    print("# width()를 검증합니다.")
    if Circle(10).width() - 314 < 10 ** -7:
        print("width() 검증을 성공했습니다: Success")
    else:
        print("width() 검증을 실패했습니다: Fail")
    print("# circumference()를 검증합니다.")
    if Circle(10).circumference() - 62.8 < 10 ** -7:
        print("circumference() 검증을 성공했습니다: Success")
    else:
        print("circumference() 검증을 실패했습니다: Fail")

# [팁] 부동소수점 오차
# 그런데 여기서 문제가 발생함.
# 우리가 넓이나 둘레를 구할 때 부동소수점 연산을 활용하고 있음.
# 그런데 대부분의 프로그래밍 언어에서 부동소수점 연산은 완벽하게 정확하지 않음.
# 그래서 이전에 실행했던 것처럼 62.800000000000004까지 나오는 모슴을 볼 수 있다.
# 그래서 일반적으로 부동소수점 계산의 정확성을 확인할 때 == 활용하시면 제대로 조건이 잡히지 않을 수도 있다.
# 그래서 알고리즘 문제 등을 풀 때보면
# Circle(10).width() == 314 -> Circle(10).width() - 314 < 10 ** -7
# Circle(10).circumference() == 62.8 -> Circle(10).circumference() - 62.8 < 10 ** -7
# 둘 사아의 오차가 몇 이하가 되게 하라는 코드를 많이 볼 수 있다.

# 이 파일이 메인으로 실행이 되었을 때는 함수가 제대로 구현했는지 확인하게 된다.
# 실행해보셈: python3 hellomodule.py
# -> 이 파일이 메인으로 실행될 때만 조건문이 실행된다.
# 따라서 현재 main.py에 가서 실행하거나 python3 main.py라고 명령어를 입력하면
# 검증 관련 코드는 실행되지 않는다.

# 그래서 이러한 형태로 모듈을 검증하는 코드를 이 내부에 넣으면 넓이 또는 둘레 같은 함수를 변경할 때마다
# main.py를 실행해서 뭔가 잘못된거 없나하고 확인할 필요가 없이
# 해당 모듈(hellomodule.py)을 곧바로 실행해서 수정에 뭔가 문제가 있는지 곧바로 확인할 수 있다.

# 다른 모듈들을 배우게 되면
# test 모듈이라는 모듈을 배우게 되는데,
# 그러면 위에 작성한 검증코드 같은 것들을 조금 더 쉽고 깔끔하게 작성할 수 있게 된다.
# test 모듈 -> 상급자 개발자 여부 구분 요소임. 공부하면 좋음.