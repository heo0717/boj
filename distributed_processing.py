import sys
input = sys.stdin.readline

T = int(input())

#computer = 10개
for _ in range(T):
    a, b = map(int, input().split())
    
    a %= 10

    computer = pow(a,b,10)
    if computer == 0 :
        print(10)
    else :
        print(computer)