# 함수는 가독성과 유지보수성을 높여준다.
# 가독성 -> 유지보수성 향상: 빠르게 읽고 이해할 수 있어서
pi = 3.141592

def input_radius():
    number_input_a = float(input("> 숫자 입력: "))
    return number_input_a

def operate_circumference(radius):
    return radius * 2 * pi

def operate_area_of_a_circle(radius):
    return radius ** 2 * pi
    
# 함수를 제외한 부분만을 보면 무슨 말인지 알아먹는다.
radius = input_radius()
print(operate_circumference(radius))
print(operate_area_of_a_circle(radius))

# 질문: 코드를 실행할 때마다 함수를 실행하면 스택을 하나씩 만들기 때문에 코드의 실행이 너무 느려진다.
# 이 말이 뭔 말인가요?
# 현대적인 언어프는 한줄자리코드는 컴파일 단계에서 인라인 코드로 삽입한다.
