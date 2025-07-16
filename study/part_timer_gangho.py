import sys
input = sys.stdin.readline

N = int(input().strip())

T = sorted([ int(input().strip()) for _ in range(N) ], reverse = True)

tip = 0

for i in range(N):

    t = T[i] - i

    print(t)

    if t > 0 : tip += t

print(T)
print(tip)