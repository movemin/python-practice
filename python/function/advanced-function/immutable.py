# immutable -> hashable
a = 10
a = 20
b = True
b = False
c = "Hi"
c = "Bye"

# c[1] = "Y" -> because of immutable
# integer, string, boolean, tuple

# mutable -> unhashable
# list, dictionary

# immutable type: dictionary key can (사용자 정의 클래스 인스턴스는 뮤터블하지만 기본적으로 Hashable합니다.)
# 사용자 정의 객체는 기본적으로 내용물이 아닌 객체의 힙 메모리 주소(id())를 기반으로 해시값을 계산하도록 설계되어 있기 때문입니다.

# tuple key
A = {
    (2022, 1, 1): "새해",
    (2022, 12, 9): "생일",
    (2022, 12, 25): "크리스마스"
}

# 요소를 변경할 수 없다!
# 자료: 뮤터블 + 이뮤터블 자료
# 이뮤터블
# 변수에 넣었을 때 자료
# 스택에 있는 값을 변경해야만 값을 변경할 수 있는 자료

# 뮤터블 자료
# 변수에 넣었을 때
# 스택에 있는 값을 변경하지 않아도 + 값을 변경할 수 있는 자료