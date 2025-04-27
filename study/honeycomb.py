import sys
input = sys.stdin.readline

N = int(input().strip())

n = 1 #layer
while True:

    total = 3 * n * ( n - 1 ) + 1

    if total >= N :
        print(n)
        break

    n += 1