import sys
input = sys.stdin.readline

T = int(input().strip())

cnt = 0
while True :
    if cnt == T : break

    #a:horizontal b:vertical c:height
    a, b, c = map(int, input().split()) 

    x_1 = a ** 2 + ( b + c ) ** 2

    x_2 = b ** 2 + ( a + c ) ** 2

    x_3 = c ** 2 + ( a + b ) ** 2

    print(min(x_1, x_2, x_3))

    cnt += 1