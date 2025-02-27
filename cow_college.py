import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

cost = list(map(int, input().split()))
cost_cow = Counter(cost)
sorted_cost = sorted(cost_cow.keys())

best_tuition = 0
total_tuition = 0

cows = sum(cost_cow.values())
for t in sorted_cost:
    tuition = t * cows
    if tuition > total_tuition :
        best_tuition = t
        total_tuition = tuition
    cows -= cost_cow[t]

print(total_tuition, best_tuition)