#두 수 비교하기

A, B = map(int,input("수 입력 :").split())

if A > B:
	print(">")
elif A < B:
	print("<")
elif A == B:
	print("==")