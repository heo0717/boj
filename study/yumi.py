import math
from itertools import permutations


coords = [tuple(map(int, input().split())) for _ in range(4)]
yumi = coords[0]
people = coords[1:]

def distance(coords1, coords2):
    return math.sqrt((coords1[0]-coords2[0])**2 + (coords1[1]-coords2[1])**2)

min_total = float('inf')

for i in permutations(people):
    total = 0
    loc = yumi

    for f in i :
        total += distance(loc, f)
        loc = f

    min_total = min(min_total, total)

print(int(min_total))