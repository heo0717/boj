import math
N, W, H = map(int, input().split())

D = math.sqrt(W**2 + H**2)

for _ in range(N):
    match = int(input())

    if match > W and match > H and match > D :
        print('NE')
    else : print('DA')