import sys
input = sys.stdin.readline

x1, y1, r1 = list(map(int, input().split()))
x2, y2, r2 = list(map(int, input().split()))

# r1 + r2 < d
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) 

if d < (r1 + r2)**2  :
    print('YES')

else :
    print('NO')