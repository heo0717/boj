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
            p = queue.pop(0)
            print(p)

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        if not queue: print('1')
        else: print('0')

    elif order[0] == 'front':
        if not queue: print('-1')
        else: print(queue[0]) #값만 출력하고 제거는 X

    elif order[0] == 'back':
        if not queue: print('-1')
        else: print(queue[-1]) #값만 출력하고 제거는 X

    i += 1 