from urllib import request
from bs4 import BeautifulSoup

news_address = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
data = request.urlopen(weather_service_address)     # 열기

soup = BeautifulSoup(data, "html.parser")   # 이 데이터를 html.parser로 읽어들임.

# soup.select()       # 특정 이름을 가진 태그를 모두 찾아줍니다.
# soup.select_one()   # 특정 이름을 가진 태그를 하나만 찾아줍니다.

for item in soup.select("item"):
    print(item.select_one("pubDate").string)
    print(item.select_one("title").string)
    print()