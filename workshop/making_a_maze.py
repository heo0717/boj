n = int(input())

m = list(input())

#south : +1 row / north : -1 row / east : +1 col / west : -1 col 
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir_idx = 0

x, y = 0, 0 #first_location
path = [(x, y)]

for i in m:
    if i == 'F':
        dx, dy = dir[dir_idx]
        x, y = x + dx, y + dy
        path.append((x, y))

    elif i == 'L': 
        dir_idx = (dir_idx - 1) % 4
    elif i == 'R':
        dir_idx = (dir_idx + 1) % 4

min_x = min(x[0] for x in path)
max_x = max(x[0] for x in path)
min_y = min(y[1] for y in path)
max_y = max(y[1] for y in path)

w = max_x - min_x + 1
h = max_y - min_y + 1

maze = [['#'] * w for _ in range(h)]

for (x,y) in path:
    maze[y - min_y][x - min_x] = '.'

for row in maze:
    print(''.join(row))