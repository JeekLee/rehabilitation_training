## 터틀 모듈
import turtle
import time

# 그림을 그리기 위해서 캔버스를 불러온다.
t = turtle.Pen()
t.shape("turtle")
t.pencolor("blue")
# 직선으로 100pixel만큼 줄 긋기

i = 0
for i in range (0,4) :
    t.forward(100)
    t.right(90)

## sleep 함수
time.sleep(3)
