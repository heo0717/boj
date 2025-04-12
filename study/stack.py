import sys
input = sys.stdin.readline

n = int(input().strip())

stack = []
i = 0
while i < n:
    order = input().strip().split()

    if order[0] == 'push':
        stack.append(int(order[1]))

    elif order[0] == 'pop':
        if not stack :
            print('-1')
        else:
            p = stack.pop(-1)
            print(p)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        print( 1 if not stack else 0)

    elif order[0] == 'top':
        print( -1 if not stack else stack[-1])

    i += 1 