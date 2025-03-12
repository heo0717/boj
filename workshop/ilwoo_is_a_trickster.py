#shell game
N, X, K = map(int, input().split()) #X: first position

for i in range(K):
    a, b = map(int, input().split())

    if X == a: X = b
    elif X == b : X = a

print(X)