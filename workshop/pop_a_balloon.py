from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))

#-----------------풍선번호와 종이에 적힌 숫자를 같이 저장해야함
balloons = deque((i+1,value) for i, value in enumerate(nums))

order = []
while balloons :

    if not balloons: break

    idx, move = balloons.popleft()
    order.append(idx)

    if move > 0 :
        balloons.rotate(-(move-1))
    else :
        balloons.rotate(-move)

print(*order)