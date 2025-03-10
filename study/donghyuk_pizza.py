import sys
input = sys.stdin.readline

cnt = 1
while True:
    
    a = list(map(int, input().split()))

    if a[0] == 0 :
        break

    else :
        r, w, h = a
        diagonal = ( w ** 2 + h ** 2 ) ** 0.5

        if diagonal / 2 <= r :
            print(f'Pizza {cnt} fits on the table.')
        else :
            print(f'Pizza {cnt} does not fit on the table.')

        cnt += 1