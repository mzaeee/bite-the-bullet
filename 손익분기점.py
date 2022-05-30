def BreakEven_point():

    A, B, C = map(int,input("고정비용, 가변비용, 노트북가격 >").split())

#A = 고정비용, B = 가변비용, C= 판매가격
#A=1,000, B=70일때 노트북 한 대 생산비용 1,070만원, 열 대 생산 비용 1,700만원
#노트북 판매비용 > (고정비용 + 가변비용)이 될때까지
#Ci > A + Bi
#(A / (B - C)) + 1


    if B<C:
        x=int(A/(C-B))
        print(x+1)
    else:
        print(-1)

    

BreakEven_point()