import sys
input = sys.stdin.readline
#파이썬은 재귀가 많아지면 중단함. 따라서 limit을 만들어놓기
sys.setrecursionlimit(2500)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1,-1, 0, 1, 1, 1, 0, -1]

def dfs(x, y, w, h, matrix):
    matrix[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w : continue
        if matrix[nx][ny] == 0 : continue
        dfs(nx, ny, w, h, matrix)

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break

    matrix = []
    for i in range(h):
        line = list(map(int, input().split()))
        matrix.append(line)

    ans = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i, j, w, h, matrix)
                ans += 1

print(ans)