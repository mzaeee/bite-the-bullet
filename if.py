'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
하지만, 2000년은 400의 배수이기 때문에 윤년

Year = int(input("연도 입력: "))

if Year % 400 == 0:
    print(1)
elif Year % 4 == 0 and Year % 100 != 0:
    print(1)
else:
    print(0)


X = int(input("정수 X : "))
Y = int(input("정수 Y : "))

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X < 0 and Y < 0:
    print(3)
elif X > 0 and Y < 0:
    print(4)


H = int(input("시 : "))
M = int(input("분 : "))

if H > 0 and (M - 45) < 0:
    print(H - 1, (M + 60) - 45)
elif (M - 45) >= 0:
    print(H, M - 45)
elif H == 0 and (M - 45) < 0:
    print(H + 23, (M + 60) - 45)


A, B = map(int,input("현재시각 :").split())
C = int(input("요리시간 : "))
D = (C + B) // 60 

if 
'''