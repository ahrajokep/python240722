# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    # 문자열로 결과를 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, 
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1) # print 메서드 없어서 __str__ 찾아서 실행
account1.balance = 15000000 # 이렇게 아무나 잔고에 접근가능 한게 사고 !! -> 그래서 __balance 이렇게 다 변경
# 그랬더니 접근 안됨
# print(account1.__balance)