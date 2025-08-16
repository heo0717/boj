n = list(map(int, input().split()))

N = 0
for i in range(5):
    N += n[i] ** 2

print(N % 10)