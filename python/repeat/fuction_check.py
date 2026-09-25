"""
패밀리 레스토랑에서 여러 개의 테이블에 나누어 앉으려고 합니다.
이때 한 사람만 않는 테이블이 없게 그룹을 지어야 합니다. 
인원 수를 나누는 패턴만 구하면 되며, 누가 어디에 앉는 지 등은 고려하지 않아도 됩니다.
예를 들어 6명이라면 다음과 같은 네 가지 경우를 생각할 수 있습니다.
_________________________________________________
|   2명 + 2명 + 2명    2명 + 4명   3명 + 3명   6명  |
_________________________________________________
한 개의 테으블에 앉을 수 있는 최대 사람의 수는 10개입니다.
100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴을 구하세요.
소스 코드에서 한글 변수명은 여러분들의 이해를 돕기 위한 것이니, 식별자 작성 규칙에 따라 이름을 정해 주세요.
"""

peoples = 1000
memoization = {
    # key: value
    # parameter: return value
}
def graph(n, prev):
    # tuple: imutable data type -> dictionary key can
    if (n, prev) in memoization:
        return memoization[(n, prev)]
    
    return_value = 0
    if n == 0:
        return_value += 1
    else:  # else 없어도 정상 작동
        # 인원을 앉혔으면 절대 그 인원수보다 적게 앉히지 마라!
        # -> 절대 숫자가 줄어들게 앉히미 마라!
        # 무조건 (오름차순)으로 만들어라!
        for i in range(max(2, prev), min(n, 10) + 1):  # 화살표 구현
            return_value += graph(n - i, i)
    memoization[(n, prev)] = return_value
    return return_value
import time

debug_before_time = time.time()
print(graph(peoples, 0))
debug_affter_time = time.time()
print(debug_affter_time - debug_before_time)