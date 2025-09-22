T = int(input())

t = 0
while True :
    if t == T : break

    Y = 0
    K = 0
    for _ in range(9):
        y, k = map(int, input().split())

        Y += y
        K += k

    if Y > K : print('Yonsei')
    elif Y < K : print('Korea')
    elif Y == K : print('Draw')
    
    t += 1