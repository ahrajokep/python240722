# DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests                     # web2.py 선언부 추가
from bs4 import BeautifulSoup       # web2.py 선언부 추가

# 디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]


#폼 클래스 정의(다중 상속) 
class DemoForm(QMainWindow, form_class): # 두 클래스 QMainWindow, form_class를 상속 받음
    #초기화 메서드
    def __init__(self):
        super().__init__() # QDialog의 초기화 메서드, form_class의 초기화 메서드 모두 수행
        self.setupUi(self) # 원래 준비되어 있는 초기화 메서드 setupUi 준비
        # self.label.setText("첫번째 데모")
    # 슬롯메서드 추가
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"

        response = requests.get(url)

        # 파일에 저장
        # f = open("daangn.txt", "wt", encoding="utf-8")
        f = open("daangn_pyqt.txt", "a+", encoding="utf-8") # a+ : append 

        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            addrElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            addr = addrElem.text.strip()
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")

        f.close()

        self.label.setText("당근 크롤링 실행함")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

#해당 모듈을 직접 실행했는지 여부를 체크
#Java, C언어 main()함수가 진입점(Entry point)
if __name__ == "__main__": # 환경변수가 __main__ 이면, 직접 모듈을 실행한거
    # 실행프로세스 생성
    app = QApplication(sys.argv) # 상수값 sys.argv
    # 인스턴스 생성
    demoForm = DemoForm()
    # 화면 보여주기
    demoForm.show()
    # 이벤트 처리 대기
    app.exec_()