'''
HTML 소스를 해석하는 것을 파싱(parsing) 이라고 함
'''

# Beautiful Soup 실습
from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <div id = "content">
            <ul class = "industry">
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>스마트팩토리</li>
            </ul>
            <ul class = "language">
                <li>파이썬</li>
                <li>C++</li>
                <li>Javascript</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
print(soup)

# lxml => 속도가 빠름. pip install lxml 설치 필요
# htmlSlib => 속도가 느림. pip install htmlSlib. html 규격을 엄격히 지킴


# find 함수
first_ul = soup.find("ul")
print(first_ul)
print(first_ul.text) # 태그 없이 text 만 출력

all_ul = soup.find_all("ul") # all은 list 형태로 반환
print(all_ul[1].text)

class_ul = soup.find("ul", attrs = {"class":"language"})
print(class_ul)

# select 함수 모든 요소 찾기 / select_one 최초 원소 찾기# Beautiful Soup 실습
from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <div id = "content">
            <ul class = "industry">
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>스마트팩토리</li>
            </ul>
            <ul class = "language">
                <li>파이썬</li>
                <li>C++</li>
                <li>Javascript</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
print(soup)

# lxml => 속도가 빠름. pip install lxml 설치 필요
# htmlSlib => 속도가 느림. pip install htmlSlib. html 규격을 엄격히 지킴


# find 함수
first_ul = soup.find("ul")
print(first_ul)
print(first_ul.text) # 태그 없이 text 만 출력

all_ul = soup.find_all("ul") # all은 list 형태로 반환
print(all_ul[1].text)

class_ul = soup.find("ul", attrs = {"class":"language"})
print(class_ul)

# select 함수 모든 요소 찾기 / select_one 최초 원소 찾기
# ul.industry
#  #content > .industry
# .industry
# content:first-child
first_ul = soup.select_one(".industry")
all_ul = soup.select_one("div#content")
print(all_ul)

# 실습1

# 실습1. 국립중앙박물관 관람 정보

import requests
from bs4 import BeautifulSoup

url = " https://www.museum.go.kr/site/main/home"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

time = soup.select('div > ul > li.info > div')
cost = soup.select('div.info-admission > ul > li')

for i in time:
    print(i.text.strip())

print(cost.text)