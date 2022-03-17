'''
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0, len(key_list)):
    character[key_list[i]] =  value_list[i]

print(character)
'''

'''
limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
    print("{}를 더할 때 {}을 넘으며 그때의 값은 {} 입니다.".format(i-1, limit, sum_value))
'''

'''
max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current
        
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
'''

'''
i = 0
while i < 10:
    print("{}번째 반복입니다".format(i))
    i += 1
'''
#1~100까지 짝수를 더하는 코드

'''
i = 0
result = 0
while i <100:
    i = i + 1
    if i % 2 == 0:
        result = result + i
    print(result)'''


'''
i = 3
j = 1
while i < 6:
    while j < 10:
        print(i , 'x' , j ,'=' , i * j)
        j=j+1
    j=1
    i=i+1
'''

'''
i = 0
while i < 100:
    i = i + 2
    print(i)
    '''

#100 이상의 자연수 중 가장 작은 23의 배수

'''
i = 100
while i % 23 != 0:
    i += 1
print(i)
'''

'''N입력
0 <= N <= 99
M = (N의 십의자리수 + N의 일의자리수)

if N == M 이 될때 까지 몇번 도는지 count
만약 N == M 이 아니라면 N의 일의 자리수 + 값의 일의 자리수
(한자릿수 N은 십의자릿수에 0)
print(count)


'''
'''
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고,각 자리의 숫자를 더한다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다.
4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
'''


'''
n = int(input("0~99 사이의 수 입력 : "))
count = 1
a = n

if a > 10:
    a = ((a // 10) + (a % 10)) + ((a % 10)* 10)
else:
    a = a * 10 + a
while True:
    if a == n:
        break
    elif a >= 10:
        a = ((a//10) + (a%10)) % 10 + ((a%10)*10)
    else:
        a = a * 10 + a
    count += 1
print(count)
'''

