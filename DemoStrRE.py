# DemoStrRE.py
# 문자열변수
data = "<<<  spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam","spam egg!!!!")
print(result)
strA="python is very powerful"
lst = result.split()
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())

#정규표현식
import re
result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

result = re.search("apple","this is apple")
print(result)
print(result.group())

result = re.search("\d{4}","올해는 2024년입니다.")
print(result)
print(result.group())

print("---이메일----")
import re

def is_valid_email(email):
    # 이메일 주소 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소 리스트
sample_emails = [
    "test.email@gmail.com",     # Valid
    "user@domain.com",          # Valid
    "user.name@domain.co.in",   # Valid
    "user-name@domain.org",     # Valid
    "user_name@domain.net",     # Valid
    "user+name@domain.info",    # Valid
    "user@domain",              # Invalid
    "user@.com",                # Invalid
    "user@domain.c",            # Invalid
    "user@domain,com",          # Invalid
    "user@domain..com"          # Invalid
]

# 각 이메일 주소에 대해 체크 및 결과 출력
for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

