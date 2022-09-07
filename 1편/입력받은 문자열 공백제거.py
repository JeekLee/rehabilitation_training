state = input("원하는 문자열 입력 : ")
result = ""

for ch in state:
    if ch != " ":
        result += ch

print("임력한 문자열 : " + state)
print("공백을 제거한 문자열 : " + result)
