# 모듈의 기본적인 활용 방법
# (1) "내가 무엇을 해야겠다"라고 인지
# -> ex) "시간을 구해야 하는 경우"
# (2) 구글에서 "무엇을 하려면 어떻게 해야하나요?" 찾은 뒤
# -> ex) '파이썬 시간 구하기'
# (3) 그 코드를 복사해서 사용
from datetime import datetime

now = datetime.now()

print("현재 : ", now)
print("현재 날짜 : ", now.date())
print("현재 시간 : ", now.time())
print("timestamp : ", now.timestamp())
print("년 : ", now.year)
print("월 : ", now.month)
print("일 : ", now.day)
print("시 : ", now.hour)
print("분 : ", now.minute)
print("초 : ", now.second)
print("마이크로초 : ", now.microsecond)
print("요일 : ", now.weekday())
print("문자열 변환 : ", now.strftime('%Y-%m-%d %H:%M:%S'))
# (4) 자주 사용되는 함수가 있다면 이는 외워서 활용