import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    a,b,c = map(int, input().split())

    A = a ** 2
    B = b ** 2
    C = c ** 2

    if A + B == C or A + C == B or B + C == A :
        print(f'Scenario #{i}:')
        print('yes')
    else :
        print(f'Scenario #{i}:')
        print('no')        

    print()