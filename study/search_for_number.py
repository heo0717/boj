import sys

input = sys.stdin.readline

N = int(input().strip())
N_nums = set(map(int, input().split()))
M = int(input().strip())
M_nums = list(map(int, input().split()))

for i in M_nums:
    print('1' if i in N_nums else '0')