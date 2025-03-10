import sys
input = sys.stdin.readline

mark_1 = list(map(int, input().split()))
mark_2 = list(map(int, input().split()))

d = ((mark_1[0] - mark_2[0]) ** 2 + (mark_1[1] - mark_2[1]) ** 2) ** 0.5

# r_1 = mark_1[2]
# r_2 = mark_2[2]

# if r_1 + r_2 <= d :
#     print('NO')

# elif d + min(r_1,r_2) <= max(r_1,r_2) :
#     print('NO')

# else :
#     print('YES')

print(d)