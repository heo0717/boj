#Sprider Solitaire
import sys
import math

input = sys.stdin.readline

x, y = map(int, input().split()) 
#X: num of games / Y: num of winning games / Z: winning ratio

z = (y* 100) // x

if z >= 99 :
    print(-1)
    exit()

left, right = 1, x
ans = -1

while left <= right :
    i = (left + right) // 2
    Z = ((y + i)*100) // ( x+i )

    if Z > z:
        ans = i
        right = i - 1

    else:
        left = i + 1

print(ans)
#---------------------------------------------------time over

# for i in range(1, x+1):
    
#     Z = math.floor(((y+i)/(x+i)) * 100)

#     if Z > z :
#         print(f'{i}')

#         break

# if Z == z:
#     print('-1')