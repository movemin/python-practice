count = 0  # 이동 횟수 = (2 ** n) - 1
def hanoi(n, start, target, assistance):
    global count
    if n == 1:
        print(start , "->", target)
        count += 1
    else:
        hanoi(n - 1, start, assistance, target)
        print(start , "->", target)
        count += 1
        hanoi(n - 1, assistance, target, start)
n = int(input("원판의 개수를 입력하세요: "))
hanoi(n, "A", "B", "C")

# 원판 카운트 수학 알고리즘
# 원판 1개: 1  = 2  - 1
# 원판 2개: 3  = 4  - 1
# 원판 3개: 7  = 8  - 1
# 원판 4개: 15 = 16 - 1
# 원판 5개: 31 = 32 - 1