from collections import Counter
from itertools import product
import sys
input = sys.stdin.readline

def win_probability(X,Y):
    count_y = Counter(Y)
    sorted_y = sorted(count_y.keys())

    win_count = 0
    total = len(X)*len(Y)
    for x in X:
        smaller_y = sum(count_y[y] for y in sorted_y if y < x)
        tie_y = sum(count_y[y] for y in sorted_y if y == x)
        
        win_count += smaller_y + (tie_y * 0.5)

    return win_count / total

T = int(input().strip())

for _ in range(T):
    dice = list(map(int, input().split()))
    A = dice[:4]
    B = dice[4:]

    #C 만들기
    for C in product(range(1,11), repeat=4) :
        game_AB = win_probability(A,B)
        game_BC = win_probability(B,C) 
        game_CA = win_probability(C,A)

        game_BA = 1 - game_AB
        game_CB = 1 - game_BC
        game_AC = 1 - game_CA
        
        if (game_AB > 0.5 and game_BC > 0.5 and game_CA > 0.5) or \
        (game_BA > 0.5 and game_CB > 0.5 and game_AC > 0.5) :
            print("yes")
            break
    else:
        print("no")