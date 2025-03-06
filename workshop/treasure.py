N = int(input().strip())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)

index_B = [(value, index) for index, value in enumerate(B)]
sorted_B = sorted(index_B, key=lambda x : x[0], reverse=True)
sorted_B_index =[ x[1] for x in sorted_B ]

new_A = [0]*N
for i, idx in enumerate(sorted_B_index):
    new_A[idx] = sorted_A[i]

S = 0
for i in range(N):
    S += new_A[i] * B[i]

print(S)
