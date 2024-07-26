# DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]


#폼 클래스 정의(다중 상속)
class DemoForm(QDialog, form_class): # 두 클래스 QDialog, form_class를 상속 받음
    #초기화 메서드
    def __init__(self):
        super().__init__() # QDialog의 초기화 메서드, form_class의 초기화 메서드 모두 수행
        self.setupUi(self) # 원래 준비되어 있는 초기화 메서드 setupUi 준비
        self.label.setText("첫번째 데모")

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