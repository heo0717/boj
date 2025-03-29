import sys
input = sys.stdin.readline

def not_more_than_x(X):
    count = 0
    for i in range(1, n + 1):
        count += min(n, X // i)
    return count

n = int(input().strip())
k = int(input().strip())

low = 1
high = k
ans = 0

while low <= high :
    mid = ( low + high ) // 2
    if not_more_than_x(mid) >= k :
        ans = mid
        high = mid - 1

    else :
        low = mid + 1

print(ans)