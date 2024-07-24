# db1.py
import sqlite3

# 연결객체(메모리에 저장)
con = sqlite3.connect(":memory:") # 메모리에 저장해. 라는 거
# 커서객체
cur = con.cursor()
# 테이블 구조 생성(테이블 스키마)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');") 
# 밖에는 쌍", 안에는 단일' 으로 하는게 헷갈리지 않음

# 입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))

# 여러건 입력
datalist = (("전우치","010-123"),("홍길동","010-456"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)
# 검색결과
cur.execute("select * from PhoneBook;")
print("---fetchon()---")
print(cur.fetchone())
# print("---fetchon()---")
# print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall()) # 임시메모리에 남은게 한개여서 처음엔 한 개만 뜸

cur.execute("select * from PhoneBook;") # 이렇게 다시 검색하고 버퍼가 다시 채워지면
print(cur.fetchall()) # 전체 다 뜸


# 주석처리 : ctrl + /
# 검색결과
# cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

