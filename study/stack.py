import sys
input = sys.stdin.readline

n = int(input().strip())

queue = []
i = 0
while i < n:
    order = input().strip().split()

    if order[0] == 'push':
        queue.append(int(order[1]))

    elif order[0] == 'pop':
        if not queue :
            print('-1')
        else:
            p = queue.pop(-1)
            print(p)

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        print( 1 if not queue else 0)

    elif order[0] == 'top':
        print( -1 if not queue else queue[-1])

    i += 1 