from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())

ratio = Counter(input().strip() for _ in range(n))
pizza = 0

pizza += ratio['3/4']
ratio['1/4'] = max(0, ratio['1/4'] - ratio['3/4'])

pizza += ratio['1/2'] // 2
if ratio['1/2'] % 2 != 0 :
    pizza += 1
    ratio['1/4'] = max(0, ratio['1/4'] - 2)

pizza += ( ratio['1/4'] + 3 ) // 4

print(pizza)