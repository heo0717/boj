import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M = list( int(input()) for _ in range(N) )

money = M[::-1]

cnt = 0
for i in money :
    cnt += K // i
    K %= i

print(cnt)