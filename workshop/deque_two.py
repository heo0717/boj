from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dec = deque()
i = 0
while i < n:
    order = input().strip().split()

    if order[0] == '1':
        dec.appendleft(int(order[1]))

    elif order[0] == '2':
        dec.append(int(order[1]))

    elif order[0] == '3':
        print( -1 if not dec else dec.popleft() )

    elif order[0] == '4':
        print( -1 if not dec else dec.pop() )

    elif order[0] == '5':
        print(len(dec))

    elif order[0] == '6':
        print( 1 if not dec else 0 )

    elif order[0] == '7':
        print( -1 if not dec else dec[0] )

    elif order[0] == '8':
        print( -1 if not dec else dec[-1] )

    i += 1 