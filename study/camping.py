c = 0

while True :
    
    L, P, V = map(int,input().split())
    
    if L == P == V == 0 :
        break

    else :

        c += 1
        day = ( V // P ) * L 

        day += min(V % P , L)

        print(f"Case {c}: {day}")