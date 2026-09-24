# 팩토리얼 구현하기
n = int(input("정수 입력하셈"))
total = 1
def factorial(n):
    total *= n
    if n == 1:
        return total
    n -= 1
    return factorial(n)
print(factorial(n))