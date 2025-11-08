import math

N = int(input())

# 0 : none , 1 : student , 2 : SG , 5 : professor

# 1. 입력받을때 반복문 실행 순서로 R을 인덱스값으로 C를 구해서 각 번호마다의 위치를 저장
# 2. 2와 5 사이의 거리를 구한다.
    # 2-1. 같은 행, 같은 열인 경우를 먼저 계산 ( col or row 둘중 한가지만 구하면 됨 )
    # 2-2. 아닌 경우, 직사각형으로 col과 row를 구하기
# 3. 그 사이 학생들의 수를 구한다.

num = {1,2,5}

student = []
sg = ()
prof = ()

for i in range(N):
    s = list(map(int, input().split()))
    
    if num & set(s) :
        
        if 1 in s :
            s1 = [ i for i, x in enumerate(s) if x == 1 ]
            student_loc = [ (i, idx) for idx in s1 ] 
            student.extend(student_loc)

        if 2 in s :
            s2 = s.index(2)
            sg = (i, s2)

        if 5 in s :
            s5 = s.index(5)
            prof = (i, s5)

# print(student)
# print(sg)
# print(prof)

# 첫번째 조건, 교수와의 거리가 5 이상인가?

dist = math.sqrt((prof[0] - sg[0]) ** 2 + (prof[1] - sg[1]) ** 2)

if dist < 5 :
    print(0)
else:

    # 교수님과 같은 행,열에 앉은 경우

    cnt = 0

    if sg[0] == prof[0] : #같은 행

        l, r = sorted([sg[1],prof[1]])
        for s in student :
            if s[0] == sg[0] and l < s[1] < r :
                cnt += 1

    elif sg[1] == prof[1] : #같은 행

        l, r = sorted([sg[0],prof[0]])
        for s in student :
            if s[1] == sg[1] and l < s[0] < r :
                cnt += 1

    # 교수님과 대각선으로 앉은 경우

    else :
        l_x , r_x = sorted([sg[0],prof[0]])
        l_y , r_y = sorted([sg[1],prof[1]])
        
        for x, y in student :
            if l_x <= x <= r_x and l_y <= y <= r_y :
                cnt += 1

    if cnt >= 3 : print(1)
    else : print(0)