# iterable: 반복할 수 있는 것(반복문 뒤에 넣을 수 있는 것) = Iterate + able
# ex) list, tuple, dictionary

# iterator: 반복하는 녀석(이터러블을 만드는 방법 중 하나)

# generator: 이터레이터를 만드는 방법 중 하나

# 만드는 방식은 3가지
# ---제너레이터(: 이터레이터를 만드는 방법 중 하나) 표현식---
# 리스트 내포: [컴플리헨션]
# example = ", ".join([str(num) for num in range(1, 11) if num % 2 == 0]): 리스트 내포
example = (num for num in range(1, 11) if num % 2 == 0)
print(example)

# iterator
# next(이터레이터): 내부의 요소를 꺼낼 수 있음
print(next(example))
print(next(example))
print(next(example))

for item in example:
    print(item)

# 제너레이터 함수 -> 얘도 이터레이터를 만드는 방법 중 하나, 그 형태가 함수의 형태
# 1) 호출했을 때 내부의 코드가 즉시 실행되지 않고
# 2) 제너레이터를 리턴합니다.
# 제너레이터는 이터레이터를 만드는 방법 중 하나이고, next 메서드를 통해 element를 꺼낼 수 있다.
def gen_func():
    for number in range(1, 11):
        yield number ** 2  # yield가 포인트 -> 이 키워드를 써야 제너레이터 함수라고 인식 된다.

generator = gen_func()
print(generator)

# next(제너레이터) -> yield 부분까지 호출을 하고, 뒤의 값을 리턴한 뒤 대기하게 된다.
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("이녀석은 제너레이터이고, 제너레이터는 이터레이터이고, 이터레이터는 이터러블이기 때문에\n반복문 뒤에 넣어서 반복문 넣기 가능")
for num in generator:
    print(num)
# 이터레이터 클래스 -> 나중에 한다네요


# 활용도
# 컴플리헨션
# 기존의 있는 데이터를 기반으로 새로운 리스트를 만든다.
# 기존의 요소가 100개 있는 범위를 기반으로 컴프리헨션을 사용해 리스트를 만들면
# 요소가 100개 있는 리스트를 또 한번 다시 만들어 내기 때문에
# -> 메모리 사용량이 많음

# 제너레이터 표현식 or 제너레이터 함수
# 데이터를 하나 더 만들어 내는 것이 아니라,
# 기존의 데이터를 기반으로
# 기존의 데이터의 next 메서드를 한번씩 돌릴 때 마다
# item을 하나 꺼내서 새로운 item 요소로 뭔가를 할 뿐이다.
# -> 메모리 사용량이 적음
# next라는 함수가 돌 때 연산이 하나씩 일어남
# -> 과부하 분산