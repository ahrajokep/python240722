# 전역변수
strName = "Not Class Member"

class DemoString:
    # 인스턴스 멤버 변수 (우연히 이름 충돌)
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # print(strName) # 실수로 self를 안붙였음
        print(self.strName)

# 인스턴스 생성
d = DemoString()
d.set("First Message")
d.print()
