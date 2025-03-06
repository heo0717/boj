def rotation_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def can_stamp(N,painting,stamps):
    canvas = [['.']*N for _ in range(N)]

    for stamp in stamps:
        K_row = len(stamp)
        K_col = len(stamp[0])

        for i in range(N-K_row+1):
            for j in range(N-K_col+1):
                can_paint = True
                
                for x in range(K_row):
                    for y in range(K_col):
                        if stamp[x][y] == '*':
                            if painting[i+x][j+y] == '*':
                                continue
                            else:
                                can_paint = False
                                break

                    if not can_paint:
                        break
                        
                if can_paint:
                    for x in range(K_row):
                        for y in range(K_col):
                            if stamp[x][y] == '*':
                                canvas[i+x][j+y] = '*'
                                
    return canvas == painting

#-------------------------------------------------------

T = int(input().strip())
empty_line = input().strip() 

for _ in range(T):
    N = int(input().strip())
    painting = [list(input().strip()) for _ in range(N)]
        
    K = int(input().strip())
    stamp = [list(input().strip()) for _ in range(K)]

    #-------------------------------------------------------

    stamp_0 = stamp 
    stamp_90 = rotation_90(stamp_0)
    stamp_180 = rotation_90(stamp_90)
    stamp_270 = rotation_90(stamp_180)
    stamps = [stamp_0, stamp_90, stamp_180, stamp_270]

    #-------------------------------------------------------

    if can_stamp(N,painting,stamps) :
        print('YES')
    else :
        print('NO')

    if _ < T-1 :
        empty = input().strip()
        if empty == "":
            continue