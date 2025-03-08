import sys
import math

input = sys.stdin.readline
T = int(input())

#------------------------------------------using math

for _ in range(T):
    N, M = map(int, input().split())

    cases = math.comb(M,N)

    print(cases)

#------------------------------------------using factorial

# for _ in range(T):
#     N, M = map(int, input().split())

#     up = 1
#     bottom = 1
#     for i in range(1, N+1):
#         up *= M - i + 1
#         bottom *= i

#     print(up // bottom)