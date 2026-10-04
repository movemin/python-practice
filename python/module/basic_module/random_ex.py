# 지금부터 설명하는 모든 함수는 
# uniform과 같은 "함수 이름"을 기억하려 하지 마시고
# "특정 범위의 랜덤한 float 값을 구하는 함수가 있다"과 같은
# "기능"을 기억해주세요.
import random

# uniform이라는 함수는 매개변수를 2개 지정하게 되는 데,
# a~b 사이에 있는 랜덤한 float값을 리턴한다.
print(random.uniform(10, 20))

# integer로 반환
print(random.randrange(10, 20))

# 보통 random 모듈에서 위의 두개만 외우는 경우가 많음
a = [1, 2, 3, 4, 5, 6]
a[random.randrange(0, len(a))]  # 훨씬 더 쉬운 방법이 있는 데 복잡하게 만들 필요가 없다.
# -> 바퀴의 재발명: 널리 받아들여지는 확립된 기술과 해결방법을 모르거나 의도적으로 무시하고 같은 것을 다시 처음부터 만드는 일

# 매개변수로 반복 가능한 것(iterable)을 넣어 랜덤하게 한 요소를 반환한다.
print(random.choice([1, 2, 3, 4, 5]))