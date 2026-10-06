from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 일반적으로 웹 서버는 자기 자신을 "애플리케이션"이라고 부릅니다.
# 그래서 서버 자체를 나타내는 변수를 app이라고 이름 붙입니다.
app = Flask(__name__)
weather_address = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20261001.xml"
data = request.urlopen(weather_address)     # 열기

# 내가 이 사이트의 어느 위치에 들어갔을 때 어떤 함수를 실행하게 하겠다.
@app.route("/")
def hello():
    output = ""
    soup = BeautifulSoup(data, "html.parser")
    for item in soup.select("local_ta"):
        a = item.select_one("local_ta_name").string
        b = item.select_one("week1_local_ta_normalYear").string
        c = item.select_one("week1_local_ta_similarRange").string
        d = item.select_one("week1_local_ta_minVal").string
        e = item.select_one("week1_local_ta_similarVal").string
        f = item.select_one("week1_local_ta_maxVal").string
        output += f"<h1>{a}: {b} {c} {d} {e} {f}\n</h1>" # HTML도 또 다른 프로그래밍 언어이므로 웹 서버 개발로 나아가고자 하신다면 간단하게라도 공부해야 한다.
    
    return output

@app.route("/introduce")
def introduce():
    return "<h1>저를 소개합니다!</h1>"