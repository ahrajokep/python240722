# DemoLoop.py

Value = 5
while Value >0:
    print(Value)
    Value -= 1


lst = ["apple",100,3.14]

for item in lst :
    print(item)

print("--range()함수---")
print(list(range(1,11)))
print(list(range(2000,2025)))
print(list(range(1,32)))

print("---리스트 내장---")
lst = list(range(1,11))
print( [i**2 for i in lst if i>5])
tp = ("apple","orange")
print([len(i) for i in tp])
