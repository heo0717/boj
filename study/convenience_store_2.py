import statistics
import sys
input = sys.stdin.readline

n = int(input())

x_coords, y_coords = zip(*(map(int, input().split()) for _ in range(n)))

x_loc = int(statistics.median(x_coords))
y_loc = int(statistics.median(y_coords))

distance = 0
for i in range(n):
    d = abs(x_loc - x_coords[i]) + abs(y_loc - y_coords[i])
    distance += d

print(distance) 