# DemoStrList.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
x = 100
y = 3.14

print(len(strA))
print(len(strB))
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[-3:])

#리스트 형식
colors = ["red","blue","green"]
print(colors)
print(type(colors))
colors.append("yellow")
print(colors)
colors.insert(2, "pink")
print(colors)
colors.remove("blue")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

# 형식 변환
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)

# 튜플
tp =(10,20,30)
print(type(tp))
print(len(tp))

# 함수 정의
def calc(a,b):
    return a+b, a*b
# 호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim","김유신"))

# 딕셔너리
device = {"아이폰":5, "아이패드":10}
print(type(device))
#입력
device["맥북"]=15
print(device)
#수정
device["아이폰"]=6
print(device)
#삭제
del device["아이패드"]
print(device)
#검색
print(device["맥북"])

for item in device.items():
    print(item)


True and True and True
True and True and True
print()
