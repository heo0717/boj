T = int(input())

t = 0
while True :
    if t == T : break

    result = list(input().strip())

    score = 0
        
    cnt = 0 # 이전에 나온 'O'를 체크
    for i in result :
        if i == 'O' :
            score += ( 1 + cnt )
            cnt += 1

        else : 
            cnt = 0
        
    print( score )

    t += 1