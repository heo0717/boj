import sys
input = sys.stdin.readline

n = int(input().strip())

stack = []
i = 0
while i < n:
    order = input().strip().split()

    if order[0] == '1':
        stack.append(int(order[1]))

    elif order[0] == '2':
        if not stack :
            print('-1')
        else:
            p = stack.pop()
            print(p)

    elif order[0] == '3':
        print(len(stack))

    elif order[0] == '4':
        print( 1 if not stack else 0)

    elif order[0] == '5':
        print( -1 if not stack else stack[-1])

    i += 1 