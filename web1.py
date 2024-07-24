# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
# 검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser") # 정해져있는 상수값 html.parser
# 전체 코드 검색
# print(soup.prettify())
# <p> 전체 검색
# print(soup.find_all("p"))
# 첫번째 <p>
# print(soup.find("p"))
# 조건 : <p class='outer-text'>
# print(soup.find_all("p", class_="outer-text")) # 기존 class 키워드와의 출동 방지. class_ <- 언더바 붙임
# id=first
# print(soup.find_all(id="first"))
#내부 문자열 출력 : .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)



