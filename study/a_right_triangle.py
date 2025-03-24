from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input().strip())

coords = [tuple(map(int, input().split())) for _ in range(n)]

# if ab * ac = 0 : a right triangle

ans = 0

for i in range(n):
    squares = set()

    for j in range(n):
        if i == j : continue

        dx, dy = coords[j][0] - coords[i][0], coords[j][1] - coords[i][1]
        square_d = dx * dx + dy * dy #(c^2 = a^2 + b^2)
        
        # d2 = dx ** 2 + dy ** 2  # 거리의 제곱 (느림 / ** 연산자가 반복곱셈수행)

        for d in squares :
            if (square_d - d) in squares :
                ans += 1

        squares.add(square_d)

print(ans)

# ---------------------------------------time over 2

# ans = 0
# for p1, p2, p3 in combinations(coords, 3):

#     x1, y1 = p1
#     x2, y2 = p2
#     x3, y3 = p3

#     if ((x2 - x1) * (x3 -x1) + (y2 - y1) * (y3 - y1) == 0 or 
#         (x1 - x2) * (x3 -x2) + (y1 - y2) * (y3 - y2) == 0 or
#         (x2 - x3) * (x1 -x3) + (y2 - y3) * (y1 - y3) == 0 ) :
#         ans += 1 

# print(ans)

# ---------------------------------------time over 2

# coords = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     coords.append((x, y))

# ans = 0
# for p1, p2, p3 in combinations(coords, 3):

#     a = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
#     b = ((p2[0] - p3[0]) ** 2) + ((p2[1] - p3[1]) ** 2)
#     c = ((p1[0] - p3[0]) ** 2) + ((p1[1] - p3[1]) ** 2)

#     side = sorted([a, b, c])

#     if side[0] + side[1] == side[2]:
#         ans += 1

# print(ans)