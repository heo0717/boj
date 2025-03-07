import sys
input = sys.stdin.readline

chess_board = [input().strip() for _ in range(8)]

cnt = 0
#짝수
for i in range(0,8,2):
    for j in range(0,8,2):
        if chess_board[i][j] == 'F':
            cnt += 1

#홀수
for i in range(1,8,2):
    for j in range(1,8,2):
        if chess_board[i][j] == 'F':
            cnt += 1

print(cnt)