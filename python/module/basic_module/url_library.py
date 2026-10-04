from urllib import request

# 매개변수에 입력된 주소에 있는 데이터를 긁어올 수 있다.
target = request.urlopen("https://google.com")
print(target.read())  # : 내부에 있는 데이터를 읽고 출력할 수 있다.