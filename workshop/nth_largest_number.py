import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []

# matrix = [0] * n
for i in range(n):
    line = list(map(int, input().strip().split()))
    # matrix[i] = line
    for l in line :
        if len(h) < n : heapq.heappush(h, l)
        else :
            if l > h[0]: #h[0]은 항상 최솟값
                heapq.heappushpop(h, l)
            
print(h[0])