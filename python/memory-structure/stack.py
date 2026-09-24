# 할당: 어떠한 변수에다가 값을 집어 넣는 과정
a = 1
b = True
c = "안녕하세요"

# 참조(접근): 어떠한 변수에 있는 값을 꺼내오는 과정
print(a)
print(b)
print(c)

# 할당
a = 10
b = [1, 2, 3, 4]

def function():
    # 함수는 실행되기 전에
    # 내부에서 생성되는 모든 변수에 대한 정보를 미리 파악
    # "a, b는 함수 스택 내부에 있을 것이다!"
    # -> 미리 다 읽어서 함수 내부에 있는 a, b를 내부변수로 이미 인식한다.
    print(a)
    print(b)
    a = 20
    b = [5, 6, 7, 8]
function()

print(a)
print(b)


a = 10
b = [1, 2, 3, 4]

def function():
    # 
    a = 20
    b.extend([5, 6, 7, 8])
    print(a)
    print(b)
function()

print(a)
print(b)