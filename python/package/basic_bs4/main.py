from urllib import request
from bs4 import BeautifulSoup

weather_address = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20261001.xml"
data = request.urlopen(weather_address)     # 열기

soup = BeautifulSoup(data, "html.parser")   # 이 데이터를 html.parser로 읽어들임.

# soup.select()       # 특정 이름을 가진 태그를 모두 찾아줍니다.
# soup.select_one()   # 특정 이름을 가진 태그를 하나만 찾아줍니다.

for item in soup.select("local_ta"):
    print(item.select_one("local_ta_name").string)
    print(item.select_one("week1_local_ta_normalYear").string)
    print(item.select_one("week1_local_ta_similarRange").string)
    print(item.select_one("week1_local_ta_minVal").string)
    print(item.select_one("week1_local_ta_similarVal").string)
    print(item.select_one("week1_local_ta_maxVal").string)
    print()