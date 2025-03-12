N, L = map(int, input().split())

H = list(map(int, input().split())) # N = len(H)
h = sorted(H)

for i in range(N):
    if h[i] <= L : L += 1

    else: continue

print(L)