from itertools import combinations

while True :
    Num = list(map(int, input().split()))
    K = Num[0] #len(S)
    if K == 0: break

    S = Num[1:]

    #choose 6 of S
    for comb in combinations(S,6):
        print(comb)
    #     print(' '.join(map(str, comb)))

    # print( )