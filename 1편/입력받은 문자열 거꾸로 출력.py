state = input("문자열 입력 : ")

# 문자열의 양측 공백 제거
# lstrip : 좌측 공백 제거, rstip : 우측 공백 제거
state = state.strip()

# for문 활용
s_reverse1 = ""
for ch in state:
    s_reverse1 = ch + s_reverse1

print("역순으로 출력 : " + s_reverse1)

# [::-1]을 통해 역순으로 바꿔줄 수 있음
s_reverse2 = state[::-1]
print("역순으로 출력 : " + s_reverse2)
