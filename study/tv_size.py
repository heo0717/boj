import math
import sys
input = sys.stdin.readline

d, r_h, r_w = map(int, input().split())

x = d  / math.sqrt((r_h ** 2) + ( r_w ** 2 ))

h = math.floor(x * r_h)
w = math.floor(x * r_w)

print(h, w)