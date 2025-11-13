import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map = []
for _ in range(R):    
    m = list(input().strip())
    map.append(m)

# step 1.  x의 상하좌우 체크. 맨끝에 있다면 바다와 한부분은 접해있다고 카운트

dir = [(-1,0), (1,0), (0,-1), (0,1)]

c = [] # 바다로 바뀌는 지점
o = [] # 바뀌지않는 X 위치

for i in range(R):
    for j in range(C):
        
        if map[i][j] == 'X' :
            sea_cnt = 0

            for di, dj in dir :
                mi = i + di
                mj = j + dj
                
                if mi < 0 or mi >= R or mj < 0 or mj >= C : # 등호를 추가해야 list index out of range에러가 뜨지않음
                    sea_cnt += 1

                elif map[mi][mj] == '.':
                    sea_cnt += 1
            
            if sea_cnt >= 3 :
                c.append((i,j))
            else : o.append((i,j))

# step 2. 삼면이상인 . 인 x를 .으로 바꿀 것

for i, j in c :
    map[i][j] = '.'

# step 3. 마지막에 남는 x와 x 사이의 .만 남기고 그 외의 영역의 .은 삭제할 것

first_values = [ x[0] for x in o ]
second_values = [ x[1] for x in o ]

min_r = min(first_values)
max_r = max(first_values)

min_c = min(second_values)
max_c = max(second_values)


after_map = []

for row in map[min_r:max_r+1]:
    af = row[min_c:max_c+1]
    after_map.append(af)

# # step 4. 출력
    
for row in after_map:
    print(''.join(row))