# class Parents:
#     def func(self):
#         print("부모의 함수입니다.")

# class Child(Parents):
#     def func(self):
#         super().func()
#         print("자식의 함수입니다.")
#         super().func()

# child = Child()
# Child.func(child)


# --오버라이트 / super()
class Button:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")

class RedButton(Button):
    def __init__(self):
        super().__init__()
        print("버튼을 빨간색으로 칠합니다.")

class BlueButton(Button):
    def __init__(self):
        super().__init__()
        print("버튼을 파란색으로 칠합니다.")

class GreenButton(Button):
    def __init__(self):
        super().__init__()
        print("버튼을 초록색으로 칠합니다.")

RedButton()
BlueButton()
GreenButton()