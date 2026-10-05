# 실행하고자 하는 파일과 같은 위치에
# 어떠한 파이썬 파일이 있다면 import 해당_모듈의_이름을 입력해서
# 해당_모듈을 가져올 수 있다.
# import hellomodule

# # 이런식으로 읽어들일 수 있다.
# print(hellomodule.a)
# print(hellomodule.b)
# print(hellomodule.C)

# 추가적으로 이전에 언급했던 것처럼 모듈을 활용하면
# "관심사"를 기반으로 변수, 함수, 클래스 등을 모을 수 있습니다.
# 스스로가 만든 변수, 함수, 클래스가 많아졌을 때 활용하면 좋습니다.

# ?: 모듈을 만들어서 뭐함?
# 우리가 지금까지 작성했던 실질적인 프로그램의 실행흐름이 아닌 클래스 설계, 함수 설계 같은
# 부분을 모듈로 분리하면 실제 코드실행흐름을 굉장히 단순하게 만들 수 있다.
# ---Example---
# (1)
# import hellomodule
# hellomodule.Circle()
# (2)
# from hellomodule import Circle
# c = Circle(10)
# print(c.width())
# print(c.circumference())
# (3)
import hellomodule as h
c = h.Circle(10)
print(c.width())
print(c.circumference())

# __name__ 변수
# 현재 이 파일 자신이 main으로써 실행되는지 모듈로써 실행되는지 구분할 때 사용할 수 있는 변수
print("# main.py")
print(__name__)
# 기본적으로 모든 모듈은 __name__을 출력했을 때 자신의 이름을 출력을 하게 되고
# main으로써 실행된 파일은 __main__이라는 문자열을 출력하게 된다.

# if __name__ == "__main__"
# main으로 실행되는 코드는 실행될 필요가 없다.
# 모듈에서 많이 활용된다. (모듈로 가셈)