import sys

input = sys.stdin.readline
N = int(input().strip())
x = 10

while N > x :
    if (N%x >= x//2):
        N = N+x

    N = N - (N%x)
    x *= 10

print(N)
