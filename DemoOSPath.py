# DemoOSPath.py
from os.path import *
from os import *

fileName = "c:\\python310\\python.exe"

if exists(fileName):
    print("파일 있음:{0}", format(getsize(fileName)))
else:
    print("파일 없음")

print(abspath("python.exe"))
print(basename(fileName))

print("운영체제이름:{0}".format(name))
print("환경변수:{0}".format(environ))
# system("notepad.exe")

# 파일 목록 가져오기
import glob
# 약식 표기 : r(raw strin notation)
print(glob.glob(r"c:\work\*.py"))