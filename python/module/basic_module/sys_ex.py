import sys

# sys의 가장 중요한 역할은 명령 매개변수를 받는 기능이다.
print(sys.argv)  # 명령 매개변수라는 값을 뽑아낼 수 있다.
# python3 module/sys_ex.py 라고 실행하면
# ['module/sys_ex.py'] -> 파이썬 명령어 뒤에 입력한 코드

# python3 module/sys_ex.py 라고 실행하면
# ['module/sys_ex.py'] -> 파이썬 명령어 뒤에 입력한 코드

# python3 module/sys_ex.py 10 20 30
# ['module/sys_ex.py', '10', '20', '30']

# 이 명령 매개변수는 정말로 많이 활용된다.
# 예를 들어서 여러분이 이후에 어떤 사이트의 이미지를 모두 긁어오는 프로그램을 만들었다고 치면
# 그러면 이 내부에 url이라는 주소가 적혀 있을 텐데
# 이 주소에다가 직접 값을 입력해서 실행을 하기에는 파일을 매번 열어야 한다. 그래서 굉장히 귀찮을 거다.
url = "http://google.com"
# 하지만 만약에 이 url에다가 
url = sys.argv[1]
# 라고 작성하면
# 터미널 -> python3 module/sys_ex.py http://google.com
# 입력하는 거 만으로 해당 사이트의 데이터를 긁어오는 등
# 코드의 어떠한 데이터를 전달할 수 있게 된다.
# 그래서 굉장히 다양하게 활용되는 내용이기 때문에 지금 꼭 기억해라.