"""
# 하노이 탑에서 필요한 요소를 모두 매개변수로 받습니다.
하노이탑(원판, "시작기둥"에서 "대상기둥"으로 "보조기둥"을 활용해서):
    if 원판이 1개:
        이동 from 시작기둥 to 대상기둥
    if 원판이 2개 이상:
        # 아래의 원판을 제외하고, 시작기둥에서 보조기둥으로 이동합니다.
        하노이탑(원판 - 1, "시작기둥"에서 "보조기둥"으로 "대상기둥"을 활용해서)
        이동 from 시작기둥 to 대상기둥
        # 아래의 원판을 제외하고, 보조기둥에서 대상기둥으로 이동합니다.
        하노이탑(원판 - 1, "보조기둥"에서 "대상기둥"으로 "시작기둥"을 활용해서)
"""
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