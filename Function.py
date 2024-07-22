# Function.py

# 함수정의
def setValue(newValue): 
    # 지역변수
    x = newValue
    print("지역변수:",x)

# 호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

# 기본값명시

def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자:매개변수명 기술
def connectURI(server, port):
    strURL = "https://"+server+":"+port
    return strURL

#호출
print(connectURI("multi.com","80"))
print(connectURI(port="8080",server="multi.com"))

#이름해석:LGB이름 해석 규칙
#전역변수
x=5
def func(a):
    return a+x
#호출
print(func(1))

def func2(a):
    x=1
    return a+x

#호출
print(func2(1))

def union(*ar):
    #지역변수 리스트 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

# lambda 함수 (익명 함수) -> 입력 : 처리

g = lambda x,y:x*y
print( g(3,4))
print( g(5,6))
print( (lambda x:x*x)(3))
print( globals())

