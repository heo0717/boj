import math
import sys

input = sys.stdin.readline

d_1 = int(input())
d_2 = int(input())

ground = ( 2 * math.pi * d_2 ) + ( 2 * d_1 )
print(ground)