import sys
input = sys.stdin.readline

N = int(input().strip())
x_coords, y_coords = zip(*(map(int, input().split()) for _ in range(N)))

distance = []
for i in range(1, N):
    dx = abs(x_coords[i] - x_coords[i-1])
    dy = abs(y_coords[i] - y_coords[i-1])
    distance.append(dx+dy)

total = sum(distance)
min_dist = total

for i in range( 1, N-1 ):
    no_skip = distance[i] + distance[i-1]
    skip = abs(x_coords[i+1] - x_coords[i-1]) + abs(y_coords[i+1] - y_coords[i-1])
    new_total =total - no_skip + skip
    min_dist = min(min_dist, new_total)

print(min_dist)