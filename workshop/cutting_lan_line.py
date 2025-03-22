import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = [] #cm
for _ in range(k):
    L = int(input().strip())
    lan.append(L)

low, high = 1, max(lan)
ans = 0

while low <= high :
    h = (low + high) // 2 #h = mid
    total = sum( l // h for l in lan )

    if total >= n :
        ans = h
        low = h + 1
    else :
        high = h - 1

print(ans)